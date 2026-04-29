import requests
from config import WEATHER_API_KEY, BASE_URL
from datetime import datetime


def fetch_weather(city: str):
    query = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'en',
        'mode': 'json'
    }

    response = requests.get(BASE_URL, params=query)

    if response.status_code == 401:
        raise PermissionError("Invalid API key")

    if response.status_code == 404:
        return {}

    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")

    data = response.json()

    result = {
        "city": data.get("name").lower(),
        "temperature": data.get("main", {}).get("temp"),
        "description": data.get("weather", [{}])[0].get("description"),
        "humidity": data.get("main", {}).get("humidity"),
        "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return result