import argparse
from weather import get_weather

def main():
    parser = argparse.ArgumentParser(description="Get current weather for a city.")
    parser.add_argument("city", help="City name e.g. Philadelphia")
    parser.add_argument("state", help="State code e.g. PA")
    parser.add_argument("--country", default="US", help="Country code e.g. US")

    args = parser.parse_args()

    get_weather(args.city, args.state, args.country)

if __name__ == "__main__":
    main()

    