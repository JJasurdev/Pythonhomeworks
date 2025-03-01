import requests

# OpenWeatherMap API URL
API_KEY = 'secret'  
CITY = 'Tashkent'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={Toshkent}&appid={}&units=metric'

# Fetch data from the OpenWeatherMap API
response = requests.get()

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant weather information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    
    # Print out the weather information
    print(f"Weather Information for {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Weather: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error: Unable to fetch weather data")
