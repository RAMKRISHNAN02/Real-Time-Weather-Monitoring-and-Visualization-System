import time
import schedule
from data_retrieval import fetch_weather_data
from data_processing import process_weather_data, calculate_daily_summary
from alerting import check_thresholds
from visualization import plot_daily_summary
import json

with open('config.json') as config_file:
    config = json.load(config_file)

INTERVAL = config["update_interval"]
METROS = config["metros"]

weather_data = []
daily_summary = []

def monitor_weather():
    print("Running weather monitoring task...")
    for city in METROS:
        data = fetch_weather_data(city)
        if data:
            processed_data = process_weather_data(data)
            print(f"Data for {city} processed: {processed_data}")
            check_thresholds(processed_data)
            weather_data.append(processed_data)
        else:
            print(f"No data received for {city}")

def daily_rollup():
    global weather_data, daily_summary
    if weather_data:
        print("Performing daily rollup...")
        summary = calculate_daily_summary(weather_data)
        print(f"Daily summary: {summary}")
        daily_summary.append(summary)
        plot_daily_summary(daily_summary)
        weather_data = []  # Reset daily data after rollup
    else:
        print("No weather data available for daily rollup.")

# Schedule tasks
schedule.every(INTERVAL).minutes.do(monitor_weather)
schedule.every().day.at("23:59").do(daily_rollup)

if __name__ == "__main__":
    print("Starting weather monitoring system...")
    while True:
        schedule.run_pending()  # Run scheduled tasks
        time.sleep(1)
