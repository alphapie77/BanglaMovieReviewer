# 🎬 Bangla Movie Review Sentiment Analysis - Full Stack

A full-stack web application for Bangla movie review sentiment analysis with Explainable AI.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2.7-green.svg)
![React](https://img.shields.io/badge/react-18.2.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 🚀 Quick Start

```bash
run_all.bat    # Starts both servers
```
Then open: **http://localhost:3000**

See **[START_HERE.md](START_HERE.md)** for details.

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
├── backend/          # Django REST API + ML
├── frontend/         # React Application
├── ml_model/         # ML Documentation
├── START_HERE.md     # 👈 Start here!
├── SETUP_GUIDE.md    # Detailed setup
└── API_DOCUMENTATION.md  # API reference
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

See **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** for details.

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

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git
- 4GB+ RAM

### Installation

**Option 1: Quick Start (Windows)**
```bash
start_backend.bat    # Terminal 1
start_frontend.bat   # Terminal 2
```

**Option 2: Manual Setup**
```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (new terminal)
cd frontend
npm install
npm start
```

### First Run
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- Admin: http://localhost:8000/admin

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| **[START_HERE.md](START_HERE.md)** | 👈 Quick start guide |
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | Detailed installation |
| **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** | API reference |

---



---

## 🐛 Troubleshooting

```bash
clean_all.bat    # Clean everything
build_all.bat    # Rebuild
run_all.bat      # Start
```

---



---



---



---



---



---

---

**Built for Bangla NLP and Explainable AI research**
