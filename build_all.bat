@echo off
echo ========================================
echo Building Complete Project
echo ========================================
echo.

echo Step 1: Building Backend...
call build_backend.bat
if errorlevel 1 (
    echo ERROR: Backend build failed
    pause
    exit /b 1
)

echo.
echo Step 2: Building Frontend...
call build_frontend.bat
if errorlevel 1 (
    echo ERROR: Frontend build failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Complete Build Successful!
echo.
echo To run the application:
echo   1. Run: start_backend.bat
echo   2. Run: start_frontend.bat
echo   3. Open: http://localhost:3000
echo ========================================
pause
