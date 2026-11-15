# Vasundhara — quick fix for the current screenshot and local API errors

## What changed
- Dashboard styling now follows the landing page: charcoal `#141613`, panel `#1D211C`, leaf green `#759A64`, harvest orange `#D67C33` and Atkinson Hyperlegible.
- The content width is 1320px (matching the landing page's hero/footer width), not the compressed 1120px layout.
- Text, controls and spacing have been normalised. Location controls are in two clear rows.
- Duplicate quick-location chips are tucked under “More nearby and regional places”.
- Easy view and Detailed view now have explicit high-contrast active/inactive states.
- The Windows launcher checks Node.js, Python and all backend dependencies, then opens the backend and frontend in separate persistent terminals.

## Start locally on Windows
1. Extract the project into a normal writable folder (not inside the ZIP preview or a temporary Downloads preview).
2. Make sure Python 3.11+ and Node.js LTS are installed.
3. Double-click `START_VASUNDHARA_WINDOWS.bat` in the project root.
4. Keep both terminal windows open.
5. Visit `http://localhost:5173/` for the landing page and `http://localhost:5173/dashboard/` for the dashboard.
6. Visit `http://127.0.0.1:8000/api/health`. It must return `{"ok":true}`.

## If you still see `ECONNREFUSED 127.0.0.1:8000`
That message means the backend process is not listening. Look at the **VASUNDHARA API - PORT 8000** terminal and read the first red/traceback error. Do not start only the frontend. The dashboard requires both terminals to remain open.

## If the BAT window closes
Open the project root in File Explorer, click the address bar, type `cmd` and press Enter. Then run:

```cmd
START_VASUNDHARA_WINDOWS.bat
```

This keeps the terminal attached so the error remains visible. Also confirm that the same folder contains `backend`, `frontend`, `tests`, `.env.example` and `START_VASUNDHARA_WINDOWS.bat`.

## Build check
```cmd
cd frontend
npm ci
npm run build
```

The dashboard can be opened directly at `/dashboard/`; the site root `/` is the landing page.
