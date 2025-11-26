import requests
import time

API_KEY = "4b25353b228fa2cff1c64c0f8039a802"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cache = {}
CACHE_EXPIRY = 60  # seconds

def get_weather(city):
    city = city.lower()

    # Check cache
    if city in cache:
        data, timestamp = cache[city]
        if time.time() - timestamp < CACHE_EXPIRY:
            return {"source": "cache", "data": data}

    # Fetch from OpenWeatherMap API
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Store in cache
    cache[city] = (data, time.time())
    return {"source": "api", "data": data}
