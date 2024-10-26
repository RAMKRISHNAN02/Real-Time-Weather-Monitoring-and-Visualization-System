from datetime import datetime

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    data["temp_celsius"] = kelvin_to_celsius(data["temp"])
    data["feels_like_celsius"] = kelvin_to_celsius(data["feels_like"])
    data["date"] = datetime.fromtimestamp(data["dt"]).strftime('%Y-%m-%d')
    return data

# Calculate daily summaries with max, min, average, and dominant condition.
def calculate_daily_summary(data):
    daily_summary = {
        "date": data[0]["date"],
        "average_temp": sum(d["temp_celsius"] for d in data) / len(data),
        "max_temp": max(d["temp_celsius"] for d in data),
        "min_temp": min(d["temp_celsius"] for d in data),
        "dominant_condition": max(set([d["main"] for d in data]), key=[d["main"] for d in data].count)
    }
    return daily_summary
