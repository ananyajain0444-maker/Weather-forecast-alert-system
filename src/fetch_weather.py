import requests

LAT = 28.61   # Delhi
LON = 77.23

URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=temperature_2m,relative_humidity_2m,precipitation_probability"

def fetch_weather():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("❌ Error fetching weather:", e)
        return {}