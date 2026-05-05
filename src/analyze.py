import pandas as pd

def analyze_data(data):
    try:
        hourly = data.get('hourly', {})

        df = pd.DataFrame({
            "time": hourly.get('time', []),
            "temp": hourly.get('temperature_2m', []),
            "humidity": hourly.get('relative_humidity_2m', []),
            "rain_prob": hourly.get('precipitation_probability', [])
        })

        return df

    except Exception as e:
        print("❌ Error analyzing data:", e)
        return pd.DataFrame()