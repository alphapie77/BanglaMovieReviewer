@echo off
echo ========================================
echo Building React Frontend
echo ========================================
echo.

cd frontend

echo [1/3] Cleaning old build...
if exist build rmdir /s /q build
if exist node_modules rmdir /s /q node_modules

echo [2/3] Installing dependencies...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [3/3] Building production bundle...
call npm run build
if errorlevel 1 (
    echo ERROR: Failed to build
    pause
    exit /b 1
)

echo.
echo ========================================
echo Frontend Build Complete!
echo Output: frontend/build/
echo Run: start_frontend.bat (for dev)
echo ========================================
pause
