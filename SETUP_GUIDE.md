# 🚀 Complete Setup Guide

## Prerequisites

Before starting, make sure you have:

- ✅ Python 3.8 or higher
- ✅ Node.js 16 or higher
- ✅ Git
- ✅ 4GB+ RAM (for ML model)

## Step-by-Step Setup

### 1️⃣ Backend Setup (Django)

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies (this will take 5-10 minutes)
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Start backend server
python manage.py runserver
```

✅ Backend should now be running on: **http://localhost:8000**

### 2️⃣ Frontend Setup (React)

Open a NEW terminal window:

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies (this will take 2-3 minutes)
npm install

# Start frontend server
npm start
```

✅ Frontend should now be running on: **http://localhost:3000**

### 3️⃣ Test the Application

1. Open browser: http://localhost:3000
2. Type a Bangla movie review
3. Click "বিশ্লেষণ করুন" (Analyze)
4. Wait 10-20 seconds for first analysis (model loading)
5. See results with explainable AI!

## 🔧 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'django'`
**Solution**: Make sure virtual environment is activated

**Problem**: Model loading takes too long
**Solution**: First time downloads ~500MB model. Be patient!

**Problem**: CORS errors
**Solution**: Check that frontend is running on port 3000

### Frontend Issues

**Problem**: `npm install` fails
**Solution**: Delete `node_modules` and `package-lock.json`, try again

**Problem**: API connection failed
**Solution**: Make sure backend is running on port 8000

**Problem**: Blank page
**Solution**: Check browser console for errors

## 📊 Testing the API Directly

You can test the backend API using curl or Postman:

```bash
# Test analyze endpoint
curl -X POST http://localhost:8000/api/sentiment/analyze/ \
  -H "Content-Type: application/json" \
  -d "{\"review_text\": \"সিনেমাটা অসাধারণ ছিল\"}"

# Get history
curl http://localhost:8000/api/sentiment/history/
```

## 🎯 Next Steps

1. ✅ Test with different Bangla reviews
2. ✅ Check analysis history
3. ✅ View admin panel: http://localhost:8000/admin
4. ✅ Customize UI colors in CSS files
5. ✅ Train custom model for better accuracy

## 📁 Project Structure

```
movieReview/
├── backend/              # Django REST API
│   ├── config/          # Django settings
│   ├── sentiment_api/   # Main app
│   └── manage.py
├── frontend/            # React app
│   ├── src/
│   │   ├── components/  # UI components
│   │   └── services/    # API calls
│   └── package.json
└── ml_model/            # ML documentation
```

## 🔐 Security Notes

- Current SECRET_KEY is for development only
- Change it before deploying to production
- Add authentication if needed
- Use environment variables for sensitive data

## 📝 Git Repositories

Each section has its own Git repository:
- Main: `movieReview/.git`
- Backend: `movieReview/backend/.git`
- Frontend: `movieReview/frontend/.git`
- ML Model: `movieReview/ml_model/.git`

## 🎓 For Your Thesis

Key features to highlight:
1. **Explainable AI** - Shows which words influenced the decision
2. **Multilingual** - Works with Bangla and English
3. **Real-time** - Instant analysis
4. **History tracking** - Stores all analyses
5. **Modern UI** - Professional design

## 💡 Tips

- First analysis is slow (model loading) - this is normal
- Use GPU if available for 5-10x speed boost
- Keep both servers running while testing
- Check browser console for debugging

## 🆘 Need Help?

Common commands:

```bash
# Check Python version
python --version

# Check Node version
node --version

# Check if port is in use
# Windows:
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Kill process on port (Windows)
taskkill /PID <PID> /F
```

---

**Ready to start? Follow the steps above! 🚀**
