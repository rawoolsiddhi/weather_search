from flask import Flask, request, jsonify, send_from_directory
from weather_service import get_weather
import os

# Path to frontend folder
FRONTEND_FOLDER = os.path.join(os.path.dirname(__file__), "../frontend")
app = Flask(__name__, static_folder=FRONTEND_FOLDER)

# Serve index.html
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Serve CSS and JS files
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Weather API
@app.route("/api/weather")
def weather_api():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City name required"}), 400

    response = get_weather(city)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
