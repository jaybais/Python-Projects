# Python Projects
Welcome to my Python Projects repository. It includes three main programs that showcase
core Python and object-oriented programming concepts.


## Projects
- **OOP Demo** - Demonstrates classes, objects, constructors, and inheritance
- **Weather App** - A CLI app that fetches and displays live weather data from the OpenWeatherMap API
- **Tic-Tac-Toe** - A simple game using functions, lists, indexing, and exception handling

## Weather App
A command-line weather app built to develop practical API integration skills in Python.

### What It Does
Enter a city name as a command-line argument and the app fetches and displays live weather
data — including temperature, humidity, and conditions — from the OpenWeatherMap API.

### Skills Demonstrated
- **API key management** — Registered for an OpenWeatherMap API key and stored it securely
  using a `.env` file and the `python-dotenv` library, keeping credentials out of source code
  and version control
- **HTTP requests** — Used Python's `requests` library to make GET requests to the
  OpenWeatherMap API with query parameters (city name, units, API key)
- **JSON parsing** — Parsed the API's JSON response to extract and display relevant fields
  such as temperature, humidity, and weather description
- **Error handling** — Handled a range of failure scenarios:
  - `401 Unauthorized` — invalid or missing API key
  - `404 Not Found` — city not recognized by the API
  - Network errors — no internet connection or request timeout

### How I Built It
1. Signed up for a free OpenWeatherMap account and generated an API key
2. Created a `.env` file to store the key and loaded it at runtime with `python-dotenv`
3. Built `weather.py` to construct the API request URL, send a GET request, and parse
   the JSON response
4. Added error handling for HTTP error codes and network-level failures
5. Built `main.py` to accept a city name as a command-line argument using `sys.argv`
   and pass it to the weather module

### Tools & Libraries
- Python 3
- `requests`
- `python-dotenv`
- OpenWeatherMap API

## Tools & Languages
- Python 3
- OpenWeatherMap API

## Notes
Commit history is not available for the initial projects as they were uploaded
all at once. My SQL and GoLang repositories have more detailed commit histories.
The Weather App was built incrementally with full commit history.
