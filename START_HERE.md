# 🎬 START HERE - Bangla Movie Review Sentiment Analysis

## ⚡ Quick Start

### Easiest Way (One Command)
```bash
run_all.bat
```
Opens both servers automatically! Then go to: **http://localhost:3000**

### Manual Way (Two Terminals)
```bash
# Terminal 1
start_backend.bat

# Terminal 2
start_frontend.bat
```

### First Time Setup
```bash
build_all.bat    # Build everything (10 minutes)
run_all.bat      # Start servers
```

---

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed installation
- **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** - API reference

---

## 🎯 Features

- ✅ Real-time sentiment analysis (Positive/Negative/Neutral)
- ✅ Explainable AI with word importance
- ✅ Color-coded visualization
- ✅ Analysis history
- ✅ Works with Bangla & English

---

## 📊 Structure

```
movieReview/
├── backend/          # Django + ML
├── frontend/         # React UI
├── ml_model/         # ML docs
└── *.bat            # Run scripts
```

---

## 🔧 Tech Stack

**Backend**: Django + PyTorch + BERT + LIME  
**Frontend**: React + Axios  
**Database**: SQLite

---

## 🚀 Available Scripts

| Script | Purpose |
|--------|---------|
| `run_all.bat` | Start both servers (easiest) |
| `start_backend.bat` | Start backend only |
| `start_frontend.bat` | Start frontend only |
| `build_all.bat` | Clean build from scratch |
| `clean_all.bat` | Remove all build files |

---

## 🐛 Troubleshooting

**Something broken?**
```bash
clean_all.bat
build_all.bat
run_all.bat
```

**Port in use?**
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

**Run `run_all.bat` and open http://localhost:3000** 🚀
