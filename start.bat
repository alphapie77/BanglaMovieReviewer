@echo off
echo ============================================================
echo   STARTING BANGLA MOVIE REVIEWER
echo ============================================================
echo.
echo Starting backend and frontend servers...
echo.

REM Start backend
echo [1/2] Starting Backend Server...
start "Backend Server" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && python manage.py runserver"

REM Wait a bit
timeout /t 5 /nobreak >nul

REM Start frontend
echo [2/2] Starting Frontend Server...
start "Frontend Server" cmd /k "cd /d %~dp0frontend && npm start"

echo.
echo ============================================================
echo   SERVERS STARTING!
echo ============================================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Two windows opened. Browser will open automatically.
echo.
echo To stop: Close both terminal windows
echo.
