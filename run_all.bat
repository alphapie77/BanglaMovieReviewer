@echo off
echo Starting BanglaMovieReviewer...
echo.

REM Setup and start backend
echo [1/2] Setting up Backend...
start "Backend" cmd /k "cd backend && (if not exist venv (echo Creating virtual environment... && python -m venv venv)) && call venv\Scripts\activate.bat && (echo Installing dependencies... && pip install -r requirements.txt) && (echo Running migrations... && python manage.py migrate) && (echo Starting backend server... && python manage.py runserver 0.0.0.0:8000)"

REM Wait for backend to initialize
timeout /t 8 /nobreak >nul

REM Setup and start frontend
echo [2/2] Setting up Frontend...
start "Frontend" cmd /k "cd frontend && (if not exist node_modules (echo Installing frontend dependencies... && npm install)) && (echo Starting frontend server... && npm start)"

echo.
echo ========================================
echo   BanglaMovieReviewer Started!
echo ========================================
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Both servers are starting in separate windows...
