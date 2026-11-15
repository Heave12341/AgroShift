# Vasundhara — Current project changes

## Landing page and routes
- The supplied landing page opens at `/`.
- The farmer dashboard opens at `/dashboard/` and can be mapped to `dashboard.vasundhara.earth` through the Vercel domain configuration.
- Landing-page language selection remains on the landing page. The dashboard interface is English-only.

## Dashboard appearance
- Replaced the previous brand colours with a neutral charcoal, black and grey theme.
- Removed green and orange dashboard accents and decorative colour emojis.
- Kept readable text, visible focus indicators, responsive layouts and accessible control sizes.
- Preserved the Easy view and Detailed view for crop recommendations.

## Crop recommendations and catalogue
- Preserved the existing 53 locally calibrated Indian crop records and their IDs.
- Merged the teammate's 1,232-record global crop catalogue.
- Added global-region recommendation pathways while retaining the current Indian regional pathways and five-criteria scoring engine.
- Exposed the expanded catalogue to the crop explorer and custom rotation builder.
- Kept regional suitability caveats: a catalogue entry is not proof of local suitability.

## Climate and vegetation
- Kept the MODIS location-change request handling, progress updates and explicit synthetic-estimate labelling.
- Kept the NASA POWER climate and trend-analysis modules.

## Verification notes
- Python syntax compilation passed.
- 39 focused regression tests passed for rotation scoring, the merged global catalogue, farmer-profile adaptation and MODIS fallback labelling.
- Five-region recommendation smoke tests passed (Bihar, Kerala, US Corn Belt, Brazilian Cerrado and temperate Europe).
- The full suite could not be run in this environment because `pymannkendall` is not installed; install `backend/requirements.txt` before running all tests.
- Frontend production build was not run here because frontend dependencies are not installed. Run `npm ci` and `npm run build` from `frontend/`.
