import requests
import matplotlib.pyplot as plt

# OpenWeatherMap API settings
API_KEY = "bfaea3b827feaf5b3da0d950f89a7da0"
CITY = "Pune"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={"Pune"}&units=metric&appid={"bfaea3b827feaf5b3da0d950f89a7da0"}"
# Fetch weather data
def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

# Process data
def process_data(data):
    timestamps = [entry['dt_txt'] for entry in data['list']]
    temperatures = [entry['main']['temp'] for entry in data['list']]
    return timestamps, temperatures

# Visualize data
def visualize_data(timestamps, temperatures):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, temperatures, marker="o", linestyle="-", color="b")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Forecast for {CITY}")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    if weather_data:
        timestamps, temperatures = process_data(weather_data)
        visualize_data(timestamps, temperatures)
