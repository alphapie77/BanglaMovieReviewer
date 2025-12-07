@echo off
echo ========================================
echo Django Backend Setup and Start
echo ========================================
echo.

cd backend

REM Check if virtual environment exists
if not exist venv (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Make sure Python 3.8+ is installed
        pause
        exit /b 1
    )
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate

REM Check if dependencies are installed
if not exist venv\Lib\site-packages\django (
    echo [3/4] Installing dependencies (this may take 5-10 minutes)...
    pip install --upgrade pip
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Check if database exists
if not exist db.sqlite3 (
    echo [4/4] Setting up database...
    python manage.py migrate
    if errorlevel 1 (
        echo ERROR: Failed to run migrations
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo Backend Ready!
echo Server: http://localhost:8000
echo Admin: http://localhost:8000/admin
echo Press Ctrl+C to stop
echo ========================================
echo.
python manage.py runserver
