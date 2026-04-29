import sqlite3
from config import DATABASE
import time


class WeatherDB:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                description TEXT,
                humidity INTEGER,
                fetched_at REAL
            )
        """)
        self.conn.commit()

    def insert_weather(self, data: dict):
        self.cursor.execute("""
            INSERT INTO weather (city, temperature, description, humidity, fetched_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["city"],
            data["temperature"],
            data["description"],
            data["humidity"],
            time.time()
        ))
        self.conn.commit()

    def view_history(self, city: str):
        self.cursor.execute("""
            SELECT * FROM weather
            WHERE LOWER(city) = LOWER(?)
            ORDER BY fetched_at DESC
        """, (city,))
        return self.cursor.fetchall()

    def city_stats(self, city: str):
        self.cursor.execute("""
            SELECT 
                AVG(temperature),
                MAX(temperature),
                MIN(temperature)
            FROM weather
            WHERE city = ?
        """, (city,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()