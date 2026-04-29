# 🌦️ Weather CLI App (with SQLite History)

A simple yet powerful command-line weather application that fetches
real-time weather data using the OpenWeather API and stores query
history in a SQLite database.

Think of it as a weather app with a memory 🧠 --- it not only tells you
the weather now, but also remembers what it said before.

------------------------------------------------------------------------

## 🚀 Features

-   🌍 Fetch real-time weather by city
-   💾 Store every query in a SQLite database
-   📜 View historical weather data (clean table format)
-   📊 Get temperature statistics per city:
    -   Average temperature
    -   Maximum temperature
    -   Minimum temperature
-   ⚠️ Graceful error handling:
    -   Invalid API key (401)
    -   City not found (404)
-   ⏱️ Accurate timestamping using Unix time (REAL)

------------------------------------------------------------------------

## 🏗️ Project Structure

    weather_app/
    │
    ├── api.py
    ├── config.py
    ├── database.py
    ├── main.py
    ├── weather.db
    ├── .env
    ├── .env.example
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup

### 1. Clone the repository

``` bash
git clone https://github.com/your-username/weather-cli.git
cd weather-cli
```

### 2. Create virtual environment

``` bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install requests python-dotenv
```

### 4. Setup environment variables

Create a `.env` file:

    WEATHER_API_KEY=your_api_key_here

------------------------------------------------------------------------

## ▶️ Usage

``` bash
python main.py
```

------------------------------------------------------------------------

## 📌 Menu Options

    1. Fetch Weather
    2. View History
    3. City Stats
    4. Exit

------------------------------------------------------------------------

## 📜 Example Output

    ==============================================================================
    ID    City         Temp (°C)  Humidity   Time                 Desc
    ==============================================================================
    6     Kolkata      19.97      100        2026-04-29 21:26:38  moderate rain
    ==============================================================================

------------------------------------------------------------------------

## 🧠 How It Works

-   Uses OpenWeather API
-   Stores results in SQLite

``` sql
CREATE TABLE weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    description TEXT,
    humidity INTEGER,
    fetched_at REAL
);
```

------------------------------------------------------------------------

## 📜 License

MIT License
