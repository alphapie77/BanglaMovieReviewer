# 🔧 Troubleshooting Guide

## "বিশ্লেষণে ত্রুটি হয়েছে" Error

### Quick Diagnosis

1. **Check Backend Server**
   ```bash
   # Open http://localhost:8000/api/sentiment/ in browser
   # Should show API endpoint list
   ```

2. **Test API Directly**
   ```bash
   cd backend
   python test_api.py
   ```

3. **Check Backend Logs**
   - Look at the terminal where `python manage.py runserver` is running
   - Check for error messages

---

## Common Issues & Solutions

### 1. Backend Not Running
**Error**: `Backend server চালু আছে কিনা পরীক্ষা করুন`

**Solution**:
```bash
cd backend
venv\Scripts\activate
python manage.py runserver
```

### 2. ML Model Not Loading
**Error**: `ML model load হতে সমস্যা হয়েছে`

**Causes**:
- First time loading (downloads ~500MB model)
- Insufficient RAM (need 4GB+)
- Network issues during model download

**Solution**:
```bash
# Wait for model to download (first time only)
# Check backend terminal for progress
# Model downloads to: C:\Users\<username>\.cache\huggingface\
```

### 3. Dependencies Missing
**Error**: `ModuleNotFoundError: No module named 'transformers'`

**Solution**:
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Empty Review Text
**Error**: `Review text cannot be empty`

**Solution**: Enter at least a few words in Bangla or English

### 5. CORS Error
**Error**: `Access-Control-Allow-Origin`

**Solution**: Check `backend/backend/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

### 6. Port Already in Use
**Error**: `Error: That port is already in use`

**Solution**:
```bash
# Backend (port 8000)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Frontend (port 3000)
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

---

## Testing Checklist

- [ ] Backend server running on http://localhost:8000
- [ ] Frontend server running on http://localhost:3000
- [ ] Can access http://localhost:8000/api/sentiment/
- [ ] `python test_api.py` passes
- [ ] No errors in backend terminal
- [ ] No errors in browser console (F12)

---

## Manual API Test

### Using curl:
```bash
curl -X POST http://localhost:8000/api/sentiment/analyze/ \
  -H "Content-Type: application/json" \
  -d "{\"review_text\": \"এই সিনেমাটি অসাধারণ\"}"
```

### Using Python:
```python
import requests
response = requests.post(
    "http://localhost:8000/api/sentiment/analyze/",
    json={"review_text": "এই সিনেমাটি অসাধারণ"}
)
print(response.json())
```

---

## System Requirements

- **RAM**: 4GB minimum, 8GB recommended
- **Disk**: 2GB free space (for ML model)
- **Internet**: Required for first-time model download
- **Python**: 3.8 or higher
- **Node.js**: 16 or higher

---

## Getting Help

1. Check backend terminal for detailed error messages
2. Check browser console (F12) for frontend errors
3. Run `python test_api.py` for API diagnostics
4. Check if model downloaded: `C:\Users\<username>\.cache\huggingface\`

---

## Clean Restart

```bash
# Stop all servers (Ctrl+C)

# Clean and restart
clean_all.bat
run_all.bat
```
