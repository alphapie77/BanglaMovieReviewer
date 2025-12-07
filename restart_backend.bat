@echo off
echo Restarting Backend Server...
cd backend
call venv\Scripts\activate
python manage.py runserver
