@echo off
setlocal
cd /d "%~dp0"
title VASUNDHARA API

echo Starting VASUNDHARA API from: %CD%
if not exist ".venv\Scripts\python.exe" (
  echo ERROR: .venv is missing. Run START_VASUNDHARA_WINDOWS.bat first.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" -c "import fastapi, uvicorn, httpx, orjson, pandas, numpy, scipy, sklearn, pymannkendall" >nul 2>&1
if errorlevel 1 (
  echo ERROR: One or more backend packages are missing.
  echo Run START_VASUNDHARA_WINDOWS.bat to install them.
  pause
  exit /b 1
)
echo.
echo API health check: http://127.0.0.1:8000/api/health
echo Press CTRL+C to stop the API.
echo.
".venv\Scripts\python.exe" -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
if errorlevel 1 echo ERROR: API stopped. Read the error above.
pause
