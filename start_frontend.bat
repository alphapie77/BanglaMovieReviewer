@echo off
echo ========================================
echo Starting React Frontend Server
echo ========================================
echo.

cd frontend

if not exist node_modules (
    echo Installing dependencies...
    call npm install
    echo.
)

echo Starting server on http://localhost:3000
echo Press Ctrl+C to stop
echo.
call npm start
