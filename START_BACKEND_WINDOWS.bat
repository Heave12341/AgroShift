@echo off
setlocal
cd /d "%~dp0"
title VASUNDHARA API - STARTUP CHECK

echo ==============================================
echo   VASUNDHARA BACKEND ONLY
 echo ==============================================
echo Project folder: %CD%
if not exist ".venv\Scripts\python.exe" (
  echo Creating Python environment...
  where py >nul 2>&1
  if not errorlevel 1 (py -3 -m venv .venv) else (python -m venv .venv)
  if errorlevel 1 (
    echo ERROR: Could not create Python environment.
    pause
    exit /b 1
  )
)
".venv\Scripts\python.exe" -c "import fastapi, uvicorn, httpx, orjson, pandas, numpy, scipy, sklearn, pymannkendall" >nul 2>&1
if errorlevel 1 (
  echo Installing missing backend packages...
  ".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -r backend\requirements.txt
  if errorlevel 1 (
    echo ERROR: Backend package installation failed.
    pause
    exit /b 1
  )
)
echo.
echo API is starting at http://127.0.0.1:8000
 echo Check: http://127.0.0.1:8000/api/health
echo Do not close this window while using the dashboard.
echo.
".venv\Scripts\python.exe" -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
if errorlevel 1 echo ERROR: API stopped. Read the traceback above.
pause
