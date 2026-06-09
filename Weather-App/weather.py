import requests
from config import API_KEY

def get_weather(city, state, country="US"): # function to get weather data for a given city, state, and country (default is US)
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": f"{city},{state},{country}",
        "appid": API_KEY,  # API key is passed as a parameter for authentication
        "units": "imperial"
    }
    
    try: 
        response = requests.get(url, params=params, timeout=5)  # Make the API request with a timeout of 5 seconds

        if response.status_code == 401:
            print("Error: Invalid API key. Check your .env file.")
            return
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Check the city and state.")
            return
        elif response.status_code != 200:
            print(f"Unexpected error: {response.status_code}")
            return

        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        print(f"\nWeather in {weather['city']}:")
        print(f"  Temperature : {weather['temperature']}°F")
        print(f"  Feels like  : {weather['feels_like']}°F")
        print(f"  Humidity    : {weather['humidity']}%")
        print(f"  Conditions  : {weather['description'].capitalize()}")
        print(f"  Wind speed  : {weather['wind_speed']} mph\n")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again.")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected network error: {e}")


#get_weather("West Chester", "PA", "US")
#get_weather("FakeCity", "FakeState", "US")  # Test with an invalid city to trigger error handling

