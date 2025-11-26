
# Weather Search App

A simple weather search engine 

## Features
- Search weather by city
- Shows temperature, humidity, wind, description
- Backend caching for faster results
- REST API following proper structure


<img width="499" height="571" alt="image" src="https://github.com/user-attachments/assets/887e3e6e-e11e-415c-873a-90c6d681e8bb" />

## Project Structure
```
weather_search/
├── backend/
│ ├── app.py
│ ├── weather_service.py
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── .gitignore
├── LICENSE
├── README.md
└── weather_service1.py # optional API key reference (do not commit real key)
```

## Environment / API Key
- The app uses **OpenWeather API**.  

## Run Backend

- cd backend
- pip install -r requirements.txt
- python app.py

 Open your browser at:
  - http://127.0.0.1:5000/

## Run Frontend
- Open frontend/index.html in your browser
- Make sure the backend server is running
- Enter a city name and click "Search" to see results


