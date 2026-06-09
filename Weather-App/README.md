
# Weather-App

A Python CLI app I built to familiarize myself with core API skills:

- Signing up for and using an API key
- Making HTTP requests to fetch data using Python's `requests` library
- Reading and parsing JSON responses
- Handling API errors (invalid city, bad key, network issues, etc.)

At this time, I have completed all four goals:
* ✅ Signing up for and using an API key
* ✅ Making HTTP requests with `requests`
* ✅ Reading and parsing JSON responses
* ✅ Handling API errors

## Requirements
- Python 3
- `requests`
- `python-dotenv`

## Setup
1. Clone the repo
2. Install dependencies:
   ```
   pip3 install requests python-dotenv
   ```
3. Create a `.env` file in the project root:
   ```
   OPENWEATHER_API_KEY=your_key_here
   ```

## Usage
```
python3 main.py "City Name" STATE
```

**Examples:**
```
python3 main.py Philadelphia PA
python3 main.py "New York City" NY
python3 main.py "Los Angeles" CA
```

## Project Structure
```
Weather-App/
├── main.py       # Entry point, handles command-line arguments
├── weather.py    # Fetches and parses weather data from API
├── config.py     # Loads API key from .env file
└── .env          # Stores API key (not tracked by Git)


