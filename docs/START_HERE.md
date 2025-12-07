# 🎬 সিনেমা রিভিউ পরীক্ষক - Quick Start Guide

> **👋 Welcome!** This guide will help you run the project in 5 minutes.

---

## ⚡ Super Quick Start

### Option A: With Git (3 Commands)
```bash
# 1. Clone the repository
git clone https://github.com/alphapie77/BanglaMovieReviewer.git
cd BanglaMovieReviewer

# 2. Run everything
run_all.bat

# 3. Open browser
# http://localhost:3000
```

### Option B: Download ZIP (No Git Required)
1. **Download**: Go to https://github.com/alphapie77/BanglaMovieReviewer
2. **Extract**: Click "Code" → "Download ZIP" → Extract folder
3. **Open Terminal**: Right-click extracted folder → "Open in Terminal" or "Command Prompt here"
4. **Run**: Type `run_all.bat` and press Enter
5. **Browse**: Open http://localhost:3000

**That's it!** ✅ The application will:
- Install all dependencies automatically
- Download ML model (~500MB, first time only)
- Start both backend and frontend servers
- Open in your browser

---

## 💻 What You Need

### Required Software
```
✓ Python 3.8+     (Download: https://python.org)
✓ Node.js 16+     (Download: https://nodejs.org)
✓ Git             (Download: https://git-scm.com)
```

### System Requirements
```
✓ RAM: 4GB minimum (8GB recommended)
✓ Disk: 2GB free space
✓ Internet: Required for first run
✓ OS: Windows 10/11, Mac, or Linux
```

---

## 🚀 Step-by-Step Guide

### Step 1: Check Prerequisites
```bash
# Check Python
python --version
# Should show: Python 3.8.x or higher

# Check Node.js
node --version
# Should show: v16.x.x or higher

# Check Git
git --version
# Should show: git version 2.x.x
```

### Step 2: Get the Code

**Method 1: Clone with Git (Recommended)**
```bash
git clone https://github.com/alphapie77/BanglaMovieReviewer.git
cd BanglaMovieReviewer
```

**Method 2: Download ZIP (No Git Required)**
1. Visit: https://github.com/alphapie77/BanglaMovieReviewer
2. Click green "Code" button
3. Select "Download ZIP"
4. Extract the downloaded file
5. Navigate to extracted folder in terminal:
   ```bash
   cd path/to/BanglaMovieReviewer
   ```

### Step 3: Run Application

**Option A: Automatic (Recommended)**
```bash
run_all.bat    # Windows
```

**Option B: Manual**
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

### Step 4: Access Application
```
Frontend:  http://localhost:3000
Backend:   http://localhost:8000
API Docs:  http://localhost:8000/api/sentiment/
```

---

## 🎯 How to Use

### 1. Go to Analyzer Page
- Click "Analyzer" in navigation menu
- Or go directly to: http://localhost:3000/analyzer

### 2. Enter Review
```
Example (Positive):
এই সিনেমাটি অসাধারণ ছিল! অভিনয় এবং গল্প দুটোই চমৎকার।

Example (Negative):
বিরক্তিকর সিনেমা, গল্প একদম দুর্বল।
```

### 3. Click "বিশ্লেষণ করুন"
- First analysis takes 30-60 seconds (model loading)
- Subsequent analyses are instant

### 4. View Results
- Sentiment: Positive/Negative/Neutral
- Confidence: Percentage score
- Charts: Visual representation
- Word Analysis: Color-coded importance

---

## 🐛 Common Issues

### Issue 1: "Backend not running"
```bash
cd backend
python test_model.py    # Test if model works
python manage.py runserver
```

### Issue 2: "Port already in use"
```bash
# Kill port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Issue 3: "Module not found"
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 4: "npm install fails"
```bash
cd frontend
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

---

## 📚 More Documentation

| Document | When to Read |
|----------|-------------|
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | Detailed installation steps |
| **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** | Building with the API |
| **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** | When something breaks |
| **[QUICK_FIX.md](QUICK_FIX.md)** | ML model issues |
| **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** | Understanding project organization |

---

## 🛠️ Useful Scripts

```bash
run_all.bat           # Start everything
start_backend.bat     # Backend only
start_frontend.bat    # Frontend only
restart_backend.bat   # Restart backend
clean_all.bat         # Clean caches
```

---

## 👨💻 Tech Stack

**Backend**
- Django 4.2.7 (Web framework)
- Django REST Framework (API)
- PyTorch (ML framework)
- Transformers (BERT model)
- LIME (Explainability)

**Frontend**
- React 18.2.0 (UI framework)
- React Router (Navigation)
- Recharts (Data visualization)
- Axios (HTTP client)
- Lucide React (Icons)

**Database**
- SQLite (Development)

---

## ❓ Need Help?

1. Check **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)**
2. Run test scripts:
   ```bash
   cd backend
   python test_model.py
   python test_api.py
   ```
3. Check backend terminal for error messages
4. Check browser console (F12) for frontend errors

---

**Happy Analyzing! 🎉**
