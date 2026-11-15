import { useState, useEffect, useRef, type FormEvent } from "react";
import {
  fetchClimateAnalysis,
  fetchTrendAnalysis,
  fetchVegetationAnalysis,
} from "./api";
import type {
  ClimateAnalysisResponse,
  TrendAnalysisResponse,
  VegetationAnalysisResponse,
  ProgressEvent,
} from "./types";
import MapPicker, { resolvePlaceSearch } from "./MapPicker";
import RotationLab from "./RotationLab";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
  ReferenceLine,
} from "recharts";

const PRESETS = [
  { name: "Patna", lat: 25.5941, lon: 85.1376, region: "Middle Gangetic Plains (Bihar)" },
  { name: "Chennai", lat: 13.0827, lon: 80.2707, region: "Southern Peninsular Coastal (TN)" },
  { name: "Hyderabad", lat: 17.3850, lon: 78.4867, region: "Deccan Plateau (Telangana)" },
  { name: "Pune", lat: 18.5204, lon: 73.8567, region: "Western Scarcity Zone (Maharashtra)" },
  { name: "Indore", lat: 22.7196, lon: 75.8577, region: "Malwa Plateau (Madhya Pradesh)" },
  { name: "Ludhiana", lat: 30.9010, lon: 75.8573, region: "Trans-Gangetic Plains (Punjab)" },
  { name: "Ahmedabad", lat: 23.0225, lon: 72.5714, region: "North Gujarat Semi-Arid" },
  { name: "Varanasi", lat: 25.3176, lon: 82.9739, region: "Eastern Alluvial Plain (UP)" },
  { name: "Kolkata", lat: 22.5726, lon: 88.3639, region: "Lower Gangetic Delta (West Bengal)" },
];

const DEFAULT_LOCATION = { lat: 25.5941, lon: 85.1376 };
const SAVED_LOCATION_KEY = "vasundhara-dashboard-location";
const SKIPPED_LOCATION_SETUP_KEY = "vasundhara-dashboard-location-setup-skipped";

interface DashboardLocation {
  lat: number;
  lon: number;
}

function readSavedLocation(): DashboardLocation | null {
  try {
    const stored = window.localStorage.getItem(SAVED_LOCATION_KEY);
    if (!stored) return null;

    const location = JSON.parse(stored) as DashboardLocation;
    if (
      Number.isFinite(location.lat) && location.lat >= -90 && location.lat <= 90 &&
      Number.isFinite(location.lon) && location.lon >= -180 && location.lon <= 180
    ) {
      return location;
    }
  } catch {
    return null;
  }
  return null;
}

function hasSkippedLocationSetup(): boolean {
  try {
    return window.localStorage.getItem(SKIPPED_LOCATION_SETUP_KEY) === "true";
  } catch {
    return false;
  }
}

function farmerFriendlyVegetationProgress(event: ProgressEvent): { message: string; percent: number | null } {
  switch (event.step) {
    case "connecting":
      return { message: "Connecting to the satellite picture service…", percent: null };
    case "cache":
      return { message: "Checking saved satellite pictures for this place…", percent: null };
    case "dates":
      return { message: "Finding the dates of satellite pictures…", percent: null };
    case "chunk":
      return {
        message: event.done && event.total
          ? `Reading satellite pictures: ${event.done} of ${event.total} groups…`
          : "Reading satellite pictures…",
        percent: event.done && event.total ? Math.round((event.done / event.total) * 100) : null,
      };
    case "waiting":
      return { message: "This place is taking longer than usual. Still trying…", percent: null };
    case "unavailable":
      return { message: "Live satellite pictures are not available right now. Checking what can be shown…", percent: null };
    case "estimate":
      return { message: "Preparing an example only. This is not a real satellite reading…", percent: null };
    case "analysis":
      return { message: "Preparing the plant-growth chart…", percent: 100 };
    default:
      return { message: event.message || "Loading plant-growth pictures for this place…", percent: null };
  }
}

export default function App() {
  const [initialLocation] = useState(readSavedLocation);
  const [lat, setLat] = useState<number>(initialLocation?.lat ?? DEFAULT_LOCATION.lat);
  const [lon, setLon] = useState<number>(initialLocation?.lon ?? DEFAULT_LOCATION.lon);
  const [inputLat, setInputLat] = useState<string>((initialLocation?.lat ?? DEFAULT_LOCATION.lat).toFixed(4));
  const [inputLon, setInputLon] = useState<string>((initialLocation?.lon ?? DEFAULT_LOCATION.lon).toFixed(4));
  const [locationPromptOpen, setLocationPromptOpen] = useState(
    () => !initialLocation && !hasSkippedLocationSetup()
  );
  const [locationSearch, setLocationSearch] = useState("");
  const [locationSearchError, setLocationSearchError] = useState<string | null>(null);
  const [locationSearching, setLocationSearching] = useState(false);
  const [locationStorageWarning, setLocationStorageWarning] = useState<string | null>(null);
  const [startYear, setStartYear] = useState<number>(2015);
  const [endYear, setEndYear] = useState<number>(2024);

  const [activeTab, setActiveTab] = useState<"climate" | "rainfall" | "trends" | "vegetation" | "rotation" | "quality">("rotation");
  const [showMap, setShowMap] = useState<boolean>(true);

  const [climateData, setClimateData] = useState<ClimateAnalysisResponse | null>(null);
  const [trendData, setTrendData] = useState<TrendAnalysisResponse | null>(null);
  const [vegData, setVegData] = useState<VegetationAnalysisResponse | null>(null);
  const [vegDataLocation, setVegDataLocation] = useState<{ lat: number; lon: number; startYear: number; endYear: number } | null>(null);
  const [vegRetryCount, setVegRetryCount] = useState<number>(0);
  const [vegAllowFallback, setVegAllowFallback] = useState<boolean>(true);
  const [vegCancelled, setVegCancelled] = useState<boolean>(false);

  const [loading, setLoading] = useState<boolean>(true);
  const [vegLoading, setVegLoading] = useState<boolean>(false);
  const [vegProgress, setVegProgress] = useState<string>("");
  const [vegProgressPct, setVegProgressPct] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [vegError, setVegError] = useState<string | null>(null);

  const latestRequestIdRef = useRef<number>(0);
  const latestVegRequestIdRef = useRef<number>(0);
  const vegAbortControllerRef = useRef<AbortController | null>(null);

  const cancelVegetationFetch = () => {
    if (vegAbortControllerRef.current) {
      vegAbortControllerRef.current.abort();
      vegAbortControllerRef.current = null;
    }
    latestVegRequestIdRef.current += 1;
    setVegLoading(false);
    setVegProgress("");
    setVegProgressPct(null);
    setVegCancelled(true);
  };

  const retryVegetation = (allowFallback = true) => {
    setVegAllowFallback(allowFallback);
    setVegRetryCount((current) => current + 1);
  };

  const loadData = async (targetLat = lat, targetLon = lon) => {
    const requestId = ++latestRequestIdRef.current;
    setLoading(true);
    setError(null);
    try {
      const [climateRes, trendRes] = await Promise.all([
        fetchClimateAnalysis(targetLat, targetLon, startYear, endYear),
        fetchTrendAnalysis(targetLat, targetLon, startYear, endYear),
      ]);
      if (requestId !== latestRequestIdRef.current) return;
      setClimateData(climateRes);
      setTrendData(trendRes);
    } catch (err: any) {
      if (requestId !== latestRequestIdRef.current) return;
      setError(err?.message || "Failed to load climate & trend data");
    } finally {
      if (requestId === latestRequestIdRef.current) {
        setLoading(false);
      }
    }
  };


  const handleLocationChange = (newLat: number, newLon: number) => {
    setLat(newLat);
    setLon(newLon);
    setInputLat(newLat.toFixed(4));
    setInputLon(newLon.toFixed(4));
    try {
      window.localStorage.setItem(SAVED_LOCATION_KEY, JSON.stringify({ lat: newLat, lon: newLon }));
      window.localStorage.removeItem(SKIPPED_LOCATION_SETUP_KEY);
      setLocationStorageWarning(null);
    } catch {
      setLocationStorageWarning("Your location is selected, but this browser could not save it for your next visit.");
    }
    if (newLat === lat && newLon === lon && !locationPromptOpen) {
      loadData(newLat, newLon);
    }
    // The plant-growth effect follows the selected coordinates automatically.
  };

  const applyCoordinates = () => {
    const parsedLat = parseFloat(inputLat);
    const parsedLon = parseFloat(inputLon);
    if (
      !isNaN(parsedLat) &&
      !isNaN(parsedLon) &&
      parsedLat >= -90 &&
      parsedLat <= 90 &&
      parsedLon >= -180 &&
      parsedLon <= 180
    ) {
      handleLocationChange(parsedLat, parsedLon);
    } else {
      setInputLat(lat.toFixed(4));
      setInputLon(lon.toFixed(4));
    }
  };

  const searchForInitialLocation = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLocationSearchError(null);
    setLocationSearching(true);
    try {
      const location = await resolvePlaceSearch(locationSearch);
      if (!location) {
        setLocationSearchError("No matching place found. Try another name or enter coordinates below.");
        return;
      }

      handleLocationChange(location.lat, location.lon);
      setLocationPromptOpen(false);
    } catch (searchError) {
      setLocationSearchError(
        searchError instanceof Error ? searchError.message : "Place search is temporarily unavailable."
      );
    } finally {
      setLocationSearching(false);
    }
  };

  const applyInitialCoordinates = () => {
    const parsedLat = Number(inputLat.trim());
    const parsedLon = Number(inputLon.trim());
    if (
      inputLat.trim() && inputLon.trim() &&
      Number.isFinite(parsedLat) && parsedLat >= -90 && parsedLat <= 90 &&
      Number.isFinite(parsedLon) && parsedLon >= -180 && parsedLon <= 180
    ) {
      setLocationSearchError(null);
      handleLocationChange(parsedLat, parsedLon);
      setLocationPromptOpen(false);
    } else {
      setLocationSearchError("Enter a latitude from -90 to 90 and a longitude from -180 to 180.");
    }
  };

  const skipInitialLocationSetup = () => {
    try {
      window.localStorage.setItem(SKIPPED_LOCATION_SETUP_KEY, "true");
      setLocationStorageWarning(null);
    } catch {
      setLocationStorageWarning("This browser could not save your setup preference. You can still use the dashboard.");
    }
    setLocationPromptOpen(false);
  };


  useEffect(() => {
    if (locationPromptOpen) return;
    loadData();
  }, [locationPromptOpen, lat, lon, startYear, endYear]);

  // Fetch satellite data whenever the visible place or selected years change.
  // Cleanup cancels the old request, so a slow old response cannot replace new data.
  useEffect(() => {
    if (activeTab !== "vegetation") return;

    const controller = new AbortController();
    const requestId = ++latestVegRequestIdRef.current;
    const requestLat = lat;
    const requestLon = lon;
    const requestStartYear = startYear;
    const requestEndYear = endYear;
    let stillCurrent = true;

    vegAbortControllerRef.current = controller;
    setVegLoading(true);
    setVegProgress("Connecting to the satellite picture service…");
    setVegProgressPct(null);
    setVegError(null);
    setVegCancelled(false);
    setVegData(null);
    setVegDataLocation(null);

    fetchVegetationAnalysis(
      requestLat, requestLon, requestStartYear, requestEndYear,
      controller.signal,
      vegAllowFallback,
      (event) => {
        if (!stillCurrent || requestId !== latestVegRequestIdRef.current) return;
        const progress = farmerFriendlyVegetationProgress(event);
        setVegProgress(progress.message);
        setVegProgressPct(progress.percent);
      },
    )
      .then((result) => {
        if (!stillCurrent || requestId !== latestVegRequestIdRef.current) return;
        setVegData(result);
        setVegDataLocation({ lat: requestLat, lon: requestLon, startYear: requestStartYear, endYear: requestEndYear });
      })
      .catch((err: any) => {
        if (!stillCurrent || requestId !== latestVegRequestIdRef.current || err?.name === "AbortError") return;
        setVegError(err?.message || "Plant-growth data could not be loaded.");
      })
      .finally(() => {
        if (stillCurrent && requestId === latestVegRequestIdRef.current) {
          setVegLoading(false);
          setVegProgress("");
          setVegProgressPct(null);
          if (vegAbortControllerRef.current === controller) vegAbortControllerRef.current = null;
        }
      });

    return () => {
      stillCurrent = false;
      controller.abort();
      if (vegAbortControllerRef.current === controller) vegAbortControllerRef.current = null;
    };
  }, [activeTab, lat, lon, startYear, endYear, vegRetryCount, vegAllowFallback]);

  const vegDataMatchesCurrentSelection = Boolean(
    vegData && vegDataLocation &&
    vegDataLocation.lat === lat && vegDataLocation.lon === lon &&
    vegDataLocation.startYear === startYear && vegDataLocation.endYear === endYear
  );

  return (
    <div className="farmer-ui dashboard-dark min-h-screen flex flex-col font-sans">
      {/* Header */}
      <header className="bg-[#101113] text-white shadow-md border-b-4 border-[#858991]">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
          <div className="dashboard-brand flex items-center gap-3.5">
            <img
              src="../logo.webp"
              alt="Vasundhara logo"
              className="w-12 h-12 rounded-full object-contain bg-white p-0.5 shadow-md border-2 border-[#747780]"
            />
            <div className="dashboard-brand-copy">
              <div className="flex items-center gap-2.5 flex-wrap">
                <h1 className="text-2xl font-black text-white">Vasundhara</h1>
                <span className="dashboard-brand-badge bg-[#315d43] text-white text-xs font-semibold px-2 py-0.5 rounded uppercase tracking-wider">
                  Simple farm, weather and crop guidance
                </span>
              </div>
              <p className="text-sm text-white mt-1">
                Choose your farm place to see rain, heat, plant growth and crop choices.
              </p>
            </div>
          </div>
          <div className="dashboard-header-tools">
            <a
              href={window.location.hostname === "dashboard.vasundhara.earth" ? "https://vasundhara.earth/" : "../"}
              className="dashboard-home-link"
              aria-label="Return to the Vasundhara home page"
            >
              ← Home
            </a>
            <div className="dashboard-location-meta">
              <div>Climate comparison period: <span className="font-semibold text-white">1991–2020</span></div>
              <div>Selected place: <span className="text-[#d4d5d9] font-mono">{lat.toFixed(4)}°, {lon.toFixed(4)}°</span></div>
            </div>
          </div>
        </div>
      </header>

      {locationStorageWarning && (
        <div role="status" className="dashboard-location-storage-warning">
          {locationStorageWarning}
        </div>
      )}

      {/* Control Bar */}
      <section className="dashboard-controls border-b shadow-xs">
        <div className="max-w-7xl mx-auto px-4 py-3 sm:px-6 lg:px-8">
          <div className="dashboard-controls-layout">
            {/* Presets */}
            <div className="dashboard-preset-row">
              <span className="dashboard-row-label">Choose a main place:</span>
              {PRESETS.map((p) => (
                <button
                  key={p.name}
                  type="button"
                  aria-pressed={Math.abs(lat - p.lat) < 0.001 && Math.abs(lon - p.lon) < 0.001}
                  onClick={() => handleLocationChange(p.lat, p.lon)}
                  className={`text-xs px-2.5 py-1 rounded transition-colors font-medium border ${
                    Math.abs(lat - p.lat) < 0.001 && Math.abs(lon - p.lon) < 0.001
                      ? "bg-[#6a6d75] text-white border-[#e7e8eb]"
                      : "bg-[#232428] text-[#6a6d75] hover:bg-[#303136] border-[#505158]"
                  }`}
                >
                  {p.name}
                </button>
              ))}
            </div>

            {/* Form controls & Map Toggle */}
            <div className="dashboard-coordinate-row">
              <div className="flex items-center gap-1 text-xs">
                <label htmlFor="latitude-input" className="font-semibold text-gray-800">Latitude:</label>
                <input
                  id="latitude-input"
                  type="text"
                  value={inputLat}
                  onChange={(e) => setInputLat(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") applyCoordinates();
                  }}
                  onBlur={applyCoordinates}
                  className="w-20 px-2 py-1 text-xs border border-gray-300 rounded bg-[#202125] focus:outline-[#6a6d75]"
                  placeholder="25.5941"
                />
              </div>
              <div className="flex items-center gap-1 text-xs">
                <label htmlFor="longitude-input" className="font-semibold text-gray-800">Longitude:</label>
                <input
                  id="longitude-input"
                  type="text"
                  value={inputLon}
                  onChange={(e) => setInputLon(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") applyCoordinates();
                  }}
                  onBlur={applyCoordinates}
                  className="w-20 px-2 py-1 text-xs border border-gray-300 rounded bg-[#202125] focus:outline-[#6a6d75]"
                  placeholder="85.1376"
                />
              </div>
              <button
                type="button"
                onClick={applyCoordinates}
                title="Apply entered coordinates"
                className="bg-[#6a6d75] hover:bg-[#e7e8eb] text-white text-xs font-semibold px-2.5 py-1 rounded transition-colors shadow-xs cursor-pointer"
              >
                Go
              </button>
              <div className="flex items-center gap-1.5 text-xs">
                <label htmlFor="year-start" className="font-semibold text-gray-800">Years:</label>
                <select
                  id="year-start"
                  aria-label="First year to show"
                  value={startYear}
                  onChange={(e) => { setStartYear(parseInt(e.target.value)); setVegData(null); }}
                  className="px-2 py-1 text-xs border border-gray-300 rounded bg-[#202125]"
                >
                  {[2000, 2005, 2010, 2015, 2018, 2020].map((y) => (
                    <option key={y} value={y}>{y}</option>
                  ))}
                </select>
                <span>to</span>
                <select
                  id="year-end"
                  aria-label="Last year to show"
                  value={endYear}
                  onChange={(e) => { setEndYear(parseInt(e.target.value)); setVegData(null); }}
                  className="px-2 py-1 text-xs border border-gray-300 rounded bg-[#202125]"
                >
                  {[2020, 2022, 2023, 2024, 2025].map((y) => (
                    <option key={y} value={y}>{y}</option>
                  ))}
                </select>
              </div>

              <button
                onClick={() => handleLocationChange(lat, lon)}
                className="bg-[#6a6d75] hover:bg-[#e7e8eb] text-white text-xs font-semibold px-3 py-1 rounded transition-colors shadow-xs"
              >
                Apply
              </button>

              <button
                onClick={() => setShowMap(!showMap)}
                className={`text-xs font-semibold px-3 py-1 rounded transition-colors border ${
                  showMap
                    ? "bg-[#e7e8eb] text-white border-[#e7e8eb]"
                    : "bg-white text-[#e7e8eb] border-[#6a6d75]"
                }`}
              >
                {showMap ? "Hide Map" : "Show Map"}
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Map Picker Section */}
      {showMap && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4 w-full">
          <MapPicker
            lat={lat}
            lon={lon}
            onLocationChange={handleLocationChange}
            startYear={startYear}
            endYear={endYear}
          />
        </section>
      )}

      {/* Simple steps for first-time users */}
      <section className="dashboard-howto max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4 w-full" aria-label="How to use this tool">
        <div className="bg-white border border-[#505158] rounded-lg p-4">
          <h2 className="text-xl font-bold text-[#e7e8eb]">How to use this tool</h2>
          <ol className="mt-2 grid grid-cols-1 md:grid-cols-3 gap-3 text-base text-gray-800">
            <li><strong>1.</strong> Choose your village or farm place on the map.</li>
            <li><strong>2.</strong> Add soil and water details if you know them.</li>
            <li><strong>3.</strong> Read the crop suggestions and warnings before deciding.</li>
          </ol>
        </div>
      </section>

      {/* Tabs */}
      <nav className="dashboard-tabs max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4 w-full">
        <div role="tablist" aria-label="Farm information" className="flex border-b border-[#505158] gap-2 overflow-x-auto">
          {[
            { id: "rotation", label: "Crop choices" },
            { id: "climate", label: "Temperature" },
            { id: "rainfall", label: "Rain and seasons" },
            { id: "trends", label: "Changes over time" },
            { id: "vegetation", label: "Plant growth history" },
            { id: "quality", label: "ℹ️ About these results" },
          ].map((tab) => (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={activeTab === tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`py-3 px-4 font-semibold text-sm transition-colors rounded-t-md whitespace-nowrap border-t border-x ${
                activeTab === tab.id
                  ? "bg-white text-[#e7e8eb] border-[#505158] border-b-transparent shadow-xs"
                  : "bg-[#303136] text-[#d0d1d5] hover:bg-[#4a4c53] border-transparent"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </nav>

      {/* Main Content Area */}
      <main className="dashboard-content max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex-1 w-full">
        {/* Error Notification */}
        {error && (
          <div className="bg-zinc-50 border-l-4 border-zinc-500 p-4 mb-6 rounded-r shadow-xs">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="text-zinc-600 font-bold">Error:</span>
                <span className="text-sm text-zinc-700">{error}</span>
              </div>
              <button
                onClick={() => loadData()}
                className="text-xs bg-zinc-600 hover:bg-zinc-700 text-white font-medium px-3 py-1 rounded"
              >
                Retry
              </button>
            </div>
          </div>
        )}

        {/* Global Loading Spinner for analytical data */}
        {loading && activeTab !== "rotation" && (
          <div className="flex flex-col items-center justify-center py-20 bg-white rounded-lg shadow-xs border border-[#44464d]">
            <div className="w-10 h-10 border-4 border-[#6a6d75] border-t-transparent rounded-full animate-spin"></div>
            <p className="mt-4 text-sm text-[#8b8d94] font-medium">Fetching NASA POWER climate metrics...</p>
          </div>
        )}

        {/* TAB 0: CROP ROTATION LAB */}
        {activeTab === "rotation" && (
          <RotationLab
            lat={lat}
            lon={lon}
            baselineRainfall={climateData?.baseline?.rainfall_mean_mm}
            climateData={climateData}
          />
        )}

        {(!loading || activeTab === "vegetation") && (
          <>
            {/* TAB 1: CLIMATE & TEMPERATURE */}
            {activeTab === "climate" && (
              !climateData ? null : !climateData.available ? (
                <div className="bg-zinc-50 border-l-4 border-zinc-500 p-5 rounded-r shadow-xs space-y-2">
                  <div className="text-xs font-bold text-zinc-900 uppercase">Weather information is not available for this place</div>
                  <div className="text-sm text-zinc-800">{climateData.reason || "Data could not be retrieved from NASA POWER servers."}</div>
                  <p className="text-xs text-gray-600">
                    Vasundhara adheres strictly to scientific data integrity and will never invent or fabricate substitute observations.
                  </p>
                  <button onClick={() => loadData()} className="mt-2 bg-[#e7e8eb] text-white text-xs px-3 py-1.5 rounded cursor-pointer font-semibold">
                    Retry NASA Query
                  </button>
                </div>
              ) : (
              <div className="space-y-6">
                {/* Metric Summary Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                  <div className="dashboard-metric-card metric-sage bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Usual temperature (1991–2020)</div>
                    <div className="text-2xl font-bold text-[#e7e8eb] mt-1">
                      {climateData.baseline?.temperature_mean_c != null ? `${climateData.baseline.temperature_mean_c} °C` : "N/A"}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">Average yearly temperature in the reference period</div>
                  </div>

                  <div className="dashboard-metric-card metric-amber bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Average temperature in selected years</div>
                    <div className="text-2xl font-bold text-[#6a6d75] mt-1">
                      {climateData.annual && climateData.annual.length > 0
                        ? `${(
                            climateData.annual.filter(a => a.t2m_complete && a.t2m_mean_c !== null).reduce((acc, curr) => acc + (curr.t2m_mean_c || 0), 0) /
                            (climateData.annual.filter(a => a.t2m_complete && a.t2m_mean_c !== null).length || 1)
                          ).toFixed(2)} °C`
                        : "N/A"}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">{startYear}–{endYear} observed mean</div>
                  </div>

                  <div className="dashboard-metric-card metric-coral bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Highest recorded temperature</div>
                    <div className="text-2xl font-bold text-zinc-700 mt-1">
                      {climateData.annual && climateData.annual.length > 0
                        ? `${Math.max(...climateData.annual.map(a => a.t2m_max_c || -999).filter(v => v > -900)).toFixed(1)} °C`
                        : "N/A"}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">Highest daily air temperature in these years</div>
                  </div>

                  <div className="dashboard-metric-card metric-blue bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Lowest recorded temperature</div>
                    <div className="text-2xl font-bold text-zinc-700 mt-1">
                      {climateData.annual && climateData.annual.length > 0
                        ? `${Math.min(...climateData.annual.map(a => a.t2m_min_c || 999).filter(v => v < 900)).toFixed(1)} °C`
                        : "N/A"}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">Lowest daily air temperature in these years</div>
                  </div>
                </div>

                {/* Annual Temperature Trajectory Chart */}
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <div className="flex justify-between items-center mb-4">
                    <div>
                      <h3 className="font-bold text-[#e7e8eb] text-sm">Annual Mean Temperature Trajectory & Extremes</h3>
                      <p className="text-xs text-gray-500">Daily readings are grouped by year. Missing readings are left blank.</p>
                    </div>
                    <span className="text-xs bg-[#232428] px-2 py-1 rounded text-[#6a6d75] font-medium border border-[#44464d]">
                      Units: °C
                    </span>
                  </div>
                  <div className="h-72 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                      <LineChart data={climateData.annual || []}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#2b2c31" />
                        <XAxis dataKey="year" tick={{ fontSize: 16 }} />
                        <YAxis domain={["auto", "auto"]} unit="°C" tick={{ fontSize: 16 }} />
                        <Tooltip
                          formatter={(val: any) => [val !== null ? `${val} °C` : "Incomplete (null)", ""]}
                          labelFormatter={(label) => `Year: ${label}`}
                        />
                        <Legend wrapperStyle={{ fontSize: 14 }} />
                        {climateData.baseline?.temperature_mean_c && (
                          <ReferenceLine
                            y={climateData.baseline.temperature_mean_c}
                            stroke="#aeb1b8"
                            strokeDasharray="4 4"
                            label={{ value: `Baseline: ${climateData.baseline.temperature_mean_c} °C`, fontSize: 14, fill: "#d0d1d5" }}
                          />
                        )}
                        <Line type="monotone" dataKey="t2m_max_c" stroke="#E3A36F" name="Annual Max (°C)" dot={{ r: 2 }} connectNulls={false} />
                        <Line type="monotone" dataKey="t2m_mean_c" stroke="#E7CC7A" strokeWidth={2} name="Annual Mean (°C)" dot={{ r: 3 }} connectNulls={false} />
                        <Line type="monotone" dataKey="t2m_min_c" stroke="#82B6D1" name="Annual Min (°C)" dot={{ r: 2 }} connectNulls={false} />
                      </LineChart>
                    </ResponsiveContainer>
                  </div>
                </div>

                {/* Monthly Climatology Chart */}
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <div className="flex justify-between items-center mb-4">
                    <div>
                      <h3 className="font-bold text-[#e7e8eb] text-sm">Monthly Climatological Profile (12-Month Cycle)</h3>
                      <p className="text-xs text-gray-500">Average temperature for each month</p>
                    </div>
                    <span className="text-xs bg-[#232428] px-2 py-1 rounded text-[#6a6d75] font-medium border border-[#44464d]">
                      Units: °C
                    </span>
                  </div>
                  <div className="h-64 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart
                        data={(climateData.monthly_climatology || []).map((m) => ({
                          ...m,
                          monthName: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][m.month - 1],
                        }))}
                      >
                        <CartesianGrid strokeDasharray="3 3" stroke="#2b2c31" />
                        <XAxis dataKey="monthName" tick={{ fontSize: 16 }} />
                        <YAxis domain={[0, "auto"]} unit="°C" tick={{ fontSize: 16 }} />
                        <Tooltip formatter={(val: any) => [`${val} °C`, "Mean Temp"]} />
                        <Bar dataKey="t2m_mean_c" fill="#D9AE69" radius={[4, 4, 0, 0]} name="Monthly Mean Temp (°C)" />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                </div>
              </div>
              )
            )}

            {/* TAB 2: RAINFALL & SEASONS */}
            {activeTab === "rainfall" && (
              !climateData ? null : !climateData.available ? (
                <div className="bg-zinc-50 border-l-4 border-zinc-500 p-5 rounded-r shadow-xs space-y-2">
                  <div className="text-xs font-bold text-zinc-900 uppercase">Rainfall information is not available for this place</div>
                  <div className="text-sm text-zinc-800">{climateData.reason || "Precipitation observations could not be retrieved from NASA POWER."}</div>
                  <button onClick={() => loadData()} className="mt-2 bg-[#e7e8eb] text-white text-xs px-3 py-1.5 rounded cursor-pointer font-semibold">
                    Retry NASA Query
                  </button>
                </div>
              ) : (
              <div className="space-y-6">
                {/* Metric Summary Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                  <div className="dashboard-metric-card metric-blue bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Usual yearly rainfall</div>
                    <div className="text-2xl font-bold text-[#e7e8eb] mt-1">
                      {climateData.baseline?.rainfall_mean_mm != null ? `${climateData.baseline.rainfall_mean_mm} mm` : "N/A"}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">Average rainfall from 1991 to 2020</div>
                  </div>

                  <div className="dashboard-metric-card metric-teal bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Rain in the rainy season (June–October)</div>
                    <div className="text-2xl font-bold text-zinc-700 mt-1">
                      {(() => {
                        const kharif = (climateData.seasonal_period_means || []).find(s => s.season === "kharif");
                        const val = kharif?.mean_rainfall_mm ?? kharif?.rainfall_mm;
                        if (val != null) {
                          const total = climateData.baseline?.rainfall_mean_mm;
                          const pct = total ? ` (${Math.round((val / total) * 100)}%)` : "";
                          return `${val} mm${pct}`;
                        }
                        // Fallback: calculate from seasons array if present
                        const kSeasons = (climateData.seasons || []).filter(s => s.season === "kharif" && s.rainfall_mm != null);
                        if (kSeasons.length > 0) {
                          const avg = Math.round((kSeasons.reduce((acc, s) => acc + (s.rainfall_mm || 0), 0) / kSeasons.length) * 10) / 10;
                          return `${avg} mm`;
                        }
                        return "N/A";
                      })()}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">June–October seasonal rainfall mean</div>
                  </div>

                  <div className="dashboard-metric-card metric-sage bg-white p-4 rounded-lg border border-[#44464d] shadow-xs">
                    <div className="text-xs font-semibold text-gray-500 uppercase">Rain in the cool season (November–March)</div>
                    <div className="text-2xl font-bold text-zinc-700 mt-1">
                      {(() => {
                        const rabi = (climateData.seasonal_period_means || []).find(s => s.season === "rabi");
                        const val = rabi?.mean_rainfall_mm ?? rabi?.rainfall_mm;
                        if (val != null) {
                          const total = climateData.baseline?.rainfall_mean_mm;
                          const pct = total ? ` (${Math.round((val / total) * 100)}%)` : "";
                          return `${val} mm${pct}`;
                        }
                        // Fallback: calculate from seasons array if present
                        const rSeasons = (climateData.seasons || []).filter(s => s.season === "rabi" && s.rainfall_mm != null);
                        if (rSeasons.length > 0) {
                          const avg = Math.round((rSeasons.reduce((acc, s) => acc + (s.rainfall_mm || 0), 0) / rSeasons.length) * 10) / 10;
                          return `${avg} mm`;
                        }
                        return "N/A";
                      })()}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">Nov–Mar winter crop season mean</div>
                  </div>
                </div>

                {/* Annual Precipitation Bar Chart */}
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <div className="flex justify-between items-center mb-4">
                    <div>
                      <h3 className="font-bold text-[#e7e8eb] text-sm">Annual Total Precipitation & Baseline Normal</h3>
                      <p className="text-xs text-gray-500">Daily rainfall added up for each year</p>
                    </div>
                    <span className="text-xs bg-[#232428] px-2 py-1 rounded text-[#6a6d75] font-medium border border-[#44464d]">
                      Units: mm/year
                    </span>
                  </div>
                  <div className="h-72 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart data={climateData.annual || []}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#2b2c31" />
                        <XAxis dataKey="year" tick={{ fontSize: 16 }} />
                        <YAxis unit="mm" tick={{ fontSize: 16 }} />
                        <Tooltip
                          formatter={(val: any, _name: any, item: any) => {
                            if (!item.payload.rainfall_complete) {
                              return [`Incomplete year (${item.payload.observed_days}/${item.payload.expected_days} days)`, "Rainfall Total"];
                            }
                            return [`${val} mm`, "Annual Rainfall"];
                          }}
                        />
                        {climateData.baseline?.rainfall_mean_mm && (
                          <ReferenceLine
                            y={climateData.baseline.rainfall_mean_mm}
                            stroke="#aeb1b8"
                            strokeWidth={2}
                            strokeDasharray="4 4"
                            label={{ value: `Baseline: ${climateData.baseline.rainfall_mean_mm} mm`, fontSize: 14, fill: "#aeb1b8" }}
                          />
                        )}
                        <Bar
                          dataKey="rainfall_mm"
                          fill="#78B8D1"
                          radius={[4, 4, 0, 0]}
                          name="Annual Rainfall (mm)"
                        />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                  <div className="mt-2 text-xs text-gray-500">
                    * Incomplete years are withheld and not compared directly with full calendar years to prevent misleading drought interpretations.
                  </div>
                </div>

                {/* Seasonal Breakdown Table */}
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <h3 className="font-bold text-[#e7e8eb] text-sm mb-3">Seasonal Rainfall Distribution (Non-Overlapping Windows)</h3>
                  <div className="overflow-x-auto">
                    <table className="min-w-full text-xs text-left">
                      <thead className="bg-[#232428] border-b border-[#44464d] font-semibold text-[#e7e8eb]">
                        <tr>
                          <th className="py-2 px-3">Year</th>
                          <th className="py-2 px-3">Season</th>
                          <th className="py-2 px-3">Window</th>
                          <th className="py-2 px-3">Rainfall</th>
                          <th className="py-2 px-3">Anomaly</th>
                          <th className="py-2 px-3">Completeness</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-gray-100">
                        {(climateData.seasons || []).slice(-15).map((s, idx) => (
                          <tr key={idx} className="hover:bg-[#202125]">
                            <td className="py-2 px-3 font-medium">{s.year}</td>
                            <td className="py-2 px-3 capitalize font-semibold text-[#6a6d75]">{s.season}</td>
                            <td className="py-2 px-3 text-gray-500">{s.label}</td>
                            <td className="py-2 px-3 font-semibold">{s.rainfall_mm !== null ? `${s.rainfall_mm} mm` : "Incomplete"}</td>
                            <td className="py-2 px-3">
                              {s.rainfall_anomaly_mm !== null && s.rainfall_anomaly_mm !== undefined ? (
                                <span className={s.rainfall_anomaly_mm >= 0 ? "text-zinc-700 font-medium" : "text-zinc-700 font-medium"}>
                                  {s.rainfall_anomaly_mm > 0 ? `+${s.rainfall_anomaly_mm}` : s.rainfall_anomaly_mm} mm
                                </span>
                              ) : "—"}
                            </td>
                            <td className="py-2 px-3">
                              {s.complete ? (
                                <span className="bg-zinc-100 text-zinc-800 text-xs px-2 py-0.5 rounded">100% complete</span>
                              ) : (
                                <span className="bg-zinc-100 text-zinc-800 text-xs px-2 py-0.5 rounded">
                                  {s.expected_days - s.missing_days}/{s.expected_days} days
                                </span>
                              )}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              )
            )}

            {/* TAB 3: TREND ANALYSIS (MANN-KENDALL & SEN'S SLOPE) */}
            {activeTab === "trends" && (
              !trendData ? null : !trendData.available ? (
                <div className="bg-zinc-50 border-l-4 border-zinc-500 p-5 rounded-r shadow-xs space-y-2">
                  <div className="text-xs font-bold text-zinc-900 uppercase">Long-term weather changes are not available</div>
                  <div className="text-sm text-zinc-800">{trendData.reason || "Historical series is incomplete or unavailable for statistical trend detection."}</div>
                  <button onClick={() => loadData()} className="mt-2 bg-[#e7e8eb] text-white text-xs px-3 py-1.5 rounded cursor-pointer font-semibold">
                    Retry NASA Query
                  </button>
                </div>
              ) : (
              <div className="space-y-6">
                {/* Non-Forecast Disclaimer Banner */}
                <div className="bg-[#27282d] border-l-4 border-zinc-500 p-4 rounded-r shadow-xs">
                  <div className="text-xs font-bold text-zinc-900 uppercase">Important note about these results</div>
                  <div className="text-xs text-zinc-800 mt-1 font-medium">{trendData.disclaimer}</div>
                </div>

                {/* Trend Table */}
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <h3 className="font-bold text-[#e7e8eb] text-sm mb-1">Non-Parametric Trend Detection & Rates</h3>
                  <p className="text-xs text-gray-500 mb-4">
                    Mann-Kendall test with Hamed–Rao serial correlation adjustment (annual) and Hipel seasonal adjustment (monthly).
                  </p>
                  <div className="overflow-x-auto">
                    <table className="min-w-full text-xs text-left">
                      <thead className="bg-[#232428] border-b border-[#44464d] font-semibold text-[#e7e8eb]">
                        <tr>
                          <th className="py-2.5 px-3">Variable</th>
                          <th className="py-2.5 px-3">Method</th>
                          <th className="py-2.5 px-3">Direction</th>
                          <th className="py-2.5 px-3">Sen's Slope Rate</th>
                          <th className="py-2.5 px-3">Mann-Kendall Tau</th>
                          <th className="py-2.5 px-3">p-value</th>
                          <th className="py-2.5 px-3">Significance (α=0.05)</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-gray-100">
                        {(trendData.series || []).map((t) => (
                          <tr key={t.id} className="hover:bg-[#202125]">
                            <td className="py-2.5 px-3 font-semibold text-[#e7e8eb]">{t.label}</td>
                            <td className="py-2.5 px-3 text-gray-500">{t.method_label.split(" (")[0]}</td>
                            <td className="py-2.5 px-3">
                              {t.direction === "increasing" && (
                                <span className="bg-zinc-100 text-zinc-800 px-2 py-0.5 rounded font-semibold">Increasing ▲</span>
                              )}
                              {t.direction === "decreasing" && (
                                <span className="bg-zinc-100 text-zinc-800 px-2 py-0.5 rounded font-semibold">Decreasing ▼</span>
                              )}
                              {t.direction === "no statistically significant trend" && (
                                <span className="bg-gray-100 text-gray-700 px-2 py-0.5 rounded">No trend</span>
                              )}
                              {t.direction === null && (
                                <span className="text-gray-400">Not computed ({t.error || "insufficient data"})</span>
                              )}
                            </td>
                            <td className="py-2.5 px-3 font-mono font-bold">
                              {t.slope !== null ? `${t.slope > 0 ? "+" : ""}${t.slope} ${t.slope_units}` : "—"}
                            </td>
                            <td className="py-2.5 px-3 font-mono">{t.tau !== null ? t.tau : "—"}</td>
                            <td className="py-2.5 px-3 font-mono">
                              {t.p_value !== null ? t.p_value.toFixed(4) : "—"}
                            </td>
                            <td className="py-2.5 px-3">
                              {t.significant ? (
                                <span className="bg-zinc-100 text-zinc-800 font-semibold px-2 py-0.5 rounded">Statistically Significant</span>
                              ) : (
                                <span className="text-gray-500">Not Significant</span>
                              )}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>

                {/* Limitations and Methodology Notes */}
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <h4 className="font-bold text-xs text-[#e7e8eb] uppercase mb-2">What these results cannot tell us</h4>
                  <ul className="list-disc list-inside text-xs text-gray-600 space-y-1">
                    {(trendData.limitations || []).map((l, idx) => (
                      <li key={idx}>{l}</li>
                    ))}
                  </ul>
                </div>
              </div>
              )
            )}

            {/* TAB 4: VEGETATION (MODIS NDVI) */}
            {activeTab === "vegetation" && (
              <div className="space-y-6">
                <section className="rounded-lg border border-[#505158] bg-white p-5">
                  <h2 className="text-xl font-bold text-[#e7e8eb]">Plant growth pictures for this place</h2>
                  <p className="mt-2 text-base text-gray-900">These pictures help show whether plants in the surrounding area looked greener or less green over time. They do not measure one farm or tell us how much crop you will harvest.</p>
                  <p className="mt-1 text-sm text-gray-700">Place: {lat.toFixed(4)}° latitude, {lon.toFixed(4)}° longitude · Years: {startYear} to {endYear}</p>
                </section>
                {vegLoading && (
                  <div role="status" aria-live="polite" aria-busy="true" className="flex flex-col items-center justify-center py-16 px-4 bg-white rounded-lg shadow-xs border border-[#44464d] text-center">
                    <div className="w-10 h-10 border-4 border-[#6a6d75] border-t-transparent rounded-full animate-spin"></div>
                    <p className="mt-4 text-lg text-[#e7e8eb] font-bold">
                      Getting plant-growth pictures for this place
                    </p>
                    <p className="text-base text-gray-800 mt-2 max-w-xl">
                      {vegProgress || `Looking at pictures from ${startYear} to ${endYear}. A new place may take longer the first time.`}
                    </p>
                    {vegProgressPct !== null && (
                      <div className="w-full max-w-md mt-3" aria-label={`${vegProgressPct}% complete`}>
                        <div className="h-3 rounded-full bg-[#44464d] overflow-hidden">
                          <div className="h-full rounded-full bg-[#759A64] transition-all" style={{ width: `${vegProgressPct}%` }} />
                        </div>
                        <p className="mt-1 text-sm font-semibold text-[#e7e8eb]">{vegProgressPct}% done</p>
                      </div>
                    )}
                    <button
                      onClick={cancelVegetationFetch}
                      className="mt-4 text-xs font-semibold text-gray-600 hover:text-zinc-700 bg-gray-100 hover:bg-gray-200 px-3 py-1.5 rounded transition-colors border border-gray-300 cursor-pointer"
                    >
                      Stop loading
                    </button>
                  </div>
                )}

                {vegError && (
                  <div role="alert" className="bg-zinc-50 border-l-4 border-zinc-700 p-5 rounded-r shadow-xs">
                    <div className="flex items-center justify-between gap-4 flex-wrap">
                      <span className="text-base text-zinc-950 font-semibold">{vegError}</span>
                      <button
                        onClick={() => retryVegetation(true)}
                        className="text-xs bg-zinc-600 hover:bg-zinc-700 text-white font-medium px-3 py-1 rounded"
                      >
                        Try again
                      </button>
                    </div>
                  </div>
                )}

                {!vegLoading && vegCancelled && !vegError && !vegDataMatchesCurrentSelection && (
                  <div role="status" className="bg-white border border-[#505158] rounded-lg p-5 space-y-3">
                    <h3 className="text-lg font-bold text-[#e7e8eb]">Loading was stopped</h3>
                    <p className="text-base text-gray-800">No new plant-growth pictures were loaded. You can start again for this place.</p>
                    <button type="button" onClick={() => retryVegetation(true)} className="min-h-11 rounded-md bg-[#e7e8eb] px-5 py-3 text-base font-semibold text-white">Load plant-growth pictures</button>
                  </div>
                )}
                {!vegLoading && !vegError && !vegCancelled && !vegDataMatchesCurrentSelection && (
                  <div role="status" className="bg-white border border-[#505158] rounded-lg p-5 space-y-3">
                    <h3 className="text-lg font-bold text-[#e7e8eb]">Plant-growth information is not loaded yet</h3>
                    <p className="text-base text-gray-800">Choose a place on the map or press the button to load satellite information for the selected place.</p>
                    <button type="button" onClick={() => retryVegetation(true)} className="min-h-11 rounded-md bg-[#e7e8eb] px-5 py-3 text-base font-semibold text-white">Load plant-growth pictures</button>
                  </div>
                )}
                {!vegLoading && vegDataMatchesCurrentSelection && vegData && (
                  !vegData.available ? (
                    <div className="bg-zinc-50 border-l-4 border-zinc-500 p-5 rounded-r shadow-xs space-y-3">
                      <div className="text-xs font-bold text-zinc-900 uppercase">Plant-growth pictures are not available for this place</div>
                      <div className="text-sm text-zinc-800">{vegData.reason || "MODIS composites could not be retrieved from ORNL DAAC."}</div>
                      <p className="text-xs text-gray-600">
                        The satellite service did not send data. You can try again, or view an example estimate. The example is not a real satellite reading and must not be used to judge a field.
                      </p>
                      <div className="flex items-center gap-2 pt-1 flex-wrap">
                        <button
                          onClick={() => retryVegetation(true)}
                          className="bg-[#6a6d75] hover:bg-[#e7e8eb] text-white text-xs px-3.5 py-2 rounded font-semibold cursor-pointer shadow-xs transition-colors"
                        >
                          Show example estimate (not satellite data)
                        </button>
                        <button
                          onClick={() => retryVegetation(false)}
                          className="bg-white hover:bg-gray-50 text-gray-700 border border-gray-300 text-xs px-3 py-2 rounded font-medium cursor-pointer transition-colors"
                        >
                          Try satellite data again
                        </button>
                      </div>
                    </div>
                  ) : (
                  <>
                    {vegData.is_fallback && (
                      <div className="bg-zinc-50 border-l-4 border-zinc-600 p-4 rounded-r shadow-xs mb-4 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                        <div>
                          <div className="text-xs font-bold text-zinc-900 uppercase">
                            EXAMPLE — Estimate only — not a real satellite reading
                          </div>
                          <div className="text-xs text-zinc-800 mt-0.5">
                            {vegData.fallback_notice || "Live satellite data could not be reached. This chart is an example estimate, not a measurement of your farm."}
                          </div>
                        </div>
                        <button
                          onClick={() => retryVegetation(false)}
                          className="text-xs bg-zinc-700 hover:bg-zinc-800 text-white font-semibold px-3 py-1.5 rounded transition-colors whitespace-nowrap cursor-pointer shadow-xs"
                        >
                          Try real satellite data
                        </button>
                      </div>
                    )}
                    {/* Latest Observation Card */}
                    {vegData.latest && (
                      <div className="bg-white p-4 rounded-lg border border-[#44464d] shadow-xs flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                        <div>
                          <div className="text-lg font-bold text-gray-900">Most recent plant green score</div>
                          <div className="text-2xl font-bold text-[#e7e8eb] mt-1">
                            {vegData.latest.ndvi !== null ? `${vegData.latest.ndvi}` : "No clear picture"}
                            <span className="text-sm text-gray-700 ml-2 font-normal">Date: {vegData.latest.date}</span>
                          </div>
                          <div className="text-sm text-gray-700 mt-2">{vegData.latest.note}</div>
                        </div>
                        <div className="text-right text-xs text-gray-500 bg-[#232428] p-3 rounded border border-[#44464d]">
                          <div>Clear pictures used: <span className="font-bold text-[#e7e8eb]">{vegData.observation_count}</span></div>
                          <div>Cloudy or unclear pictures skipped: <span className="font-bold text-zinc-800">{vegData.missing_count}</span></div>
                          
                        </div>
                      </div>
                    )}

                    {(vegData.observation_count ?? 0) === 0 && (
                      <div role="status" className="rounded-lg border border-zinc-400 bg-zinc-50 p-5 text-base text-zinc-950">
                        <strong>No clear satellite pictures were found for these years.</strong>
                        Pictures covered by clouds or other interference are left out. Try another place or a different set of years.
                      </div>
                    )}

                    {/* Plant greenness over time */}
                    <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                      <div className="flex justify-between items-center mb-4">
                        <div>
                          <h3 className="font-bold text-[#e7e8eb] text-lg">How green the land looked over time</h3>
                          <p className="text-base text-gray-700">A new picture is made about every 16 days. Cloudy pictures may be missing.</p>
                        </div>
                        <span className="text-xs bg-[#232428] px-2 py-1 rounded text-[#6a6d75] font-medium border border-[#44464d]">
                          Plant green score
                        </span>
                      </div>
                      <div className="h-72 w-full">
                        <ResponsiveContainer width="100%" height="100%">
                          <LineChart accessibilityLayer data={vegData.series || []}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#2b2c31" />
                            <XAxis dataKey="date" tick={{ fontSize: 16 }} minTickGap={48} />
                            <YAxis domain={[0, 1]} tick={{ fontSize: 16 }} />
                            <Tooltip
                              formatter={(val: any) => [val !== null ? val.toFixed(2) : "No clear picture", "Plant green score"]}
                              labelFormatter={(label) => `Date: ${label}`}
                            />
                            <ReferenceLine y={0.2} stroke="#aeb1b8" strokeDasharray="2 2" label={{ value: "Low green cover guide (0.2)", fontSize: 14, fill: "#666a72" }} />
                            <Line
                              type="monotone"
                              dataKey="ndvi"
                              stroke="#759A64"
                              strokeWidth={2}
                              dot={{ r: 2 }}
                              connectNulls={false}
                              name="Plant green score"
                            />
                          </LineChart>
                        </ResponsiveContainer>
                      </div>
                      <div className="mt-3 text-base text-gray-800 bg-[#232428] border border-[#505158] rounded-md p-3">
                        <strong>What this means:</strong> A higher score usually means more green plant cover. It does not tell us how much grain or fruit you will get, and it cannot prove that a crop is healthy. Each picture covers an area about 232 metres wide. It may include land outside your farm.
                      </div>
                    </div>

                    {/* Seasonal NDVI Breakdown */}
                    <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                      <h3 className="font-bold text-[#e7e8eb] text-lg mb-3">Average plant green score by season</h3>
                      <div className="overflow-x-auto">
                        <table className="min-w-full text-xs text-left">
                          <thead className="bg-[#232428] border-b border-[#44464d] font-semibold text-[#e7e8eb]">
                            <tr>
                              <th className="py-3 px-3">Year</th>
                              <th className="py-3 px-3">Season</th>
                              <th className="py-3 px-3">Average green score</th>
                              <th className="py-3 px-3">Lowest score</th>
                              <th className="py-3 px-3">Highest score</th>
                              <th className="py-3 px-3">Clear pictures used</th>
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-gray-100">
                            {(vegData.seasons || []).map((s, idx) => (
                              <tr key={idx} className="hover:bg-[#202125]">
                                <td className="py-2 px-3 font-medium">{s.year}</td>
                                <td className="py-2 px-3 capitalize font-semibold text-[#6a6d75]">{s.season}</td>
                                <td className="py-2 px-3 font-mono font-bold text-[#e7e8eb]">{s.mean !== null ? s.mean.toFixed(4) : "—"}</td>
                                <td className="py-2 px-3 font-mono">{s.min !== null ? s.min.toFixed(4) : "—"}</td>
                                <td className="py-2 px-3 font-mono text-zinc-700">{s.max !== null ? s.max.toFixed(4) : "—"}</td>
                                <td className="py-2 px-3 text-gray-500">{s.n_obs} composites</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </>
                  )
                )}
              </div>
            )}

            {/* TAB 5: DATA PROVENANCE */}
            {activeTab === "quality" && (
              <div className="space-y-6">
                <div className="bg-white p-5 rounded-lg border border-[#44464d] shadow-xs">
                  <h3 className="font-bold text-[#e7e8eb] text-sm mb-4">Where this information comes from</h3>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* NASA POWER Quality */}
                    <div className="border border-[#44464d] p-4 rounded-md bg-[#202125]">
                      <div className="flex items-center justify-between border-b border-[#44464d] pb-2 mb-3">
                        <span className="font-bold text-xs uppercase text-[#e7e8eb]">NASA weather and rainfall data</span>
                        <span className="text-xs bg-zinc-100 text-zinc-800 px-2 py-0.5 rounded font-semibold">Active</span>
                      </div>
                      <dl className="text-xs space-y-2">
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Spatial Resolution:</dt>
                          <dd className="font-medium">0.5° × 0.625° regional grid (~50 km)</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Temporal Resolution:</dt>
                          <dd className="font-medium">Daily</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Observed Variables:</dt>
                          <dd className="font-medium">T2M, T2M_MAX, T2M_MIN, PRECTOTCORR, RH2M, Solar</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Modeled Variables:</dt>
                          <dd className="font-medium text-zinc-800 font-semibold">GWETTOP, GWETROOT (MERRA-2 wetness)</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Completeness Rule:</dt>
                          <dd className="font-medium">≥ 90% calendar days required per year</dd>
                        </div>
                      </dl>
                    </div>

                    {/* MODIS Terra Quality */}
                    <div className="border border-[#44464d] p-4 rounded-md bg-[#202125]">
                      <div className="flex items-center justify-between border-b border-[#44464d] pb-2 mb-3">
                        <span className="font-bold text-xs uppercase text-[#e7e8eb]">MODIS satellite plant pictures</span>
                        <span className="text-xs bg-zinc-100 text-zinc-800 px-2 py-0.5 rounded font-semibold">Active</span>
                      </div>
                      <dl className="text-xs space-y-2">
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Provider:</dt>
                          <dd className="font-medium">ORNL DAAC Subset API</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Spatial Resolution:</dt>
                          <dd className="font-medium">231.7 m sinusoidal pixel containing point</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Temporal Resolution:</dt>
                          <dd className="font-medium">16-day composite</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Quality Filter:</dt>
                          <dd className="font-medium">Ranks 0 (Good) and 1 (Marginal)</dd>
                        </div>
                        <div className="flex justify-between">
                          <dt className="text-gray-500">Missing Data Protocol:</dt>
                          <dd className="font-medium">Gaps preserved as null; never replaced with zero</dd>
                        </div>
                      </dl>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-[#44464d] py-4 text-center text-xs text-gray-500">
        <p>Vasundhara &copy; 2026 &bull; NASA Space Apps Agriculture &bull; Location: {lat.toFixed(4)}°, {lon.toFixed(4)}°</p>
        <p className="mx-auto mt-2 max-w-4xl px-4">
          AI tools assisted with parts of this code and descriptive text. Climate data comes from NASA POWER, plant-growth observations from MODIS, and crop comparisons are heuristic estimates—not AI-generated observations.
        </p>
      </footer>

      {locationPromptOpen && (
        <div className="dashboard-location-backdrop">
          <section
            className="dashboard-location-dialog"
            role="dialog"
            aria-modal="true"
            aria-labelledby="dashboard-location-title"
            aria-describedby="dashboard-location-description"
          >
            <p className="dashboard-location-eyebrow">Personalize your dashboard</p>
            <h2 id="dashboard-location-title">Choose a location</h2>
            <p id="dashboard-location-description">
              Search for a place or enter its coordinates. We will save your choice in this browser for next time.
            </p>

            <form className="dashboard-location-search" onSubmit={searchForInitialLocation}>
              <label htmlFor="dashboard-location-search-input">Search by city, town, or district</label>
              <div className="dashboard-location-search-row">
                <input
                  id="dashboard-location-search-input"
                  type="search"
                  value={locationSearch}
                  onChange={(event) => setLocationSearch(event.target.value)}
                  placeholder="e.g. Pune or Varanasi"
                  autoFocus
                />
                <button type="submit" className="dashboard-location-primary" disabled={locationSearching}>
                  {locationSearching ? "Searching..." : "Search"}
                </button>
              </div>
            </form>

            <div className="dashboard-location-coordinate-entry">
              <h3>Or enter coordinates</h3>
              <div className="dashboard-location-coordinate-grid">
                <div>
                  <label htmlFor="dashboard-location-latitude">Latitude (-90 to 90)</label>
                  <input
                    id="dashboard-location-latitude"
                    type="number"
                    min="-90"
                    max="90"
                    step="any"
                    value={inputLat}
                    onChange={(event) => setInputLat(event.target.value)}
                  />
                </div>
                <div>
                  <label htmlFor="dashboard-location-longitude">Longitude (-180 to 180)</label>
                  <input
                    id="dashboard-location-longitude"
                    type="number"
                    min="-180"
                    max="180"
                    step="any"
                    value={inputLon}
                    onChange={(event) => setInputLon(event.target.value)}
                  />
                </div>
              </div>
              <button type="button" className="dashboard-location-primary" onClick={applyInitialCoordinates}>
                Use these coordinates
              </button>
            </div>

            {locationSearchError && <p role="alert" className="dashboard-location-error">{locationSearchError}</p>}
            <button type="button" className="dashboard-location-skip" onClick={skipInitialLocationSetup}>
              Skip for now
            </button>
          </section>
        </div>
      )}
    </div>
  );
}
