# 🚀 Scripts Guide

## Quick Reference

| Script | What It Does | When to Use |
|--------|-------------|-------------|
| **run_all.bat** | Starts both servers in separate windows | Easiest way to run everything |
| **start_backend.bat** | Starts Django backend only | Development (backend work) |
| **start_frontend.bat** | Starts React frontend only | Development (frontend work) |
| **build_all.bat** | Clean build from scratch | First time or after major changes |
| **build_backend.bat** | Rebuild backend only | Backend dependency changes |
| **build_frontend.bat** | Build production frontend | Production deployment |
| **clean_all.bat** | Remove all build files | Start fresh / fix issues |

---

## 🎯 Common Workflows

### First Time Setup
```bash
build_all.bat    # Build everything (5-10 minutes)
run_all.bat      # Start both servers
```
Then open: http://localhost:3000

### Daily Development
```bash
run_all.bat      # Start both servers
```
OR
```bash
start_backend.bat    # Terminal 1
start_frontend.bat   # Terminal 2
```

### After Pulling New Code
```bash
# If backend changed:
build_backend.bat

# If frontend changed:
cd frontend
npm install
```

### Something Broken?
```bash
clean_all.bat    # Clean everything
build_all.bat    # Rebuild
run_all.bat      # Run
```

---

## 📝 Script Details

### run_all.bat
**Purpose**: Start both servers automatically
**What it does**:
1. Opens backend in new window
2. Waits 5 seconds
3. Opens frontend in new window
4. Shows URLs

**Usage**:
```bash
run_all.bat
```

---

### start_backend.bat
**Purpose**: Start Django development server
**What it does**:
1. Creates venv if missing
2. Activates virtual environment
3. Installs dependencies if needed
4. Runs migrations if needed
5. Starts server on port 8000

**Usage**:
```bash
start_backend.bat
```

**Output**:
- Server: http://localhost:8000
- Admin: http://localhost:8000/admin

---

### start_frontend.bat
**Purpose**: Start React development server
**What it does**:
1. Checks Node.js installed
2. Installs dependencies if needed
3. Starts server on port 3000

**Usage**:
```bash
start_frontend.bat
```

**Output**:
- Server: http://localhost:3000

---

### build_all.bat
**Purpose**: Complete clean build
**What it does**:
1. Runs build_backend.bat
2. Runs build_frontend.bat

**Usage**:
```bash
build_all.bat
```

**Time**: 10-15 minutes first time

---

### build_backend.bat
**Purpose**: Rebuild backend from scratch
**What it does**:
1. Removes old venv
2. Creates new venv
3. Upgrades pip
4. Installs all dependencies
5. Runs migrations

**Usage**:
```bash
build_backend.bat
```

**Time**: 5-10 minutes

---

### build_frontend.bat
**Purpose**: Build production frontend
**What it does**:
1. Removes old build
2. Installs dependencies
3. Creates production build

**Usage**:
```bash
build_frontend.bat
```

**Output**: `frontend/build/` folder

**Time**: 2-3 minutes

---

### clean_all.bat
**Purpose**: Remove all build artifacts
**What it does**:
1. Asks for confirmation
2. Removes backend/venv/
3. Removes backend/db.sqlite3
4. Removes frontend/node_modules/
5. Removes frontend/build/

**Usage**:
```bash
clean_all.bat
```

**Warning**: This deletes your database!

---

## 🔧 Troubleshooting

### Script won't run?
- Right-click → "Run as administrator"
- Check Python/Node.js installed
- Check internet connection

### Port already in use?
```bash
# Find process
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Kill process
taskkill /PID <PID> /F
```

### Dependencies fail to install?
```bash
# Backend
cd backend
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Frontend
cd frontend
npm cache clean --force
npm install
```

### Database issues?
```bash
cd backend
del db.sqlite3
python manage.py migrate
```

### Complete reset?
```bash
clean_all.bat
build_all.bat
run_all.bat
```

---

## 💡 Pro Tips

1. **Use run_all.bat** for quick testing
2. **Use separate terminals** for development (easier to see logs)
3. **Keep terminals open** while working
4. **Check error messages** in terminal output
5. **Run clean_all.bat** if things get weird

---

## 🎯 Quick Commands

```bash
# Start everything
run_all.bat

# Start separately
start_backend.bat
start_frontend.bat

# Rebuild everything
clean_all.bat
build_all.bat

# Just backend
build_backend.bat
start_backend.bat

# Just frontend
build_frontend.bat
start_frontend.bat
```

---

## 📊 What Each Script Checks

### start_backend.bat
✅ Python installed
✅ Virtual environment exists
✅ Dependencies installed
✅ Database migrated

### start_frontend.bat
✅ Node.js installed
✅ Dependencies installed

### build_backend.bat
✅ Python version
✅ Pip upgraded
✅ All packages installed
✅ Migrations applied

### build_frontend.bat
✅ Node.js installed
✅ Clean build directory
✅ Production bundle created

---

**Need help? Check [QUICK_START.md](QUICK_START.md) or [SETUP_GUIDE.md](SETUP_GUIDE.md)**
