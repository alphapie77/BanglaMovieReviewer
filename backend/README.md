# Backend - Django REST API

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Endpoints

- `POST /api/sentiment/analyze/` - Analyze sentiment
- `GET /api/sentiment/history/` - Get analysis history
- `GET /api/sentiment/` - List all analyses
- `GET /api/sentiment/{id}/` - Get specific analysis

## Admin Panel

http://localhost:8000/admin
