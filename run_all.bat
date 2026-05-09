@echo off
echo ============================================================
echo   BANGLA MOVIE REVIEWER - COMPLETE SETUP
echo ============================================================
echo.
echo This script will:
echo   - Setup Python virtual environment
echo   - Install all backend dependencies (including Hugging Face)
echo   - Run database migrations
echo   - Start backend server
echo   - Install frontend dependencies
echo   - Start frontend server
echo.
echo First run may take 10-15 minutes to download dependencies.
echo Models will download from Hugging Face on first use.
echo.
pause

REM Setup and start backend
echo.
echo ============================================================
echo [1/2] BACKEND SETUP
echo ============================================================
echo.

start "Backend Server" cmd /k "cd /d %~dp0backend && if not exist venv (echo [Backend] Creating virtual environment... && python -m venv venv) else (echo [Backend] Virtual environment exists) && echo. && echo [Backend] Activating virtual environment... && call venv\Scripts\activate.bat && echo. && echo [Backend] Installing dependencies... && pip install --upgrade pip && pip install -r requirements.txt && echo. && echo [Backend] Running database migrations... && python manage.py migrate && echo. && echo ============================================================ && echo   BACKEND READY! && echo ============================================================ && echo. && echo Models will download from Hugging Face on first use && echo Starting backend server at http://localhost:8000 && echo. && python manage.py runserver"

REM Wait for backend to initialize
echo.
echo [Waiting] Backend is starting (15 seconds)...
timeout /t 15 /nobreak >nul

REM Setup and start frontend
echo.
echo ============================================================
echo [2/2] FRONTEND SETUP
echo ============================================================
echo.

start "Frontend Server" cmd /k "cd /d %~dp0frontend && if not exist node_modules (echo [Frontend] Installing dependencies... && npm install) else (echo [Frontend] Dependencies already installed) && echo. && echo ============================================================ && echo   FRONTEND READY! && echo ============================================================ && echo. && echo Starting frontend server at http://localhost:3000 && echo. && npm start"

echo.
echo ============================================================
echo   BOTH SERVERS STARTING!
echo ============================================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000 (opens automatically)
echo.
echo Two windows opened:
echo   1. Backend Server (Django)
echo   2. Frontend Server (React)
echo.
echo IMPORTANT:
echo   - First API call will download models from Hugging Face
echo   - This may take 2-3 minutes per model
echo   - Models are cached after first download
echo   - No local model files needed!
echo.
echo To stop: Close both terminal windows
echo.
echo ============================================================
