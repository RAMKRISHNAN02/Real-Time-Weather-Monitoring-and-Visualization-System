import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')  # or 'Qt5Agg' if you have Qt installed

import matplotlib.pyplot as plt


def plot_daily_summary(daily_summary):
    dates = [summary["date"] for summary in daily_summary]
    avg_temps = [summary["average_temp"] for summary in daily_summary]
    max_temps = [summary["max_temp"] for summary in daily_summary]
    min_temps = [summary["min_temp"] for summary in daily_summary]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, avg_temps, label="Average Temp (°C)", marker='o', color='blue')
    plt.plot(dates, max_temps, label="Max Temp (°C)", marker='^', color='red')
    plt.plot(dates, min_temps, label="Min Temp (°C)", marker='v', color='green')

    plt.title("Daily Weather Summary")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show(block=True)

