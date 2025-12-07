@echo off
echo ========================================
echo Starting Full Application
echo ========================================
echo.

echo Starting Backend in new window...
start "Backend Server" cmd /k "start_backend.bat"

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak >nul

echo Starting Frontend in new window...
start "Frontend Server" cmd /k "start_frontend.bat"

echo.
echo ========================================
echo Both servers are starting!
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Check the new terminal windows
echo Close this window when done
echo ========================================
pause
