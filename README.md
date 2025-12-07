# 🎬 সিনেমা রিভিউ পরীক্ষক | Bangla Movie Review Sentiment Analyzer

A modern full-stack web application for analyzing Bangla movie reviews with AI-powered sentiment detection and explainability features.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2.7-green.svg)
![React](https://img.shields.io/badge/react-18.2.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 🚀 Quick Start (3 Steps)

### Step 1: Clone Repository
```bash
git clone <your-repo-url>
cd movieReview
```

### Step 2: Run Application
```bash
run_all.bat    # Windows (starts both servers automatically)
```

### Step 3: Open Browser
```
http://localhost:3000
```

**First time?** Model will download automatically (~500MB, takes 2-5 minutes). See **[docs/START_HERE.md](docs/START_HERE.md)** for detailed setup.

---

## ✨ Features

- 🎯 **Real-time Sentiment Analysis** - Instant Positive/Negative/Neutral classification
- 🔍 **Explainable AI** - Visual word importance highlighting with LIME
- 📊 **Analysis History** - Automatic storage of all analyses in SQLite
- 🎨 **Modern UI** - Professional, responsive design with gradient themes
- 🌐 **Bilingual Support** - Works with both Bangla and English text
- 📈 **Confidence Scores** - Shows prediction confidence percentage
- 🎨 **Color-Coded Words** - Green (positive), Red (negative), Gray (neutral)

---

## 🏗️ Architecture

```
┌─────────────┐      REST API      ┌──────────────┐      ML Model      ┌─────────────┐
│   React     │ ◄─────────────────► │   Django     │ ◄─────────────────► │    BERT     │
│  Frontend   │   JSON (Axios)      │   Backend    │   Transformers     │   + LIME    │
└─────────────┘                     └──────────────┘                     └─────────────┘
                                           │
                                           ▼
                                    ┌──────────────┐
                                    │   SQLite     │
                                    │   Database   │
                                    └──────────────┘
```

---

## 📁 Project Structure

```
movieReview/
├── backend/                    # Django REST API + ML Model
│   ├── config/                 # Django settings
│   ├── sentiment_api/          # Main API app
│   ├── requirements.txt        # Python dependencies
│   ├── test_model.py           # ML model test
│   └── test_api.py             # API test
│
├── frontend/                   # React Application
│   ├── src/
│   │   ├── pages/              # Main pages (Home, Analyzer, Result, etc.)
│   │   ├── components/         # Reusable components
│   │   ├── services/           # API integration
│   │   └── App.js              # Router setup
│   └── package.json            # Node dependencies
│
├── docs/                       # 📚 Documentation
│   ├── START_HERE.md           # Quick start guide
│   ├── SETUP_GUIDE.md          # Detailed installation
│   ├── API_DOCUMENTATION.md    # API reference
│   ├── TROUBLESHOOTING.md      # Common issues
│   ├── QUICK_FIX.md            # ML model fixes
│   └── PROJECT_STRUCTURE.md    # Complete structure
│
├── ml_model/                   # ML model documentation
├── *.bat                       # Windows scripts
└── README.md                   # This file
```

---

## 🔧 Technology Stack

### Backend
- **Framework**: Django 4.2.7 + Django REST Framework 3.14.0
- **Database**: SQLite (development)
- **ML**: PyTorch 2.1.1 + Transformers 4.35.2
- **Explainability**: LIME 0.2.0.1
- **Model**: nlptown/bert-base-multilingual-uncased-sentiment

### Frontend
- **Framework**: React 18.2.0
- **HTTP Client**: Axios 1.6.2
- **Icons**: Lucide React 0.294.0
- **Styling**: Custom CSS (Tailwind-inspired)

---

## 📊 How It Works

1. **User Input** → Enter Bangla movie review
2. **API Request** → Frontend sends POST to Django
3. **ML Processing** → BERT predicts sentiment + LIME explains
4. **Database** → Save analysis to SQLite
5. **Response** → Return sentiment, confidence, word importance
6. **Visualization** → Display color-coded results

---

## 🎯 API Endpoints

```bash
POST /api/sentiment/analyze/   # Analyze sentiment
GET  /api/sentiment/history/   # Get last 20 analyses
GET  /api/sentiment/           # List all analyses
GET  /api/sentiment/{id}/      # Get specific analysis
```

See **[docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)** for details.

---

## 📸 Screenshots

### Main Interface
- Modern gradient header with Bangla title
- Large text area for review input
- Example reviews for quick testing
- Real-time analysis with loading states

### Results Display
- Sentiment badge with icon (😊/☹️/😐)
- Confidence percentage with progress indicator
- Color-coded word visualization
- Word importance table with scores
- Legend explaining color meanings

### History Panel
- Chronological list of past analyses
- Sentiment badges and confidence scores
- Truncated review text preview
- Timestamps in Bangla format

---

## 🎓 Academic Value

### Research Contributions
1. **Explainable AI for Bangla** - Novel application of LIME to Bangla text
2. **Transparency** - Shows AI decision-making process
3. **Full-Stack Implementation** - Complete end-to-end solution
4. **Practical Application** - Real-world usable system

### Thesis Highlights
- Comparison with black-box models
- User study on explainability value
- Performance benchmarks
- Scalability analysis

---

## 🚀 Installation Guide

### Prerequisites
```
✓ Python 3.8 or higher
✓ Node.js 16 or higher  
✓ Git
✓ 4GB+ RAM (for ML model)
✓ 2GB+ free disk space
✓ Internet connection (first run only)
```

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
# Clone repository
git clone <your-repo-url>
cd movieReview

# Run everything
run_all.bat
```

**Manual (if batch files don't work):**
```bash
# Terminal 1 - Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Terminal 2 - Frontend
cd frontend
npm install
npm start
```

### Option 2: Step-by-Step Setup

**1. Backend Setup**
```bash
cd backend
python -m venv venv
venv\Scripts\activate              # Windows
# source venv/bin/activate        # Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python test_model.py               # Test ML model (optional)
python manage.py runserver
```

**2. Frontend Setup (New Terminal)**
```bash
cd frontend
npm install
npm start
```

### Access Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api/sentiment/
- **Admin Panel**: http://localhost:8000/admin

### First Run Notes
- ML model downloads automatically (~500MB)
- Takes 2-5 minutes on first analysis
- Subsequent analyses are fast (<1 second)

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[docs/START_HERE.md](docs/START_HERE.md)** | 👈 **Start here!** Quick setup in 5 minutes |
| **[docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md)** | Detailed installation guide |
| **[docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)** | API endpoints & examples |
| **[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** | Common issues & solutions |
| **[docs/QUICK_FIX.md](docs/QUICK_FIX.md)** | ML model troubleshooting |
| **[docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)** | Complete project structure |

---



---

## 🐛 Troubleshooting

### Quick Fixes
```bash
clean_all.bat         # Clean all caches
restart_backend.bat   # Restart backend only
run_all.bat           # Fresh start
```

### Common Issues

**1. "বিশ্লেষণে ত্রুটি হয়েছে" Error**
```bash
cd backend
python test_model.py    # Check if model loads
python test_api.py      # Test API
```

**2. Backend Not Starting**
```bash
cd backend
venv\Scripts\activate
pip install --upgrade -r requirements.txt
python manage.py migrate
```

**3. Frontend Not Starting**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm start
```

**4. Port Already in Use**
```bash
# Kill process on port 8000 (backend)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Kill process on port 3000 (frontend)
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

See **[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** for more details.

---

## 🎯 Usage Examples

### Positive Review
```
এই সিনেমাটি অসাধারণ ছিল! অভিনয় এবং গল্প দুটোই চমৎকার।
→ Result: Positive (95% confidence)
```

### Negative Review  
```
বিরক্তিকর সিনেমা, গল্প একদম দুর্বল আর অভিনয়ও জোর করা মনে হয়েছে।
→ Result: Negative (95% confidence)
```

### Neutral Review
```
সিনেমাটি মোটামুটি ছিল, কিছু ভালো কিছু খারাপ।
→ Result: Neutral (70% confidence)
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built for Bangla NLP and Explainable AI research.

---

## 🙏 Acknowledgments

- **Model**: nlptown/bert-base-multilingual-uncased-sentiment
- **Explainability**: LIME (Local Interpretable Model-agnostic Explanations)
- **UI Icons**: Lucide React
- **Charts**: Recharts
