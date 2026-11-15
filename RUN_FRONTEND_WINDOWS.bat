@echo off
setlocal
cd /d "%~dp0frontend"
title VASUNDHARA WEB

echo Starting VASUNDHARA website from: %CD%
if not exist "node_modules\vite\bin\vite.js" (
  echo ERROR: Frontend packages are missing. Run START_VASUNDHARA_WINDOWS.bat first.
  pause
  exit /b 1
)
echo.
echo Landing page: http://localhost:5173/
echo Dashboard:    http://localhost:5173/dashboard/
echo Press CTRL+C to stop the website.
echo.
call npm run dev -- --host 127.0.0.1
if errorlevel 1 echo ERROR: Vite stopped. Read the error above.
pause
