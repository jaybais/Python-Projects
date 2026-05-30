import requests
from config import API_KEY

def get_weather(city, state, country="US"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": f"{city},{state},{country}",
        "appid": API_KEY,
        "units": "imperial"
    }
    
    response = requests.get(url, params=params)
    
    print(response.status_code)
    print(response.json())

get_weather("West Chester", "PA", "US")

