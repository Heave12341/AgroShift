# ROTATION IQ — MODIS location refresh and farmer-friendly UI fix

This update includes the earlier crop-recommendation fix plus the new MODIS loading, location-refresh, and readability work.

## Files included

- `backend/main.py` — adds a progress-enabled plant-growth stream and a shared vegetation analysis function.
- `backend/modis_ornl.py` — allows longer satellite requests and retries temporary request failures.
- `frontend/src/api.ts` — reads progress events from the stream.
- `frontend/src/App.tsx` — refreshes plant-growth data for each selected place and displays clear progress, error, and estimate messages.
- `frontend/src/MapPicker.tsx` — uses the latest location callback when a farmer taps the map.
- `frontend/src/index.css` — larger readable text, stronger contrast, large controls, and visible keyboard focus across the app.
- `frontend/src/RotationLab.tsx` — clearer farmer-facing labels and optional soil-test fields.
- `frontend/src/types.ts` and `backend/rotation.py` — included to preserve the previously supplied recommendation-engine fix.
- `tests/test_api.py` and `tests/test_profile_adaptation.py` — regression tests.

## Install the patch

1. Make a backup of your current project folder.
2. Extract this ZIP into the **project root** (the folder that contains `backend`, `frontend`, and `tests`). Keep the folder names. Allow files to be replaced.
3. Install backend dependencies if needed:

   ```bash
   python -m pip install -r backend/requirements.txt
   ```

4. Run backend tests from the project root:

   ```bash
   python -m unittest discover -s tests -q
   ```

5. Install frontend dependencies for your own computer and build the app:

   ```bash
   cd frontend
   npm ci
   npm run build
   ```

6. Restart the backend and frontend servers, then open the **Plant growth pictures** tab. Move the map pin or search for another place. You should see a progress message while the new place loads.

## What to expect

- The old satellite request is cancelled when the place changes. A new request starts for the new coordinates.
- The app sends progress updates while it finds and reads satellite pictures. It can send a “still waiting” message if the satellite service is slow.
- The satellite request can take longer the first time a new place is checked. If live MODIS data cannot be retrieved and the example option is enabled, the screen clearly labels the result as an example estimate, not a real satellite reading.
- If the service cannot return a result, the screen shows an error and a retry action instead of leaving the details area blank.
- Larger text, stronger contrast, simpler labels, and larger buttons apply across the whole interface.

## Verification performed while preparing this update

- Backend automated tests: 66 passed.
- Frontend TypeScript check: passed (`npx tsc --noEmit`).
- The production Vite bundle could not be run in this environment because the uploaded `node_modules` folder contains Windows-only native Rollup binaries. Run `npm ci` on your own computer before `npm run build` to install the correct binaries for that computer.

The app is currently English-only. The accessibility notes in `docs/FARMER_ACCESSIBILITY.md` explain what remains before real-world deployment with farmers who prefer another language.
