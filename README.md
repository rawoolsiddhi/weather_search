
# Weather Search App

A simple weather search engine 

## Features
- Search weather by city
- Shows temperature, humidity, wind, description
- Backend caching for faster results
- REST API following proper structure

## Run Backend
- cd backend
- pip install -r requirements.txt
- python app.py
- http://127.0.0.1:5000/

<img width="499" height="571" alt="image" src="https://github.com/user-attachments/assets/887e3e6e-e11e-415c-873a-90c6d681e8bb" />

## Project Structure

weather_search/
├─ backend/
│   ├─ app.py
│   ├─ weather_service.py
│   └─ __pycache__/
├─ frontend/
│   ├─ index.html
│   ├─ style.css
│   └─ script.js
├─ .gitignore
├─ LICENSE
├─ README.md
└─ weather_service1.py  # optional reference for API key (do not commit actual key)


Environment / API Key

The app uses OpenWeather API.

Store your API key in weather_service.py or weather_service1.py.

Recommended for safety: use a .env file and do not commit your key.

Example in weather_service.py:

API_KEY = "your_api_key_here"  # replace with your own API key



How to Run Frontend

Open frontend/index.html in your browser

Make sure backend is running

Enter a city name and click Search to see weather results

