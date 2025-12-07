# 🎬 Bangla Movie Review Sentiment Analysis - Full Stack

A full-stack web application for Bangla movie review sentiment analysis with Explainable AI.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2.7-green.svg)
![React](https://img.shields.io/badge/react-18.2.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 🚀 Quick Start

### Windows (Easiest)
```bash
# Terminal 1: Start Backend
start_backend.bat

# Terminal 2: Start Frontend
start_frontend.bat

# Open browser: http://localhost:3000
```

### Manual Setup
See **[SETUP_GUIDE.md](SETUP_GUIDE.md)** for detailed instructions.

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
├── backend/          # Django REST API + ML Model
├── frontend/         # React Application
├── ml_model/         # ML Model Documentation
├── START_HERE.md     # 👈 Start here!
├── QUICK_START.md    # Fast setup guide
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
| **[START_HERE.md](START_HERE.md)** | 👈 **Begin here!** Quick overview |
| **[QUICK_START.md](QUICK_START.md)** | Fastest way to get running |
| **[SETUP_GUIDE.md](SETUP_GUIDE.md)** | Detailed installation guide |
| **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** | Architecture & design details |
| **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** | API endpoints & examples |

---

## 🔮 Future Enhancements

- [ ] User authentication & authorization
- [ ] Export results to PDF/CSV
- [ ] Batch analysis (upload CSV)
- [ ] Train custom Bangla model
- [ ] Deploy to cloud (AWS/Heroku)
- [ ] Mobile app version
- [ ] Sentiment trends dashboard

---

## 🐛 Troubleshooting

**Backend won't start?**
- Check Python version: `python --version`
- Verify port 8000 is free
- Activate virtual environment

**Frontend won't start?**
- Check Node version: `node --version`
- Delete `node_modules` and reinstall
- Verify port 3000 is free

**Analysis is slow?**
- First analysis: 10-20 seconds (model loading)
- Subsequent: 2-5 seconds (normal)
- Use GPU for 5-10x speedup

---

## 📝 Git Repositories

Each section has its own Git repository for modular development:
- **Main**: Overall project coordination
- **Backend**: Django API and ML service
- **Frontend**: React application
- **ML Model**: Model documentation

---

## 🤝 Contributing

This is an academic research project. Contributions welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

MIT License - Free for academic and research use.

```
Copyright (c) 2024 Bangla Sentiment Analysis Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🌟 Acknowledgments

- **HuggingFace** - Pre-trained BERT model
- **LIME** - Explainability framework
- **Django** - Web framework
- **React** - Frontend library
- **Academic Community** - Research inspiration

---

## 📞 Support

For issues or questions:
1. Check documentation files
2. Review error messages
3. Test API endpoints directly
4. Verify both servers are running

---

## 🎉 Status

✅ **Backend**: Complete - Django REST API with ML integration
✅ **Frontend**: Complete - React UI with modern design
✅ **Database**: Complete - SQLite with history tracking
✅ **ML Model**: Complete - BERT + LIME explainability
✅ **Documentation**: Complete - Comprehensive guides
✅ **Git**: Complete - Version control for all sections

---

**Built with ❤️ for academic research in Bangla NLP and Explainable AI**

*A full-stack demonstration of transparent AI decision-making for sentiment analysis*

---

## 🚀 Ready to Start?

👉 **[START_HERE.md](START_HERE.md)** - Begin your journey!
