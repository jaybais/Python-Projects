from dotenv import load_dotenv 
import os 

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("No API key found. Make sure your .env file has OPENWEATHER_API_KEY set.")