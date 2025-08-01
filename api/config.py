import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENWEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_UNITS = "metric"
OPENWEATHER_LANG = "en"