# 📈 StockPrediction AI System

A Django-based stock analysis platform that provides real-time stock data, AI-powered insights, and automated price alerts using background tasks.

---

## 🚀 Features

- 📊 Real-time stock data (Alpha Vantage, Finnhub, StockData)
- 🤖 AI-based stock analysis (Google Gemini)
- 🔔 Price alert system (above/below target)
- ⚡ Background tasks using Celery + Redis
- 🔐 JWT Authentication (Secure APIs)
- 📡 REST APIs for frontend integration

---

## 🛠️ Tech Stack

- Backend: Django, Django REST Framework  
- Async Tasks: Celery  
- Broker: Redis  
- Database: PostgreSQL / MySQL  
- AI: Google Gemini  
- APIs: Alpha Vantage, Finnhub, StockData  

---

## 📁 Project Structure

stockprediction/
│
├── alerts/
├── users/
├── stocks/
├── chatbot/
├── core/
├── manage.py
├── requirements.txt
└── .env

---

## ⚙️ Installation

### 1. Clone Repository
git clone https://github.com/your-username/stockprediction.git  
cd stockprediction

### 2. Create Virtual Environment
python -m venv venv  
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

---

## 🔐 Environment Variables (.env)

SECRET_KEY=your_secret_key

ALPHA_VANTAGE_KEY=your_key  
FINNHUB_KEY=your_key  
STOCKDATA_API_KEY=your_key  

GEMINI_API_KEY=your_key  

EMAIL_HOST_USER=your_email  
EMAIL_HOST_PASSWORD=your_app_password  

---

## 🗄️ Database Setup

python manage.py makemigrations  
python manage.py migrate  

---

## ▶️ Run Server

python manage.py runserver  

---

## ⚡ Run Celery Worker

python -m celery -A stockprediction worker -l info -P solo  

---

## ⏰ Run Celery Beat

python -m celery -A stockprediction beat -l info  

---

## 📡 API Endpoints

### Get Stock Data
GET /api/stocks/?symbol=AAPL  

### AI Analysis
POST /api/chatbot/  
{
  "symbol": "AAPL",
  "question": "Should I invest?"
}

### Create Alert
POST /api/alerts/  
{
  "symbol": "AAPL",
  "target_price": 150,
  "alert_type": "below"
}

---

## 🔔 Alert Logic

- Runs via Celery Beat  
- Fetches stock price  
- Compares with target  
- Sends email if matched  

---

## 🧠 AI Feature

- Uses Gemini AI  
- Provides buy/sell suggestions  
- Trend analysis  

---

## 📧 Email Notifications

- Gmail SMTP integration  
- Sends alerts automatically  

---

## 📌 Future Improvements

- Frontend Dashboard (React)  
- Charts & analytics  
- Mobile app  
- WebSocket real-time updates  

---

## 👨‍💻 Author

Kartik Choudhary  
Python Developer  

GitHub: https://github.com/kartikchoudhary1177-lgtm  
Email: kartikchoudhary1177@gmail.com  

---

## ⭐ Resume Line

Developed a Stock Prediction System with real-time APIs, AI analysis, and automated alerts using Django, Celery, Redis, and REST APIs.
