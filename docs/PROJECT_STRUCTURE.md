# 📁 Project Structure Documentation

## Overview

This document explains the complete project structure and the purpose of each file/folder.

---

## Root Directory

```
movieReview/
├── backend/                 # Django REST API + ML Model
├── frontend/                # React Application
├── ml_model/                # ML Model Documentation
├── *.bat                    # Windows batch scripts
├── *.md                     # Documentation files
└── .gitignore              # Git ignore rules
```

---

## Backend Structure

```
backend/
├── config/                          # Django Project Configuration
│   ├── __init__.py                 # Python package marker
│   ├── settings.py                 # Django settings (CORS, DB, etc.)
│   ├── urls.py                     # Main URL routing
│   ├── wsgi.py                     # WSGI server config
│   └── asgi.py                     # ASGI server config
│
├── sentiment_api/                   # Main API Application
│   ├── migrations/                 # Database migrations
│   │   └── 0001_initial.py        # Initial database schema
│   ├── __init__.py                # Python package marker
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Database models (SentimentAnalysis)
│   ├── serializers.py             # DRF serializers
│   ├── views.py                   # API endpoints (ViewSets)
│   ├── urls.py                    # API URL routing
│   └── ml_service.py              # ML Model Integration (BERT + LIME)
│
├── db.sqlite3                      # SQLite database file
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
├── test_model.py                   # ML model test script
├── test_api.py                     # API test script
├── README.md                       # Backend documentation
└── .gitignore                      # Backend git ignore
```

### Key Backend Files

**config/settings.py**
- Database configuration (SQLite)
- CORS settings for frontend
- Installed apps and middleware
- Static files configuration

**sentiment_api/models.py**
```python
SentimentAnalysis Model:
- review_text: TextField (user input)
- sentiment: CharField (Positive/Negative/Neutral)
- confidence: FloatField (0-100)
- word_importance: JSONField (LIME results)
- created_at: DateTimeField (timestamp)
```

**sentiment_api/ml_service.py**
- `SentimentAnalyzer` class
- BERT model loading (nlptown/bert-base-multilingual-uncased-sentiment)
- LIME explainer integration
- Keyword-enhanced detection for Bangla
- Word importance calculation

**sentiment_api/views.py**
- `SentimentAnalysisViewSet`: CRUD operations
- `analyze()`: POST endpoint for sentiment analysis
- `history()`: GET endpoint for last 20 analyses

---

## Frontend Structure

```
frontend/
├── public/                          # Static public files
│   └── index.html                  # HTML template
│
├── src/                            # Source code
│   ├── pages/                      # Main application pages
│   │   ├── Home.js                # Landing page
│   │   ├── Home.css               # Landing page styles
│   │   ├── Analyzer.js            # Review input page
│   │   ├── Analyzer.css           # Input page styles
│   │   ├── Result.js              # Results page with charts
│   │   ├── Result.css             # Results page styles
│   │   ├── History.js             # Analysis history page
│   │   ├── History.css            # History page styles
│   │   ├── About.js               # About page
│   │   └── About.css              # About page styles
│   │
│   ├── components/                 # Reusable components
│   │   ├── AnalyzerForm.js        # Review input form
│   │   ├── AnalyzerForm.css       # Form styles
│   │   ├── HistoryPanel.js        # History list component
│   │   ├── HistoryPanel.css       # History styles
│   │   ├── ResultDisplay.js       # Result display component
│   │   └── ResultDisplay.css      # Result styles
│   │
│   ├── services/                   # API integration
│   │   └── api.js                 # Axios HTTP calls
│   │
│   ├── App.js                      # Main app component (Router)
│   ├── App.css                     # Global app styles
│   ├── index.js                    # React entry point
│   └── index.css                   # Global CSS
│
├── package.json                    # Node dependencies
├── package-lock.json               # Locked dependency versions
├── README.md                       # Frontend documentation
└── .gitignore                      # Frontend git ignore
```

### Key Frontend Files

**src/App.js**
- React Router setup
- Navigation menu
- Route definitions:
  - `/` → Home
  - `/analyzer` → Analyzer
  - `/result` → Result
  - `/history` → History
  - `/about` → About

**src/pages/Analyzer.js**
- Review input form
- Example reviews
- Loading states
- Error handling
- Navigation to Result page

**src/pages/Result.js**
- Sentiment display with icon
- Pie chart (confidence visualization)
- Bar chart (word importance)
- Color-coded word analysis
- Professional tooltips

**src/services/api.js**
```javascript
- analyzeSentiment(reviewText): POST to /api/sentiment/analyze/
- getHistory(): GET from /api/sentiment/history/
```

---

## ML Model Directory

```
ml_model/
├── README.md                       # ML model documentation
└── .gitignore                      # Ignore model cache
```

**Model Details:**
- Name: nlptown/bert-base-multilingual-uncased-sentiment
- Type: BERT-based sentiment classifier
- Languages: 104 languages including Bangla
- Size: ~500MB
- Cache Location: `~/.cache/huggingface/`

---

## Batch Scripts (Windows)

```
run_all.bat              # Start both backend and frontend
start_backend.bat        # Start backend only
start_frontend.bat       # Start frontend only
restart_backend.bat      # Restart backend server
clean_all.bat           # Clean all caches and temp files
```

---

## Documentation Files

```
README.md                # Main project documentation
START_HERE.md           # Quick start guide for beginners
SETUP_GUIDE.md          # Detailed installation instructions
API_DOCUMENTATION.md    # API endpoints and examples
TROUBLESHOOTING.md      # Common issues and solutions
QUICK_FIX.md           # ML model troubleshooting
PROJECT_STRUCTURE.md    # This file
```

---

## Data Flow

```
User Input (Frontend)
    ↓
Analyzer.js → api.js
    ↓
POST /api/sentiment/analyze/
    ↓
views.py → ml_service.py
    ↓
BERT Model + LIME
    ↓
Database (SQLite)
    ↓
JSON Response
    ↓
Result.js (Charts & Visualization)
```

---

## Database Schema

**SentimentAnalysis Table:**
```sql
CREATE TABLE sentiment_analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    review_text TEXT NOT NULL,
    sentiment VARCHAR(20) NOT NULL,
    confidence FLOAT NOT NULL,
    word_importance JSON NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## API Endpoints

```
GET  /api/sentiment/              # List all analyses
POST /api/sentiment/analyze/      # Analyze new review
GET  /api/sentiment/history/      # Get last 20 analyses
GET  /api/sentiment/{id}/         # Get specific analysis
PUT  /api/sentiment/{id}/         # Update analysis
DELETE /api/sentiment/{id}/       # Delete analysis
```

---

## Dependencies

### Backend (requirements.txt)
```
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
torch>=2.0.0
transformers>=4.40.0
lime==0.2.0.1
numpy>=1.24.0
scikit-learn>=1.3.0
```

### Frontend (package.json)
```json
{
  "react": "^18.2.0",
  "react-router-dom": "^6.20.0",
  "axios": "^1.6.2",
  "recharts": "^2.10.3",
  "lucide-react": "^0.294.0"
}
```

---

## Environment Variables

**Backend (.env - optional):**
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

**Frontend (.env - optional):**
```
REACT_APP_API_URL=http://localhost:8000/api
```

---

## Build & Deployment

### Development
```bash
# Backend
python manage.py runserver

# Frontend
npm start
```

### Production
```bash
# Backend
gunicorn config.wsgi:application

# Frontend
npm run build
serve -s build
```

---

## Testing

### Backend Tests
```bash
cd backend
python test_model.py      # Test ML model
python test_api.py        # Test API endpoints
python manage.py test     # Run Django tests
```

### Frontend Tests
```bash
cd frontend
npm test                  # Run React tests
```

---

## Git Structure

```
movieReview/              # Main repository
├── .git/                # Git metadata
├── backend/             # Backend submodule
│   └── .git/           # Backend git
└── frontend/            # Frontend submodule
    └── .git/           # Frontend git
```

---

## Cache & Temporary Files

**Ignored by Git:**
```
backend/venv/                    # Python virtual environment
backend/__pycache__/             # Python cache
backend/db.sqlite3               # Database (optional)
frontend/node_modules/           # Node packages
frontend/build/                  # Production build
~/.cache/huggingface/           # ML model cache
```

---

## Port Configuration

```
Backend:  8000  (Django development server)
Frontend: 3000  (React development server)
```

---

## Security Notes

- CORS enabled for localhost:3000
- SQLite for development only
- No authentication (add for production)
- API rate limiting not implemented
- Input validation in serializers

---

## Performance Considerations

- First ML prediction: 30-60 seconds (model loading)
- Subsequent predictions: <1 second
- Model cached in memory after first load
- Database queries optimized with indexes
- Frontend uses React.memo for optimization

---

## Future Enhancements

- [ ] User authentication
- [ ] PostgreSQL for production
- [ ] API rate limiting
- [ ] Batch analysis
- [ ] Export results (CSV/PDF)
- [ ] More languages support
- [ ] Real-time WebSocket updates
- [ ] Docker containerization

---

**Last Updated:** 2025
