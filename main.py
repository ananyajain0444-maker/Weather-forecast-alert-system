import os
from src.fetch_weather import fetch_weather
from src.analyze import analyze_data
from src.alerts import generate_alerts
from src.visualize import generate_charts

def main():
    print("🚀 Fetching weather data...\n")

    data = fetch_weather()
    df = analyze_data(data)

    if df.empty:
        print("❌ No data received. Exiting...")
        return

    # Generate Alerts
    alerts = generate_alerts(df)

    print("📊 ALERTS:")
    if alerts:
        for alert in alerts:
            print(f"⚠️ {alert}")
    else:
        print("✅ No major alerts")

    # Save CSV
    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/weather.csv", index=False)

    # Generate Charts (4 images)
    generate_charts(df)

    print("\n✅ Outputs generated successfully!")
    print("📁 Check images/ and outputs/ folders")

if __name__ == "__main__":
    main()