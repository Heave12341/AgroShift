import asyncio, json, time, os, math, sys
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any
import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, ORJSONResponse, StreamingResponse
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# Ensure backend and repository root directories are in sys.path
# so imports succeed whether invoked via `uvicorn backend.main:app` from root
# or `uvicorn main:app` from inside backend.
_backend_dir = os.path.dirname(os.path.abspath(__file__))
_repo_root = os.path.dirname(_backend_dir)
if _backend_dir not in sys.path:
    sys.path.insert(0, _backend_dir)
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)

import nasa_power, modis_ornl, analysis, config, rotation
from common import unavailable

PATNA = (25.5941, 85.1376)
WARM_YEARS = (2022, 2025)
client: httpx.AsyncClient | None = None


class SelectiveGZip(GZipMiddleware):
    """Skip gzip for SSE. Compression buffers small events, so progress would arrive late."""

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and str(scope.get("path", "")).endswith("/stream"):
            await self.app(scope, receive, send)
            return
        await super().__call__(scope, receive, send)


async def _warm():
    if not config.WARM_CACHE:
        return
    try:
        await nasa_power.fetch_power(client, *PATNA, *WARM_YEARS)
        await modis_ornl.fetch_ndvi(client, *PATNA, *WARM_YEARS)
        print("warm cache ready for Patna", WARM_YEARS)
    except Exception as exc:
        print("warm cache failed:", type(exc).__name__, exc)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client
    client = httpx.AsyncClient(headers={"User-Agent": "RotationIQ-SpaceApps"}, timeout=httpx.Timeout(60.0))
    warm = asyncio.create_task(_warm())
    yield
    warm.cancel()
    await client.aclose()
    client = None


app = FastAPI(title="Rotation IQ API", default_response_class=ORJSONResponse, lifespan=lifespan)
app.add_middleware(SelectiveGZip, minimum_size=1000)

DEFAULT_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
env_origins = os.getenv("CORS_ORIGINS", "")
allowed_origins = [o.strip() for o in env_origins.split(",") if o.strip()] if env_origins else DEFAULT_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.middleware("http")
async def timing(request, call_next):
    t = time.perf_counter()
    resp = await call_next(request)
    resp.headers["Server-Timing"] = f"total;dur={(time.perf_counter() - t) * 1000:.0f}"
    return resp


def http() -> httpx.AsyncClient:
    global client
    if client is None or client.is_closed:
        client = httpx.AsyncClient(headers={"User-Agent": "RotationIQ-SpaceApps"}, timeout=httpx.Timeout(60.0))
    return client


def sanitize_json(obj):
    """Recursively converts NaN and Infinity floats to None (valid JSON null)."""
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    elif isinstance(obj, dict):
        return {k: sanitize_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_json(v) for v in obj]
    elif isinstance(obj, tuple):
        return [sanitize_json(v) for v in obj]
    return obj


def validate_inputs(
    lat: float,
    lon: float,
    start_year: int,
    end_year: int,
    min_year: int = config.POWER_MIN_YEAR,
    current_max_year: int = 2026,
):
    if not (-90.0 <= lat <= 90.0):
        raise HTTPException(status_code=422, detail="Latitude must be between -90.0 and 90.0")
    if not (-180.0 <= lon <= 180.0):
        raise HTTPException(status_code=422, detail="Longitude must be between -180.0 and 180.0")
    if start_year < min_year:
        raise HTTPException(status_code=422, detail=f"start_year must be at least {min_year}")
    if end_year < start_year:
        raise HTTPException(status_code=422, detail="end_year must be greater than or equal to start_year")
    if end_year > current_max_year:
        raise HTTPException(status_code=422, detail=f"end_year must not exceed {current_max_year}")
    if end_year - start_year + 1 > config.MAX_SPAN_YEARS:
        raise HTTPException(
            status_code=422,
            detail=f"Requested range ({end_year - start_year + 1} years) exceeds max span ({config.MAX_SPAN_YEARS} years)",
        )


@app.get("/api/health")
async def health():
    return {"ok": True}


@app.get("/api/data/power")
async def power(lat: float, lon: float, start_year: int = 2000, end_year: int = 2025):
    validate_inputs(lat, lon, start_year, end_year, min_year=config.POWER_MIN_YEAR)
    return await nasa_power.fetch_power(http(), lat, lon, start_year, end_year)


@app.get("/api/data/ndvi")
async def ndvi(lat: float, lon: float, start_year: int = 2000, end_year: int = 2025):
    validate_inputs(lat, lon, start_year, end_year, min_year=config.NDVI_MIN_YEAR)
    return await modis_ornl.fetch_ndvi(http(), lat, lon, start_year, end_year)


@app.get("/api/data/ndvi/stream")
async def ndvi_stream(lat: float, lon: float, start_year: int = 2000, end_year: int = 2025):
    validate_inputs(lat, lon, start_year, end_year, min_year=config.NDVI_MIN_YEAR)
    queue: asyncio.Queue = asyncio.Queue()

    async def worker():
        try:
            result = await modis_ornl.fetch_ndvi(
                http(), lat, lon, start_year, end_year, progress=queue.put
            )
            await queue.put({"step": "result", "result": result})
        except Exception as exc:
            await queue.put(
                {
                    "step": "result",
                    "result": unavailable("MODIS MOD13Q1 (ORNL)", f"{type(exc).__name__}: {exc}"),
                }
            )
        finally:
            await queue.put(None)

    async def gen():
        task = asyncio.create_task(worker())
        try:
            while True:
                event = await queue.get()
                if event is None:
                    break
                yield f"data: {json.dumps(event)}\n\n"
        finally:
            if not task.done():
                task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    return StreamingResponse(
        gen(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/api/analysis/climate")
async def analysis_climate(
    lat: float = Query(..., description="Latitude in degrees (-90 to 90)"),
    lon: float = Query(..., description="Longitude in degrees (-180 to 180)"),
    start_year: int = Query(2000, description="Start year"),
    end_year: int = Query(2025, description="End year"),
    baseline_start: int | None = Query(None, description="Baseline start year"),
    baseline_end: int | None = Query(None, description="Baseline end year"),
    min_completeness: float | None = Query(None, description="Min completeness fraction (0, 1]"),
):
    validate_inputs(lat, lon, start_year, end_year, min_year=config.POWER_MIN_YEAR)
    b_start = config.BASELINE_START if baseline_start is None else baseline_start
    b_end = config.BASELINE_END if baseline_end is None else baseline_end
    if min_completeness is not None and not (0 < min_completeness <= 1.0):
        raise HTTPException(status_code=422, detail="min_completeness must be in (0, 1]")

    fetch_start, fetch_end = analysis.power_fetch_years(
        start_year, end_year, b_start, b_end, min_year=config.POWER_MIN_YEAR
    )
    payload = await nasa_power.fetch_power(http(), lat, lon, fetch_start, fetch_end)
    if not payload.get("available"):
        return payload

    return sanitize_json(analysis.analyze_climate(
        payload,
        lat=lat,
        lon=lon,
        start_year=start_year,
        end_year=end_year,
        baseline_start=baseline_start,
        baseline_end=baseline_end,
        min_completeness=min_completeness,
    ))


@app.get("/api/analysis/trends")
async def analysis_trends(
    lat: float = Query(..., description="Latitude in degrees (-90 to 90)"),
    lon: float = Query(..., description="Longitude in degrees (-180 to 180)"),
    start_year: int = Query(2000, description="Start year"),
    end_year: int = Query(2025, description="End year"),
    min_completeness: float | None = Query(None, description="Min completeness fraction (0, 1]"),
    alpha: float | None = Query(None, description="Two-sided significance level (0, 1)"),
    min_years: int | None = Query(None, description="Minimum complete years required"),
):
    validate_inputs(lat, lon, start_year, end_year, min_year=config.POWER_MIN_YEAR)
    if min_completeness is not None and not (0 < min_completeness <= 1.0):
        raise HTTPException(status_code=422, detail="min_completeness must be in (0, 1]")
    if alpha is not None and not (0 < alpha < 1.0):
        raise HTTPException(status_code=422, detail="alpha must be in (0, 1)")
    if min_years is not None and min_years < 4:
        raise HTTPException(status_code=422, detail="min_years must be at least 4")

    payload = await nasa_power.fetch_power(http(), lat, lon, start_year, end_year)
    if not payload.get("available"):
        return payload

    return sanitize_json(analysis.analyze_trends(
        payload,
        lat=lat,
        lon=lon,
        start_year=start_year,
        end_year=end_year,
        min_completeness=min_completeness,
        alpha=alpha,
        min_years=min_years,
    ))


async def _build_vegetation_result(
    lat: float,
    lon: float,
    start_year: int,
    end_year: int,
    fallback: bool,
    progress=None,
):
    """Fetch and analyse plant-growth data, optionally reporting progress."""
    async def report(event: dict):
        if progress is not None:
            await progress(event)

    fetch_start = max(config.NDVI_MIN_YEAR, start_year - 1)
    await report({"step": "connecting", "message": "Connecting to the MODIS satellite-data service"})
    try:
        # A new point can take ~20 seconds just to return its date list. A
        # multi-year series then needs many subset calls, so allow more than
        # one short web-request window for the full operation.
        payload = await asyncio.wait_for(
            modis_ornl.fetch_ndvi(http(), lat, lon, fetch_start, end_year, progress=report),
            timeout=180.0,
        )
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        reason = "The satellite service took too long to answer. Please try again."
        if not isinstance(exc, (asyncio.TimeoutError, TimeoutError)):
            reason = f"Satellite data could not be downloaded: {type(exc).__name__}. Please try again."
        payload = {
            "available": False,
            "reason": reason,
            "location": {"lat": lat, "lon": lon, "source": "ORNL DAAC MODIS"},
        }
        await report({"step": "unavailable", "message": reason})

    is_fallback = False
    if not payload.get("available"):
        if fallback:
            await report({"step": "estimate", "message": "Live satellite data is unavailable. Preparing a clearly labelled example estimate."})
            payload = modis_ornl.generate_illustrative_baseline_payload(lat, lon, fetch_start, end_year)
            is_fallback = True
        else:
            return payload

    await report({"step": "analysis", "message": "Preparing the plant-growth chart"})
    result = analysis.analyze_vegetation(
        payload,
        lat=lat,
        lon=lon,
        start_year=start_year,
        end_year=end_year,
    )
    if is_fallback or payload.get("is_fallback"):
        result["is_fallback"] = True
        result["fallback_notice"] = payload.get(
            "fallback_notice",
            "Live NASA MODIS data could not be retrieved. This is an illustrative computer-made estimate, not an observed satellite reading or a measurement of your field.",
        )
    return sanitize_json(result)


@app.get("/api/analysis/vegetation")
async def analysis_vegetation(
    lat: float = Query(..., description="Latitude in degrees (-90 to 90)"),
    lon: float = Query(..., description="Longitude in degrees (-180 to 180)"),
    start_year: int = Query(2000, description="Start year"),
    end_year: int = Query(2025, description="End year"),
    fallback: bool = Query(False, description="Enable clearly labelled illustrative estimate if live satellite data is unavailable"),
):
    validate_inputs(lat, lon, start_year, end_year, min_year=config.NDVI_MIN_YEAR)
    return await _build_vegetation_result(lat, lon, start_year, end_year, fallback)


@app.get("/api/analysis/vegetation/stream")
async def analysis_vegetation_stream(
    lat: float = Query(..., description="Latitude in degrees (-90 to 90)"),
    lon: float = Query(..., description="Longitude in degrees (-180 to 180)"),
    start_year: int = Query(2000, description="Start year"),
    end_year: int = Query(2025, description="End year"),
    fallback: bool = Query(True, description="Enable a clearly labelled example estimate if live satellite data is unavailable"),
):
    """Progress-enabled vegetation endpoint so the user never sees a silent blank panel."""
    validate_inputs(lat, lon, start_year, end_year, min_year=config.NDVI_MIN_YEAR)
    queue: asyncio.Queue = asyncio.Queue()

    async def report(event: dict):
        await queue.put(event)

    async def worker():
        try:
            result = await _build_vegetation_result(lat, lon, start_year, end_year, fallback, report)
            await queue.put({"step": "result", "result": result})
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            await queue.put({
                "step": "result",
                "result": {
                    "available": False,
                    "reason": f"Plant-growth information could not be prepared ({type(exc).__name__}). Please try again.",
                    "location": {"lat": lat, "lon": lon, "source": "ORNL DAAC MODIS"},
                },
            })
        finally:
            await queue.put(None)

    async def generate():
        task = asyncio.create_task(worker())
        try:
            while True:
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=15.0)
                except asyncio.TimeoutError:
                    event = {"step": "waiting", "message": "Still waiting for satellite pictures. A new place can take longer the first time."}
                if event is None:
                    break
                yield f"data: {json.dumps(event)}\n\n"
        finally:
            if not task.done():
                task.cancel()

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


class FarmerProfileInput(BaseModel):
    area_acres: float = Field(2.5, description="Farm area in acres")
    soil_type: str = Field("alluvial", description="Soil type (alluvial, clay_loam, sandy_loam, silt_loam, black_cotton, red_laterite)")
    soil_ph: float | None = Field(None, description="Measured soil pH (optional, 4.0-9.5)")
    organic_carbon_pct: float | None = Field(None, description="Soil organic carbon percentage (optional, 0.1-5.0)")
    irrigation: str = Field("assured_tubewell", description="Irrigation status (assured_canal, assured_tubewell, partial, rainfed)")
    current_rotation: str = Field("rice_wheat", description="Current rotation practice")
    priority: str = Field("water_conservation", description="Farmer priority (water_conservation, soil_improvement, income_stability, balanced)")
    lat: float | None = Field(None, description="Farm latitude in degrees")
    lon: float | None = Field(None, description="Farm longitude in degrees")
    climate_summary: dict[str, Any] | None = Field(None, description="Optional NASA POWER climate summary statistics")


class CustomRotationInput(BaseModel):
    crop_ids: list[str] = Field(..., min_length=1, max_length=5, description="List of crop IDs in rotational sequence")
    area_acres: float = Field(2.5, description="Farm area in acres")
    soil_type: str = Field("alluvial", description="Soil type")
    soil_ph: float | None = Field(None, description="Measured soil pH (optional, 4.0-9.5)")
    organic_carbon_pct: float | None = Field(None, description="Soil organic carbon percentage (optional, 0.1-5.0)")
    irrigation: str = Field("assured_tubewell", description="Irrigation status")
    priority: str = Field("balanced", description="Farmer priority")
    lat: float | None = Field(None, description="Farm latitude in degrees")
    lon: float | None = Field(None, description="Farm longitude in degrees")
    climate_summary: dict[str, Any] | None = Field(None, description="Optional NASA POWER climate summary statistics")


@app.post("/api/rotation/evaluate")
async def post_evaluate_rotation(profile: FarmerProfileInput):
    data = profile.model_dump()
    climate_summary = data.pop("climate_summary", None)
    return sanitize_json(rotation.evaluate_rotations(data, climate_summary=climate_summary))


@app.get("/api/rotation/evaluate")
async def get_evaluate_rotation(
    area_acres: float = 2.5,
    soil_type: str = "alluvial",
    soil_ph: float | None = None,
    organic_carbon_pct: float | None = None,
    irrigation: str = "assured_tubewell",
    current_rotation: str = "rice_wheat",
    priority: str = "water_conservation",
    lat: float | None = None,
    lon: float | None = None,
):
    prof = {
        "area_acres": area_acres,
        "soil_type": soil_type,
        "soil_ph": soil_ph,
        "organic_carbon_pct": organic_carbon_pct,
        "irrigation": irrigation,
        "current_rotation": current_rotation,
        "priority": priority,
        "lat": lat,
        "lon": lon,
    }
    return sanitize_json(rotation.evaluate_rotations(prof))


@app.post("/api/rotation/evaluate-custom")
async def post_evaluate_custom_rotation(req: CustomRotationInput):
    unknown = [cid for cid in req.crop_ids if cid not in rotation.CROPS]
    if unknown:
        raise HTTPException(status_code=422, detail=f"Unknown crop ID(s): {', '.join(unknown)}")

    prof = {
        "area_acres": req.area_acres,
        "soil_type": req.soil_type,
        "soil_ph": req.soil_ph,
        "organic_carbon_pct": req.organic_carbon_pct,
        "irrigation": req.irrigation,
        "priority": req.priority,
        "lat": req.lat,
        "lon": req.lon,
    }
    return sanitize_json(rotation.evaluate_custom_rotation(req.crop_ids, prof, climate_summary=req.climate_summary))


@app.get("/api/rotation/crops/summary")
async def get_crops_summary():
    import crops_registry
    return sanitize_json(crops_registry.get_catalog_stats())


@app.get("/api/rotation/crops/{crop_id}")
async def get_single_crop(crop_id: str):
    crop = rotation.CROPS.get(crop_id)
    if not crop:
        raise HTTPException(status_code=404, detail=f"Crop with ID '{crop_id}' not found in registry.")
    return sanitize_json(crop)


@app.get("/api/rotation/crops")
async def get_crops(
    category: str | None = Query(None),
    family: str | None = Query(None),
    season: str | None = Query(None),
    region: str | None = Query(None),
    zone: str | None = Query(None),
    q: str | None = Query(None),
    limit: int | None = Query(None, ge=1, le=2000),
    offset: int = Query(0, ge=0),
):
    crops = rotation.CROPS
    result = {}
    for cid, crop in crops.items():
        cats = [str(cat).lower() for cat in crop.get("categories", [])]
        primary = str(crop.get("primary_category", "")).lower()
        if category and category.lower() not in cats and category.lower() != primary:
            continue
        if family and family.lower() != str(crop.get("crop_family", "")).lower():
            continue
        if season and season.lower() not in str(crop.get("season", "")).lower() and "annual" not in str(crop.get("season", "" )).lower():
            continue
        if region:
            suitability = (crop.get("regional_suitability") or {}).get(region.lower(), "low")
            if suitability not in ("high", "moderate"):
                continue
        if zone and zone.lower() not in [str(z).lower() for z in crop.get("climatic_zones", [])]:
            continue
        if q:
            needle = q.strip().lower()
            searchable = [cid, crop.get("name", ""), crop.get("scientific_name", ""), crop.get("crop_family", "")]
            searchable += list(crop.get("synonyms", []) or []) + cats
            if not any(needle in str(item).lower() for item in searchable):
                continue
        result[cid] = crop
    items = list(result.items())[offset:]
    if limit is not None:
        items = items[:limit]
    return sanitize_json(dict(items))


_static_root = Path(_repo_root)


@app.get("/", include_in_schema=False)
async def landing_page():
    return FileResponse(_static_root / "index.html")


@app.get("/styles.css", include_in_schema=False)
async def landing_styles():
    return FileResponse(_static_root / "styles.css")


app.mount("/images", StaticFiles(directory=str(_static_root / "images")), name="site-images")
app.mount(
    "/dashboard",
    StaticFiles(directory=str(_static_root / "dashboard"), html=True),
    name="dashboard",
)

