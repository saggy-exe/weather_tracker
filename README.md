# 🌦️ Weather Tracker CLI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![CLI](https://img.shields.io/badge/Interface-CLI-orange)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

A simple yet practical **command-line weather tracker** that fetches real-time data from the OpenWeather API and stores it locally using SQLite.

This isn’t just a weather app — it **remembers every query**, so you can analyze past data instead of just seeing the current weather.

---

## 🚀 Features

- 🌍 Fetch real-time weather by city  
- 💾 Automatically store results in SQLite  
- 📜 View historical weather data in a clean table  
- 📊 Get city-based temperature stats:
  - Average temperature  
  - Maximum temperature  
  - Minimum temperature  
- ⚠️ Handles errors properly:
  - Invalid API key (401)  
  - City not found (404)  
- ⏱️ Accurate timestamps using Unix time  

---

## 🏗️ Project Structure

```
weather_tracker/
│
├── api.py
├── config.py
├── database.py
├── main.py
├── weather.db
├── .env
├── .env.example
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/saggy-exe/weather_tracker.git
cd weather_tracker
```

### 2. Create & activate virtual environment

```bash
python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
WEATHER_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 📌 CLI Menu

```
1. Fetch Weather
2. View History
3. City Stats
4. Exit
```

---

## 📜 Example Output

```
==============================================================================
ID    City         Temp (°C)  Humidity   Time                 Description
==============================================================================
6     Kolkata      19.97      100        2026-04-29 21:26:38  moderate rain
==============================================================================
```

---

## 🧠 How It Works

- Fetches weather data from OpenWeather API  
- Stores every request in SQLite  

```sql
CREATE TABLE weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    description TEXT,
    humidity INTEGER,
    fetched_at REAL
);
```

---

## 🛠️ Tech Stack

- Python  
- Requests  
- SQLite  
- python-dotenv  

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Possible Improvements

- Add unit tests  
- Export history to CSV  
- Add search/filter for history  
- Convert CLI → Web dashboard  
