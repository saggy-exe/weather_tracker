import os
from dotenv import load_dotenv

load_dotenv()

def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if value is None or value.strip()=="":
        raise ValueError(
            f"Missing required environment variable: '{key}'.\n"
            f"Add it to your .env file like:\n{key}=your_value_here"
        )
    return value

WEATHER_API_KEY = get_required_env("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "weather.db")