import json

with open('config.json') as config_file:
    config = json.load(config_file)

THRESHOLD_TEMP = config["temperature_threshold"]

def check_thresholds(weather_data):
    if weather_data["temp_celsius"] > THRESHOLD_TEMP:
        print(f"ALERT: Temperature in {weather_data['city']} exceeded {THRESHOLD_TEMP}°C.")
        # Add email or other alert mechanisms here if needed.
