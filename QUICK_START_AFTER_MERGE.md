# Vasundhara merged update

## What changed
- Dashboard now uses only black, charcoal and grey tones. Green and orange dashboard accents are removed.
- Dashboard-wide automatic translation has been removed. The landing page's own language selector remains unchanged.
- Teammate crop data merged: 1,232 catalogued crops. The original 53 locally calibrated Indian crop records were preserved.
- Existing five-criteria scoring, soil pH / organic-carbon logic, MODIS location-change handling, and landing-page/dashboard routes are retained.
- Teammate's curated global-region crop pathways are used for coordinates outside India.

## Run locally
Terminal 1 (project root):
```cmd
.venv\Scripts\activate
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```
Terminal 2 (`frontend` folder):
```cmd
npm run dev -- --host 127.0.0.1
```

## Check
- http://127.0.0.1:8000/api/health
- http://127.0.0.1:8000/api/rotation/crops/summary (should report 1,232 crops)
- http://localhost:5173/ (landing page)
- http://localhost:5173/dashboard/ (dashboard)

Dashboard translation has been removed; language selection on the independent landing page is retained.
