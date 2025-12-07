@echo off
echo ========================================
echo Cleaning Project
echo ========================================
echo.
echo This will remove:
echo   - backend/venv/
echo   - backend/db.sqlite3
echo   - frontend/node_modules/
echo   - frontend/build/
echo.
set /p confirm="Are you sure? (Y/N): "
if /i not "%confirm%"=="Y" (
    echo Cancelled.
    pause
    exit /b 0
)

echo.
echo Cleaning backend...
if exist backend\venv rmdir /s /q backend\venv
if exist backend\db.sqlite3 del /q backend\db.sqlite3
if exist backend\__pycache__ rmdir /s /q backend\__pycache__

echo Cleaning frontend...
if exist frontend\node_modules rmdir /s /q frontend\node_modules
if exist frontend\build rmdir /s /q frontend\build

echo.
echo ========================================
echo Clean Complete!
echo Run: build_all.bat to rebuild
echo ========================================
pause
