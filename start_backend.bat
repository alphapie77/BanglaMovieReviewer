@echo off
cd backend
if not exist venv python -m venv venv
call venv\Scripts\activate
if not exist venv\Lib\site-packages\django pip install -r requirements.txt
if not exist db.sqlite3 python manage.py migrate
echo Backend: http://localhost:8000
python manage.py runserver
