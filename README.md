# 🎬 Bangla Movie Review Sentiment Analysis - Full Stack

A full-stack web application for Bangla movie review sentiment analysis with Explainable AI.

## 🏗️ Architecture

- **Backend**: Django REST Framework + ML Model (Transformers + LIME)
- **Frontend**: React + Tailwind CSS
- **Database**: SQLite
- **ML Model**: Multilingual BERT for sentiment analysis

## 📁 Project Structure

```
movieReview/
├── backend/          # Django REST API
├── frontend/         # React application
├── ml_model/         # ML model and utilities
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs on: http://localhost:8000

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on: http://localhost:3000

## 📊 Features

- ✅ Real-time sentiment analysis
- ✅ Explainable AI (word importance visualization)
- ✅ Analysis history storage
- ✅ Modern, responsive UI
- ✅ Color-coded word highlighting
- ✅ Confidence scores

## 🔧 Development

Each section (backend, frontend, ml_model) has its own Git repository for modular development.

## 📝 License

MIT License - Academic/Research Project
