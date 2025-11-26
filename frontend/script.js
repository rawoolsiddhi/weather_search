async function searchWeather() {
    const city = document.getElementById("cityInput").value.trim();
    if (!city) {
        alert("Please enter a city name");
        return;
    }

    try {
        const res = await fetch(`http://127.0.0.1:5000/api/weather?city=${city}`);
        const data = await res.json();

        if (data.error) {
            document.getElementById("result").innerHTML = `<p style="color:red">${data.error}</p>`;
            return;
        }

        if (data.data && data.data.cod && data.data.cod !== 200) {
            document.getElementById("result").innerHTML =
                `<p style="color:red">Error: ${data.data.message}</p>`;
            return;
        }

        const weather = data.data;
        document.getElementById("result").innerHTML = `
            <h3>Weather in ${weather.name}, ${weather.sys.country}</h3>
            <p>Temperature: ${weather.main.temp}°C</p>
            <p>Weather: ${weather.weather[0].description}</p>
            <p>Humidity: ${weather.main.humidity}%</p>
            <p>Wind Speed: ${weather.wind.speed} m/s</p>
            <p><small>Source: ${data.source}</small></p>
        `;
    } catch (err) {
        document.getElementById("result").innerHTML = `<p style="color:red">Fetch error: ${err}</p>`;
    }
}
