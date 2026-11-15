# Vasundhara branding and crop-planner update

## Branding
- Replaced the landing-page header and footer's placeholder SVG mark with the dashboard's existing `frontend/public/logo.png`.
- Added `frontend/public/favicon.png` derived from that same dashboard logo and linked it from both landing-page entry files.
- Dashboard surfaces remain charcoal/black/grey; primary actions, selected locations, tabs and view-mode selection use the landing page's leaf-green accent.
- Removed grayscale treatment from the dashboard logo and map tiles.
- Dashboard source CSS contains no `#D67C33` accent.

## Crop planner
- The 1,232-record global crop catalogue remains loaded into the custom rotation planner's Kharif, Rabi and Zaid crop selectors.
- Chosen crop IDs are submitted to `/api/rotation/evaluate-custom`, where each selected crop is evaluated through the same location-, soil-, irrigation- and five-criteria-aware scoring engine.
- The planner now displays the number of crop records loaded.
- Annual/perennial crops are also available in the Rabi selector; annual crops are available in the Zaid selector.

## Files changed
- `frontend/src/index.css`
- `frontend/src/RotationLab.tsx`
- `frontend/index.html`
- `frontend/public/landing/index.html`
- Added `frontend/public/favicon.png`
- Added `frontend/public/landing/images/vasundhara-logo.png`

## Validation
- Python syntax compilation passed for `backend/main.py`, `backend/rotation.py`, and `backend/crops_registry.py`.
- Confirmed the global catalogue contains 1,232 entries.
- Confirmed the custom planner loads all crop records and calls the custom evaluation API.
- Confirmed the dashboard CSS does not contain `#D67C33`.
- A full frontend production build was not run in this environment.
