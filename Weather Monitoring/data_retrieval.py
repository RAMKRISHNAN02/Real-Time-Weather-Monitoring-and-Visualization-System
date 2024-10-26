import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)

API_KEY = config["api_key"]
METROS = config["metros"]

def fetch_weather_data(city):
    print(f"Fetching weather data for {city}...")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Data received for {city}: {data}")
            return {
                "city": city,
                "main": data["weather"][0]["main"],
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "dt": data["dt"]
            }
        else:
            print(f"Error {response.status_code} fetching data for {city}")
    except requests.RequestException as e:
        print(f"Request error for {city}: {e}")
    return None
