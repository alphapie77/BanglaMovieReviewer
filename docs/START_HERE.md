# 🚀 START HERE - Quick Start Guide

## Welcome to Bangla Movie Reviewer!

This guide will get you up and running in 5 minutes.

---

## ⚡ Super Quick Start

```bash
# 1. Clone repository
git clone <your-repo-url>
cd BanglaMovieReviewer

# 2. Run this ONE command
.\start.bat

# 3. Wait 30 seconds
# 4. Browser opens at http://localhost:3000
# 5. Done! 🎉
```

---

## 🎯 What You Get

### 6 ML Models:
- 🇧🇩 **BanglaBERT** - Best for Bangla
- 🌍 **mBERT** - Multilingual
- 🧠 **CNN** - Fast neural network
- 🔄 **Masked_LSTM** - Recurrent network
- ⚡ **LightGBM** - Very fast
- 📊 **Logistic_Regression** - Baseline

### Features:
- ✨ Beautiful UI with custom dropdown
- 📊 Sentiment analysis (Positive/Negative/Neutral)
- 💯 Confidence scores
- 🎨 Word highlighting
- 📈 Word importance
- 📜 Analysis history

---

## 📋 First Time Setup

### Prerequisites:
- Python 3.8+
- Node.js 14+
- 4GB RAM
- Internet connection

### Installation:

```bash
# Full setup (first time only)
.\run_all.bat
```

This will:
1. Create Python virtual environment
2. Install all dependencies (10-15 min)
3. Run database migrations
4. Start backend server
5. Install frontend dependencies
6. Start frontend server
7. Open browser

---

## 🎮 How to Use

### Step 1: Start Application
```bash
.\start.bat
```

### Step 2: Open Browser
Goes to: http://localhost:3000

### Step 3: Select Model
Click dropdown → Choose from 6 models

### Step 4: Enter Review
Type Bangla movie review (max 5000 characters)

### Step 5: Analyze
Click "বিশ্লেষণ করুন" button

### Step 6: View Results
- Sentiment classification
- Confidence percentage
- Word highlighting
- Importance scores

---

## 🌐 Models from Hugging Face

All models automatically download from Hugging Face:
- No large files in repository
- First use: 2-3 minutes per model
- Cached after first download
- Works anywhere with internet

**Your Models:**
- `shksabbir7/bangla-movie-sentiment-banglabert`
- `shksabbir7/bangla-movie-sentiment-mbert`
- `shksabbir7/bangla-movie-sentiment-cnn`
- `shksabbir7/bangla-movie-sentiment-lstm`
- `shksabbir7/bangla-movie-sentiment-lightgbm`
- `shksabbir7/bangla-movie-sentiment-logreg`

---

## 🧪 Testing

```bash
cd backend
call venv\Scripts\activate.bat
python auto_test.py
```

**Expected:** 7/7 tests pass ✅

---

## 🛑 Stopping

Close both terminal windows:
- Backend Server
- Frontend Server

---

## 📚 Next Steps

### Learn More:
- **[README.md](../README.md)** - Project overview
- **[PROJECT_DOCUMENTATION.md](../PROJECT_DOCUMENTATION.md)** - Complete docs
- **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** - API reference
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues

### Explore Code:
- `backend/sentiment_api/ml_service.py` - Model loading
- `frontend/src/components/AnalyzerForm.js` - Custom dropdown
- `backend/sentiment_api/views.py` - API endpoints

---

## ⚠️ Common Issues

### Backend won't start:
```bash
cd backend
call venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
```

### Frontend won't start:
```bash
cd frontend
npm install
npm start
```

### Port already in use:
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**More solutions:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 🎉 That's It!

You're ready to analyze Bangla movie reviews!

**Questions?** Check other docs in `docs/` folder.

**Happy Analyzing! 🎬🇧🇩**
