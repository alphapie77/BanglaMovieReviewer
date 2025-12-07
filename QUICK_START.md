# ⚡ Quick Start (Windows)

## Easiest Way to Run

### Option 1: Run Everything at Once (Easiest!)
```bash
run_all.bat
```
This opens both servers in separate windows automatically!

### Option 2: Run Separately (Recommended for Development)

1. **Start Backend** (in first terminal):
   ```bash
   start_backend.bat
   ```

2. **Start Frontend** (in second terminal):
   ```bash
   start_frontend.bat
   ```

3. **Open Browser**: http://localhost:3000

### Option 3: First Time Setup
```bash
build_all.bat
```
Then use Option 1 or 2 to run

### Option 2: Manual Setup

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.

## Available Scripts

| Script | Purpose |
|--------|--------|
| `run_all.bat` | Start both servers at once (easiest!) |
| `start_backend.bat` | Start Django backend only |
| `start_frontend.bat` | Start React frontend only |
| `build_all.bat` | Clean build everything from scratch |
| `build_backend.bat` | Build backend only |
| `build_frontend.bat` | Build frontend only |
| `clean_all.bat` | Remove all build files |

## First Time Setup

The scripts will automatically:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Run database migrations
- ✅ Start the servers

**Note**: First run takes 5-10 minutes to install everything.

## What You'll See

### Backend Terminal:
```
Starting Django Backend Server
...
Django version 4.2.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
```

### Frontend Terminal:
```
Starting React Frontend Server
...
Compiled successfully!
You can now view bangla-sentiment-frontend in the browser.
Local: http://localhost:3000
```

## Testing

1. Go to: http://localhost:3000
2. Enter a Bangla review: `সিনেমাটা অসাধারণ ছিল!`
3. Click "বিশ্লেষণ করুন"
4. Wait 10-20 seconds (first time only)
5. See the results! 🎉

## Stopping the Servers

Press `Ctrl + C` in each terminal window.

## Troubleshooting

**Port already in use?**
```bash
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

**Dependencies not installing?**
- Make sure you have Python 3.8+ and Node.js 16+
- Check your internet connection
- Try: `clean_all.bat` then `build_all.bat`

**Something broken?**
```bash
clean_all.bat    # Clean everything
build_all.bat    # Rebuild from scratch
run_all.bat      # Start both servers
```

## Next Steps

- ✅ Test with different reviews
- ✅ Check history panel
- ✅ View admin: http://localhost:8000/admin
- ✅ Customize the UI

---

**Need detailed setup?** See [SETUP_GUIDE.md](SETUP_GUIDE.md)
