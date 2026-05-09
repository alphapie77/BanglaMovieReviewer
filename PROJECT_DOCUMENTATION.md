# 🎬 Bangla Movie Reviewer - Complete Documentation

## 📁 Project Structure

```
BanglaMovieReviewer/
│
├── 📂 backend/                      # Django Backend
│   ├── 📂 config/                   # Django Configuration
│   │   ├── settings.py             # Project settings
│   │   ├── urls.py                 # URL routing
│   │   └── wsgi.py                 # WSGI config
│   │
│   ├── 📂 sentiment_api/            # Main API App
│   │   ├── ml_service.py           # ⭐ Model loading & prediction
│   │   ├── views.py                # API endpoints
│   │   ├── models.py               # Database models
│   │   ├── serializers.py          # Data serialization
│   │   └── urls.py                 # API routes
│   │
│   ├── requirements.txt            # Python dependencies
│   ├── manage.py                   # Django management
│   ├── auto_test.py                # ⭐ Automated testing
│   └── db.sqlite3                  # SQLite database
│
├── 📂 frontend/                     # React Frontend
│   ├── 📂 src/
│   │   ├── 📂 components/          # React Components
│   │   │   ├── AnalyzerForm.js    # ⭐ Model dropdown & input
│   │   │   ├── AnalyzerForm.css   # ⭐ Custom dropdown styling
│   │   │   ├── ResultDisplay.js   # Results display
│   │   │   └── HistoryPanel.js    # History panel
│   │   │
│   │   ├── 📂 pages/               # Page Components
│   │   │   ├── Home.js            # Landing page
│   │   │   ├── Analyzer.js        # Analysis page
│   │   │   ├── Result.js          # Result page
│   │   │   └── History.js         # History page
│   │   │
│   │   ├── 📂 services/            # API Services
│   │   │   └── api.js             # ⭐ API calls to backend
│   │   │
│   │   ├── App.js                 # Main app component
│   │   └── index.js               # Entry point
│   │
│   ├── package.json               # Node dependencies
│   └── public/                    # Static files
│
├── 📂 docs/                        # Documentation
│   ├── API_DOCUMENTATION.md       # API reference
│   ├── API_MODEL_SELECTION.md     # Model selection API
│   ├── DEPLOYMENT.md              # Deployment guide
│   ├── PROJECT_STRUCTURE.md       # Project structure
│   ├── SETUP_GUIDE.md             # Setup instructions
│   ├── START_HERE.md              # Quick start
│   └── TROUBLESHOOTING.md         # Common issues
│
├── 📂 screenshots/                 # UI Screenshots
│   ├── home.jpeg
│   ├── analyzer.jpeg
│   ├── pos.jpeg
│   └── neg.jpeg
│
├── 🚀 Scripts (Windows .bat files)
│   ├── start.bat                  # ⭐ Quick start (recommended)
│   ├── run_all.bat                # Full setup + start
│   ├── start_backend.bat          # Backend only
│   ├── start_frontend.bat         # Frontend only
│   └── test_with_setup.bat        # Setup + test
│
├── 📄 Root Files
│   ├── README.md                  # Main readme
│   ├── SETUP_GUIDE.md             # Complete setup guide
│   ├── .gitignore                 # Git ignore rules
│   └── .gitattributes             # Git attributes
│
└── ⚠️ EXCLUDED: best2_models_per_family/  # Local models (not needed)
```

---

## 🔑 Key Files Explained

### Backend Core Files:

#### 1. **`backend/sentiment_api/ml_service.py`** ⭐⭐⭐
**Purpose:** Model loading and prediction logic

**Key Features:**
- Loads 6 models from Hugging Face
- Handles Transformer, Keras, and Sklearn models
- Preprocessing for different model types
- LIME explainer for word importance
- Unicode error handling

**Models Configuration:**
```python
MODEL_CONFIGS = {
    'BanglaBERT': 'shksabbir7/bangla-movie-sentiment-banglabert',
    'mBERT': 'shksabbir7/bangla-movie-sentiment-mbert',
    'CNN': 'shksabbir7/bangla-movie-sentiment-cnn',
    'Masked_LSTM': 'shksabbir7/bangla-movie-sentiment-lstm',
    'LightGBM': 'shksabbir7/bangla-movie-sentiment-lightgbm',
    'Logistic_Regression': 'shksabbir7/bangla-movie-sentiment-logreg'
}
```

#### 2. **`backend/sentiment_api/views.py`** ⭐⭐
**Purpose:** API endpoints

**Endpoints:**
- `GET /api/sentiment/models/` - List available models
- `POST /api/sentiment/analyze/` - Analyze sentiment
- `GET /api/sentiment/history/` - Get analysis history

**Validation:**
- Model name validation
- Text length limit (5000 chars)
- Empty text check
- Error handling

#### 3. **`backend/requirements.txt`** ⭐
**Purpose:** Python dependencies

**Key Dependencies:**
```
Django==4.2.7
djangorestframework==3.14.0
transformers>=4.40.0
tensorflow>=2.13.0
torch>=2.0.0
lightgbm>=4.0.0
huggingface-hub>=0.20.0  # ⭐ For model download
```

#### 4. **`backend/auto_test.py`** ⭐
**Purpose:** Automated API testing

**Tests:**
- Backend connection
- Model availability (6 models)
- Valid analysis
- Empty text validation
- Invalid model validation
- Long text validation
- Special characters
- All models working

---

### Frontend Core Files:

#### 1. **`frontend/src/components/AnalyzerForm.js`** ⭐⭐⭐
**Purpose:** Main analysis form with model dropdown

**Key Features:**
- Custom dropdown with 6 models
- Model-specific icons (🇧🇩 🌍 🧠 🔄 ⚡ 📊)
- Character counter (0/5000)
- Input validation
- Loading states
- Outside click handler

**Model Icons:**
```javascript
const icons = {
  'BanglaBERT': '🇧🇩',
  'mBERT': '🌍',
  'CNN': '🧠',
  'Masked_LSTM': '🔄',
  'LightGBM': '⚡',
  'Logistic_Regression': '📊'
};
```

#### 2. **`frontend/src/components/AnalyzerForm.css`** ⭐⭐
**Purpose:** Custom dropdown styling

**Key Styles:**
- Gradient background (purple theme)
- Hover effects
- Active state highlighting
- Smooth animations
- Custom scrollbar
- Responsive design

#### 3. **`frontend/src/services/api.js`** ⭐
**Purpose:** API communication

**Functions:**
```javascript
getModels()                          // Get available models
analyzeSentiment(text, modelName)    // Analyze sentiment
getHistory()                         // Get history
```

#### 4. **`frontend/package.json`**
**Purpose:** Node dependencies

**Key Dependencies:**
```json
{
  "react": "^18.2.0",
  "axios": "^1.6.0",
  "lucide-react": "^0.263.1",
  "react-router-dom": "^6.16.0"
}
```

---

## 🚀 Scripts Guide

### 1. **`start.bat`** ⭐ RECOMMENDED
**Use:** Daily usage (after first setup)

**What it does:**
- Starts backend server
- Starts frontend server
- Opens browser

**Command:**
```bash
.\start.bat
```

**Time:** 30 seconds

---

### 2. **`run_all.bat`**
**Use:** First time setup

**What it does:**
- Creates virtual environment
- Installs all dependencies
- Runs migrations
- Starts both servers

**Command:**
```bash
.\run_all.bat
```

**Time:** 10-15 minutes (first run)

---

### 3. **`start_backend.bat`**
**Use:** Backend only

**Command:**
```bash
.\start_backend.bat
```

---

### 4. **`start_frontend.bat`**
**Use:** Frontend only

**Command:**
```bash
.\start_frontend.bat
```

---

### 5. **`test_with_setup.bat`**
**Use:** Setup + automated testing

**Command:**
```bash
.\test_with_setup.bat
```

---

## 📚 Documentation Files

### 1. **`docs/API_DOCUMENTATION.md`**
Complete API reference with examples

### 2. **`docs/API_MODEL_SELECTION.md`**
Model selection feature documentation

### 3. **`docs/DEPLOYMENT.md`**
Deployment guide for production

### 4. **`docs/SETUP_GUIDE.md`**
Detailed setup instructions

### 5. **`docs/TROUBLESHOOTING.md`**
Common issues and solutions

### 6. **`SETUP_GUIDE.md`** (Root)
Quick setup guide

---

## 🎯 Quick Start Guide

### For First Time:
```bash
# 1. Clone repository
git clone <your-repo>
cd BanglaMovieReviewer

# 2. Run setup script
.\run_all.bat

# 3. Wait for setup (10-15 min)
# 4. Browser opens automatically
```

### For Daily Use:
```bash
# Just start servers
.\start.bat

# Wait 30 seconds
# Browser opens at http://localhost:3000
```

---

## 🔧 Configuration Files

### Backend Configuration:

**`backend/config/settings.py`**
- Django settings
- Database config
- CORS settings
- Installed apps

**`backend/config/urls.py`**
- URL routing
- API endpoints

### Frontend Configuration:

**`frontend/package.json`**
- Dependencies
- Scripts
- Proxy settings

**`frontend/src/App.js`**
- Routing
- Main layout

---

## 🗄️ Database

**File:** `backend/db.sqlite3`

**Models:**
- SentimentAnalysis
  - review_text (CharField)
  - sentiment (CharField)
  - confidence (FloatField)
  - word_importance (JSONField)
  - created_at (DateTimeField)

---

## 🌐 API Endpoints

### Base URL: `http://localhost:8000/api/sentiment`

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/models/` | List 6 models |
| POST | `/analyze/` | Analyze sentiment |
| GET | `/history/` | Get history |

---

## 🎨 UI Components

### Pages:
1. **Home** - Landing page
2. **Analyzer** - Main analysis page
3. **Result** - Results display
4. **History** - Analysis history
5. **About** - About page

### Components:
1. **AnalyzerForm** - Input form with dropdown
2. **ResultDisplay** - Sentiment results
3. **HistoryPanel** - History list

---

## 📦 Dependencies Summary

### Backend (Python):
- Django 4.2.7
- Django REST Framework
- Transformers (Hugging Face)
- TensorFlow 2.13+
- PyTorch 2.0+
- LightGBM 4.0+
- Scikit-learn 1.3+
- Hugging Face Hub 0.20+

### Frontend (Node):
- React 18.2
- Axios 1.6
- Lucide React 0.263
- React Router 6.16

---

## 🚫 Files to Ignore (.gitignore)

### Backend:
```
venv/
__pycache__/
*.pyc
db.sqlite3
*.log
```

### Frontend:
```
node_modules/
build/
.env
```

### Root:
```
best2_models_per_family/  # ⭐ Local models not needed
```

---

## 🔗 Hugging Face Models

All models hosted at:
- https://huggingface.co/shksabbir7/bangla-movie-sentiment-banglabert
- https://huggingface.co/shksabbir7/bangla-movie-sentiment-mbert
- https://huggingface.co/shksabbir7/bangla-movie-sentiment-cnn
- https://huggingface.co/shksabbir7/bangla-movie-sentiment-lstm
- https://huggingface.co/shksabbir7/bangla-movie-sentiment-lightgbm
- https://huggingface.co/shksabbir7/bangla-movie-sentiment-logreg

**Benefits:**
- ✅ No large files in GitHub
- ✅ Automatic download on first use
- ✅ Cached locally after download
- ✅ Easy deployment

---

## 📊 Testing

### Automated Tests:
```bash
cd backend
call venv\Scripts\activate.bat
python auto_test.py
```

**Expected:** 7/7 tests pass

### Manual Testing:
1. Open http://localhost:3000
2. Select model from dropdown
3. Enter Bangla text
4. Click analyze
5. Check results

---

## 🎓 Learning Resources

### Key Concepts:
- Django REST Framework
- React Hooks (useState, useEffect)
- Hugging Face Transformers
- Custom CSS Dropdowns
- API Integration

### Files to Study:
1. `ml_service.py` - Model loading
2. `AnalyzerForm.js` - Custom dropdown
3. `views.py` - API endpoints
4. `api.js` - Frontend API calls

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Update documentation
6. Submit pull request

---

## 📝 License

MIT License - Free to use

---

## 👨‍💻 Author

**Hugging Face:** shksabbir7
**GitHub:** [Your GitHub]
**Email:** [Your Email]

---

## 🎉 Summary

**Total Files:** ~50 files
**Key Files:** 10 core files
**Scripts:** 5 batch scripts
**Documentation:** 8 docs
**Models:** 6 ML models (Hugging Face)

**Quick Start:** `.\start.bat`
**Full Setup:** `.\run_all.bat`
**Testing:** `python auto_test.py`

**That's it! Everything organized and documented!** 🚀
