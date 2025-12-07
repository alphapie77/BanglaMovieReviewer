@echo off
start "Backend" cmd /k "cd backend && (if not exist venv python -m venv venv) && venv\Scripts\activate && (if not exist venv\Lib\site-packages\django pip install -r requirements.txt) && (if not exist db.sqlite3 python manage.py migrate) && python manage.py runserver"
timeout /t 3 /nobreak >nul
start "Frontend" cmd /k "cd frontend && (if not exist node_modules npm install) && npm start"
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
