@echo off
echo ========================================
echo Starting Django Backend Server
echo ========================================
echo.

cd backend

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

if not exist db.sqlite3 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
    echo Running migrations...
    python manage.py migrate
    echo.
)

echo Starting server on http://localhost:8000
echo Press Ctrl+C to stop
echo.
python manage.py runserver
