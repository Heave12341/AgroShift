@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title VASUNDHARA - Local startup

echo.
echo ============================================================
echo   VASUNDHARA - LOCAL WEBSITE + BACKEND
echo ============================================================
echo.
echo Project folder: %CD%

where npm >nul 2>&1
if errorlevel 1 (
  echo ERROR: Node.js and npm are not installed or not on PATH.
  echo Install the current Node.js LTS version, then reopen this file.
  pause
  exit /b 1
)

set PYTHON_CMD=
where py >nul 2>&1
if not errorlevel 1 set PYTHON_CMD=py -3
if "%PYTHON_CMD%"=="" (
  where python >nul 2>&1
  if not errorlevel 1 set PYTHON_CMD=python
)
if "%PYTHON_CMD%"=="" (
  echo ERROR: Python 3 is not installed or not on PATH.
  echo Install Python 3.11 or newer and tick "Add Python to PATH".
  pause
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo Creating Python virtual environment...
  %PYTHON_CMD% -m venv .venv
  if errorlevel 1 (
    echo ERROR: Could not create .venv. Check your Python installation.
    pause
    exit /b 1
  )
)

".venv\Scripts\python.exe" -c "import fastapi, uvicorn, httpx, orjson, pandas, numpy, scipy, sklearn, pymannkendall" >nul 2>&1
if errorlevel 1 (
  echo Installing missing backend requirements...
  ".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -r backend\requirements.txt
  if errorlevel 1 (
    echo ERROR: Backend dependency installation failed.
    echo Check your internet connection and the error above.
    pause
    exit /b 1
  )
)

if not exist "frontend\node_modules\vite\bin\vite.js" (
  echo Installing frontend packages (first run only)...
  pushd frontend
  call npm ci
  set NPM_RESULT=%ERRORLEVEL%
  popd
  if not "%NPM_RESULT%"=="0" (
    echo ERROR: npm ci failed. Check the error above.
    pause
    exit /b 1
  )
)

echo.
echo Starting backend and frontend in separate windows...
start "VASUNDHARA API - PORT 8000" "%ComSpec%" /k "call ""%~dp0RUN_BACKEND_WINDOWS.bat"""
timeout /t 3 /nobreak >nul
start "VASUNDHARA WEB - PORT 5173" "%ComSpec%" /k "call ""%~dp0RUN_FRONTEND_WINDOWS.bat"""

echo.
echo ============================================================
echo   OPEN: http://localhost:5173/
echo   DASHBOARD: http://localhost:5173/dashboard/
echo   API HEALTH: http://127.0.0.1:8000/api/health
echo ============================================================
echo.
echo Keep both service windows open. If one stops, read its error.
pause
