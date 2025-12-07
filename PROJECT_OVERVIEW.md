# 🎬 Bangla Movie Review Sentiment Analysis - Project Overview

## 📌 Project Summary

A full-stack web application that analyzes Bangla movie reviews using AI and provides explainable results showing which words influenced the sentiment prediction.

**Key Innovation**: Explainable AI (XAI) for Bangla sentiment analysis - showing transparency in AI decision-making.

---

## 🎯 Features

### Core Features
- ✅ **Real-time Sentiment Analysis** - Instant analysis of Bangla/English reviews
- ✅ **Explainable AI** - Visual word importance highlighting
- ✅ **Analysis History** - Automatic storage of all analyses
- ✅ **Modern UI** - Professional, responsive design
- ✅ **Bilingual Support** - Works with Bangla and English

### Technical Features
- ✅ RESTful API architecture
- ✅ SQLite database for persistence
- ✅ LIME (Local Interpretable Model-agnostic Explanations)
- ✅ Multilingual BERT model
- ✅ Component-based React architecture
- ✅ CORS-enabled API

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Browser                          │
│                  (http://localhost:3000)                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ HTTP Requests
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  React Frontend                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Components:                                      │  │
│  │  - AnalyzerForm (input)                          │  │
│  │  - ResultDisplay (visualization)                 │  │
│  │  - HistoryPanel (past analyses)                  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ REST API Calls
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Django REST Framework                       │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Endpoints:                                       │  │
│  │  POST /api/sentiment/analyze/                    │  │
│  │  GET  /api/sentiment/history/                    │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Model Inference
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  ML Service Layer                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │  - BERT Model (sentiment prediction)             │  │
│  │  - LIME Explainer (word importance)              │  │
│  │  - Visualization Generator                       │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Data Persistence
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  SQLite Database                         │
│  - SentimentAnalysis table                              │
│  - Stores: text, sentiment, confidence, words, timestamp│
└─────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
movieReview/
│
├── backend/                    # Django REST API
│   ├── config/                # Django configuration
│   │   ├── settings.py       # App settings, CORS, DB
│   │   ├── urls.py           # Main URL routing
│   │   └── wsgi.py           # WSGI config
│   │
│   ├── sentiment_api/         # Main application
│   │   ├── models.py         # Database models
│   │   ├── serializers.py    # API serializers
│   │   ├── views.py          # API endpoints
│   │   ├── ml_service.py     # ML model integration
│   │   ├── urls.py           # App URL routing
│   │   └── admin.py          # Admin panel config
│   │
│   ├── manage.py             # Django CLI
│   └── requirements.txt      # Python dependencies
│
├── frontend/                  # React Application
│   ├── public/               # Static files
│   │   └── index.html       # HTML template
│   │
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── AnalyzerForm.js      # Input form
│   │   │   ├── ResultDisplay.js     # Results view
│   │   │   └── HistoryPanel.js      # History sidebar
│   │   │
│   │   ├── services/         # API integration
│   │   │   └── api.js       # API calls
│   │   │
│   │   ├── App.js           # Main component
│   │   ├── App.css          # Main styles
│   │   ├── index.js         # Entry point
│   │   └── index.css        # Global styles
│   │
│   └── package.json          # Node dependencies
│
├── ml_model/                  # ML Documentation
│   └── README.md             # Model info
│
├── README.md                  # Project overview
├── SETUP_GUIDE.md            # Detailed setup
├── QUICK_START.md            # Quick start guide
├── API_DOCUMENTATION.md      # API reference
├── start_backend.bat         # Backend launcher
└── start_frontend.bat        # Frontend launcher
```

---

## 🔧 Technology Stack

### Backend
- **Framework**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Database**: SQLite (development)
- **ML Framework**: PyTorch 2.1.1
- **NLP**: Transformers 4.35.2 (HuggingFace)
- **Explainability**: LIME 0.2.0.1
- **CORS**: django-cors-headers 4.3.1

### Frontend
- **Framework**: React 18.2.0
- **HTTP Client**: Axios 1.6.2
- **Icons**: Lucide React 0.294.0
- **Styling**: Custom CSS (Tailwind-inspired)
- **Build Tool**: React Scripts 5.0.1

### ML Model
- **Model**: nlptown/bert-base-multilingual-uncased-sentiment
- **Type**: Multilingual BERT (supports Bangla)
- **Task**: 5-star sentiment classification
- **Size**: ~500MB (downloaded on first run)

---

## 🚀 How It Works

### 1. User Input
User enters a Bangla movie review in the text area.

### 2. API Request
Frontend sends POST request to `/api/sentiment/analyze/` with review text.

### 3. ML Processing
Backend:
1. Loads BERT model (cached after first load)
2. Predicts sentiment (Positive/Negative/Neutral)
3. Calculates confidence score
4. Uses LIME to find important words
5. Generates color-coded visualization

### 4. Database Storage
Analysis is saved to SQLite database with:
- Review text
- Sentiment result
- Confidence score
- Word importance data
- Timestamp

### 5. Response
Backend returns JSON with:
- Sentiment classification
- Confidence percentage
- Word importance scores
- Visualization data

### 6. Display
Frontend displays:
- Sentiment badge with icon
- Confidence meter
- Color-coded words (green=positive, red=negative)
- Importance scores table
- Updates history panel

---

## 📊 Data Flow

```
User Input → React Form → Axios POST → Django View → ML Service
                                                          ↓
                                                    BERT Model
                                                          ↓
                                                   LIME Explainer
                                                          ↓
User Display ← React Components ← JSON Response ← Django Serializer
                                                          ↓
                                                    SQLite Database
```

---

## 🎨 UI/UX Design

### Color Scheme
- **Primary**: Purple gradient (#667eea → #764ba2)
- **Positive**: Green (#10b981)
- **Negative**: Red (#ef4444)
- **Neutral**: Orange (#f59e0b)
- **Background**: White cards on gradient background

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: 600-700 weight
- **Body**: 400-500 weight

### Components
- **Cards**: Rounded corners (16px), shadow effects
- **Buttons**: Gradient backgrounds, hover animations
- **Inputs**: Border focus effects, smooth transitions
- **Badges**: Color-coded, rounded pills

---

## 🔐 Security Considerations

### Current (Development)
- ✅ CORS enabled for localhost
- ✅ Django CSRF protection
- ⚠️ Debug mode ON
- ⚠️ Default SECRET_KEY

### For Production
- 🔒 Change SECRET_KEY
- 🔒 Set DEBUG = False
- 🔒 Use environment variables
- 🔒 Add authentication
- 🔒 Use PostgreSQL
- 🔒 Add rate limiting
- 🔒 Enable HTTPS
- 🔒 Add input validation

---

## 📈 Performance

### First Analysis
- **Time**: 10-20 seconds
- **Reason**: Model loading (~500MB)
- **One-time**: Cached after first load

### Subsequent Analyses
- **Time**: 2-5 seconds
- **CPU**: ~100% during analysis
- **Memory**: ~2GB RAM

### Optimization Tips
- Use GPU for 5-10x speedup
- Reduce LIME samples (currently 100)
- Implement model caching
- Add Redis for session storage

---

## 🎓 Academic Value

### Research Contributions
1. **Explainable AI for Bangla** - Few researchers have done this
2. **Transparency** - Shows AI decision-making process
3. **Practical Application** - Real-world usable system
4. **Full-Stack Implementation** - Complete end-to-end solution

### Thesis Highlights
- Novel application of LIME to Bangla text
- Comparison with black-box models
- User study on explainability value
- Performance benchmarks
- Scalability analysis

---

## 🔮 Future Enhancements

### Short-term
- [ ] User authentication
- [ ] Export results to PDF/CSV
- [ ] Batch analysis (upload CSV)
- [ ] More visualization options
- [ ] Mobile responsive improvements

### Medium-term
- [ ] Train custom Bangla model
- [ ] Add more sentiment categories
- [ ] Implement caching (Redis)
- [ ] Add API rate limiting
- [ ] Deploy to cloud

### Long-term
- [ ] Multi-language support
- [ ] Real-time streaming analysis
- [ ] Sentiment trends dashboard
- [ ] Compare multiple reviews
- [ ] Integration with movie databases

---

## 📚 Documentation Files

- **README.md** - Project overview
- **QUICK_START.md** - Fast setup guide
- **SETUP_GUIDE.md** - Detailed installation
- **API_DOCUMENTATION.md** - API reference
- **PROJECT_OVERVIEW.md** - This file

---

## 🤝 Contributing

This is an academic project. For improvements:
1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

---

## 📄 License

MIT License - Free for academic and research use.

---

## 👨‍💻 Development

### Running Tests
```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

### Code Style
- **Python**: PEP 8
- **JavaScript**: ESLint (React)
- **CSS**: BEM-like naming

### Git Workflow
- Main repo: Overall project
- Backend repo: Django code
- Frontend repo: React code
- ML Model repo: Model documentation

---

## 📞 Support

For issues or questions:
1. Check documentation files
2. Review error messages
3. Check browser console
4. Verify both servers are running
5. Test API endpoints directly

---

**Built with ❤️ for academic research in Bangla NLP and Explainable AI**
