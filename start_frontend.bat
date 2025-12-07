@echo off
echo ========================================
echo React Frontend Setup and Start
echo ========================================
echo.

cd frontend

REM Check if Node.js is installed
where node >nul 2>nul
if errorlevel 1 (
    echo ERROR: Node.js is not installed
    echo Please install Node.js 16+ from https://nodejs.org/
    pause
    exit /b 1
)

REM Check if dependencies are installed
if not exist node_modules (
    echo [1/2] Installing dependencies (this may take 2-3 minutes)...
    call npm install
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        echo Try: npm cache clean --force
        pause
        exit /b 1
    )
)

echo [2/2] Starting development server...
echo.
echo ========================================
echo Frontend Ready!
echo Server: http://localhost:3000
echo Press Ctrl+C to stop
echo ========================================
echo.
call npm start
