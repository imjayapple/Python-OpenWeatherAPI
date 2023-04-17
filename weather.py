# Need import OS to interact with the operating system and os-related tasks such as working with environment variables
# and in this instance that means protecting the API key from OpenWeatherApp
import os

# Requests library for making HTTP requests in Python. It abstracts the complexities of making requests behind a simple
# api, allowing the user to send HTTP requests using various methods like GET, POST, PUT, DELETE, etc.
# In this project the user will make an HTTP GET request to fetch weather data from a given city
import requests

# Use setx OPENWEATHERMAP_API_KEY "" in PowerShell, with the key between quotes, to set the environemtn variable
API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")  # You can hardcode the API key for testing purposes
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fetch weather for a specific city
# Query parameters for the API request,
# "q" = the city name, which is the value of 'city_name'
# "appid" = the API key for OpenWeatherApp, which is the value of 'API_key'
# "units" = the unit system to use for the temperature data, set to metric in this case
def get_weather(city_name):
        params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }