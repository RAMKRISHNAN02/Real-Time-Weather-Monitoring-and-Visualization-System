# Real-Time-Weather-Monitoring-and-Visualization-System
This project is a real-time data processing system that monitors weather conditions for selected cities in India, provides daily summaries, and visualizes temperature trends. The system uses the OpenWeatherMap API to retrieve weather data, with features for data rollups, alerting, and visualization.

Features
Real-Time Data Retrieval: Fetches and processes weather data for multiple cities at a configurable interval.
Daily Weather Summaries: Calculates average, max, min temperatures, and the dominant weather condition daily.
Alerting: Customizable alerts for specific weather conditions or temperature thresholds.
Visualization: Plots daily summaries and historical temperature trends.
Installation
Clone this repository:

git clone https://github.com/username/WeatherMonitoringSystem.git
cd WeatherMonitoringSystem
Install Dependencies: Ensure you have Python 3.6+ and then install the required packages:

pip install requests matplotlib schedule
Get an OpenWeatherMap API Key:

Sign up at OpenWeatherMap to get a free API key.
Configuration:

In config.json, update the "api_key" field with your OpenWeatherMap API key and adjust other configurations as needed:

{
    "api_key": "YOUR_OPENWEATHERMAP_API_KEY",
    "update_interval": 5,
    "temperature_threshold": 35,
    "metros": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
}
Project Structure
main.py: Orchestrates the overall process, scheduling data retrieval, rollups, and visualizations.
config.json: Configuration file for API key, update intervals, and cities.
data_retrieval.py: Fetches weather data from OpenWeatherMap.
data_processing.py: Processes data and calculates daily summaries.
alerting.py: Checks for threshold violations and triggers alerts.
visualization.py: Plots daily weather summaries using matplotlib.
Usage
Run the System: Run the main.py file:


python main.py
Alerts and Logs:

Alerts are shown in the console if a threshold is breached.
Daily Visualization:

A daily weather summary plot will display trends and temperature summaries.

Tests
Manual Tests:

API Connection: Ensure the API key is valid and the connection to OpenWeatherMap is successful.
Data Retrieval: Verify data retrieval and parsing.
Temperature Conversion: Check conversion from Kelvin to Celsius.
Alerting: Set a low threshold to confirm alerts trigger correctly.
Visualization: Manually verify that plot_daily_summary() displays expected data and trends.
Troubleshooting
No Visualization: Ensure you’re using plt.show(block=True) in visualization.py if using PyCharm Community Edition or another non-interactive environment.
API Connection Issues: Check your API key in config.json and network connectivity.
License
This project is open-source and free to use.

