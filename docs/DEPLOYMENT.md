# 🚀 Deployment Guide

## Deployment Options

### Option 1: Vercel (Frontend) + PythonAnywhere (Backend) - Free
### Option 2: Render (Recommended - Free)
### Option 3: Railway
### Option 4: Heroku
### Option 5: AWS/DigitalOcean

---

## 🎯 Option 1: Vercel + PythonAnywhere (Best Free Option)

### A. Deploy Backend on PythonAnywhere

**Prerequisites:**
- PythonAnywhere account (free): https://www.pythonanywhere.com

**Step 1: Upload Code**

1. Sign up at PythonAnywhere
2. Go to "Files" tab
3. Upload your backend folder or clone from GitHub:
   ```bash
   git clone https://github.com/alphapie77/BanglaMovieReviewer.git
   cd BanglaMovieReviewer/backend
   ```

**Step 2: Create Virtual Environment**

```bash
# In PythonAnywhere Bash console
cd ~/BanglaMovieReviewer/backend
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Step 3: Configure Web App**

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration" → Python 3.10
4. Configure:

**WSGI Configuration** (`/var/www/yourusername_pythonanywhere_com_wsgi.py`):
```python
import sys
import os

path = '/home/yourusername/BanglaMovieReviewer/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Virtualenv**: `/home/yourusername/BanglaMovieReviewer/backend/venv`

**Static files**:
- URL: `/static/`
- Directory: `/home/yourusername/BanglaMovieReviewer/backend/staticfiles`

**Step 4: Update Settings**

`backend/config/settings.py`:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

CORS_ALLOWED_ORIGINS = [
    "https://your-app.vercel.app",
]
```

**Step 5: Collect Static & Migrate**

```bash
cd ~/BanglaMovieReviewer/backend
source venv/bin/activate
python manage.py collectstatic
python manage.py migrate
```

**Step 6: Reload Web App**

Click "Reload" button on Web tab.

**Backend URL**: `https://yourusername.pythonanywhere.com`

---

### B. Deploy Frontend on Vercel

**Prerequisites:**
- Vercel account (free): https://vercel.com
- GitHub repository

**Step 1: Update API URL**

`frontend/src/services/api.js`:
```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://yourusername.pythonanywhere.com/api';
```

**Step 2: Create `vercel.json`**

`frontend/vercel.json`:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "devCommand": "npm start",
  "installCommand": "npm install"
}
```

**Step 3: Deploy to Vercel**

**Method 1: Vercel CLI**
```bash
npm install -g vercel
cd frontend
vercel
```

**Method 2: Vercel Dashboard**
1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Import from GitHub
4. Select repository
5. Configure:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
6. Add Environment Variable:
   - `REACT_APP_API_URL`: `https://yourusername.pythonanywhere.com/api`
7. Click "Deploy"

**Frontend URL**: `https://your-app.vercel.app`

**Step 4: Update CORS**

Update PythonAnywhere backend settings with Vercel URL and reload.

---

## ⚠️ PythonAnywhere Limitations

**Free Tier:**
- ✅ 512MB disk space
- ✅ 1 web app
- ✅ Python 3.10
- ❌ No HTTPS for custom domains
- ❌ Limited CPU time
- ⚠️ **ML Model Issue**: 500MB model may exceed disk limit

**Solution for ML Model:**

1. **Use smaller model** (not recommended):
   ```python
   model="distilbert-base-uncased-finetuned-sst-2-english"  # 250MB
   ```

2. **Upgrade to paid plan** ($5/month):
   - 2GB disk space
   - More CPU time
   - Better for ML models

3. **Use external model hosting**:
   - Host model on HuggingFace Inference API
   - Call API instead of loading locally

---

## 🎯 Option 2: Render (Free & Easy)

### Prerequisites
- GitHub account
- Render account (free): https://render.com

### Step 1: Prepare Backend for Deployment

**1. Create `render.yaml` in root:**
```yaml
services:
  - type: web
    name: bangla-movie-backend
    env: python
    buildCommand: "cd backend && pip install -r requirements.txt"
    startCommand: "cd backend && gunicorn config.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: DEBUG
        value: False
```

**2. Update `backend/requirements.txt`:**
```txt
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
torch>=2.0.0
transformers>=4.40.0
lime==0.2.0.1
numpy>=1.24.0
scikit-learn>=1.3.0
gunicorn==21.2.0
whitenoise==6.6.0
```

**3. Update `backend/config/settings.py`:**
```python
import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Update with your domain

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-url.onrender.com",  # Update after frontend deploy
]
```

### Step 2: Deploy Backend on Render

1. Go to https://render.com/dashboard
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: bangla-movie-backend
   - **Root Directory**: `backend`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn config.wsgi:application`
   - **Instance Type**: Free
5. Add Environment Variables:
   - `PYTHON_VERSION`: 3.11.0
   - `DEBUG`: False
6. Click "Create Web Service"
7. Wait 10-15 minutes (model downloads on first deploy)
8. Copy your backend URL: `https://bangla-movie-backend.onrender.com`

### Step 3: Deploy Frontend on Render

**1. Update `frontend/src/services/api.js`:**
```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://bangla-movie-backend.onrender.com/api';
```

**2. Create `frontend/render.yaml`:**
```yaml
services:
  - type: web
    name: bangla-movie-frontend
    env: static
    buildCommand: npm install && npm run build
    staticPublishPath: ./build
```

**3. Deploy Frontend:**
1. Go to Render Dashboard
2. Click "New +" → "Static Site"
3. Connect GitHub repository
4. Configure:
   - **Name**: bangla-movie-frontend
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `build`
5. Add Environment Variable:
   - `REACT_APP_API_URL`: `https://bangla-movie-backend.onrender.com/api`
6. Click "Create Static Site"

### Step 4: Update CORS

Update backend `settings.py` with frontend URL:
```python
CORS_ALLOWED_ORIGINS = [
    "https://bangla-movie-frontend.onrender.com",
]
```

Push changes and Render will auto-deploy.

---

## 🎯 Option 2: Railway (Alternative)

### Deploy Backend

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select repository
4. Add environment variables:
   ```
   PYTHON_VERSION=3.11
   DEBUG=False
   ```
5. Railway will auto-detect Django and deploy

### Deploy Frontend

1. Create new service in same project
2. Select repository
3. Set root directory: `frontend`
4. Add build command: `npm run build`
5. Railway will serve the build

---

## 🎯 Option 3: Docker Deployment

### Create `Dockerfile` for Backend

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Create `Dockerfile` for Frontend

```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Create `docker-compose.yml`

```yaml
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
    volumes:
      - ./backend:/app

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

**Deploy:**
```bash
docker-compose up -d
```

---

## ⚠️ Important Notes

### ML Model Considerations

**Problem**: Model is 500MB and takes time to download

**Solutions**:

1. **Pre-download on deploy** (Recommended):
   Add to build command:
   ```bash
   python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')"
   ```

2. **Use model caching**:
   Set environment variable:
   ```
   TRANSFORMERS_CACHE=/app/model_cache
   ```

3. **Increase timeout**:
   - Render: Automatic (handles long builds)
   - Railway: Increase in settings
   - Heroku: Use worker dyno

### Memory Requirements

- **Minimum**: 2GB RAM
- **Recommended**: 4GB RAM
- **Free tiers**:
  - Render: 512MB (may struggle)
  - Railway: 8GB (good)
  - Heroku: 512MB (not enough)

### Database

For production, replace SQLite:

**PostgreSQL (Recommended)**:
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}
```

---

## 🔒 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use environment variables for secrets
- [ ] Update `ALLOWED_HOSTS`
- [ ] Configure proper CORS origins
- [ ] Use HTTPS (automatic on Render/Railway)
- [ ] Add rate limiting (optional)
- [ ] Set up monitoring

---

## 📊 Cost Comparison

| Platform | Backend | Frontend | Total/Month |
|----------|---------|----------|-------------|
| **Vercel + PythonAnywhere** | Free* | Free | $0 (or $5 paid) |
| **Render** | Free (512MB) | Free | $0 |
| **Railway** | $5 (8GB) | Free | $5 |
| **Heroku** | $7 (1GB) | Free | $7 |
| **AWS** | ~$10 | ~$1 | ~$11 |

*PythonAnywhere free tier may struggle with 500MB model. Paid plan ($5/month) recommended.

**Recommendations**:
- **Best Free**: Vercel (frontend) + Render (backend)
- **Best Paid**: Vercel (frontend) + Railway (backend) - $5/month
- **Budget Option**: Vercel + PythonAnywhere Paid - $5/month

---

## 🚀 Quick Deploy Commands

### Push to GitHub
```bash
git add -A
git commit -m "Prepare for deployment"
git push origin master
```

### Test Locally Before Deploy
```bash
# Backend
cd backend
python manage.py collectstatic
gunicorn config.wsgi:application

# Frontend
cd frontend
npm run build
serve -s build
```

---

## 🆘 Troubleshooting

### Backend won't start
- Check logs for errors
- Verify all dependencies installed
- Ensure model downloads successfully
- Check memory usage

### Frontend can't connect to backend
- Verify CORS settings
- Check API URL in frontend
- Ensure backend is running
- Test API endpoint directly

### Model loading timeout
- Increase build timeout
- Pre-download model in build step
- Use persistent storage for model cache

---

## 📚 Additional Resources

- [Render Docs](https://render.com/docs)
- [Railway Docs](https://docs.railway.app)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [React Deployment](https://create-react-app.dev/docs/deployment/)

---

**Need Help?** Check the logs and error messages first!
