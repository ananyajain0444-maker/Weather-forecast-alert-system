import matplotlib.pyplot as plt
import os

def generate_charts(df):
    os.makedirs("images", exist_ok=True)

    # 1️⃣ Temperature Chart
    plt.figure()
    plt.plot(df['temp'][:24])
    plt.title("Temperature Forecast (24 Hours)")
    plt.xlabel("Hour")
    plt.ylabel("Temperature (°C)")
    plt.savefig("images/temp_chart.png")
    plt.close()

    # 2️⃣ Humidity Chart
    plt.figure()
    plt.plot(df['humidity'][:24])
    plt.title("Humidity Levels (24 Hours)")
    plt.xlabel("Hour")
    plt.ylabel("Humidity (%)")
    plt.savefig("images/humidity_chart.png")
    plt.close()

    # 3️⃣ Rain Probability Chart
    plt.figure()
    plt.plot(df['rain_prob'][:24])
    plt.title("Rain Probability (24 Hours)")
    plt.xlabel("Hour")
    plt.ylabel("Rain Probability (%)")
    plt.savefig("images/rain_chart.png")
    plt.close()

    # 4️⃣ Combined Chart
    plt.figure()
    plt.plot(df['temp'][:24], label="Temperature")
    plt.plot(df['humidity'][:24], label="Humidity")
    plt.plot(df['rain_prob'][:24], label="Rain %")

    plt.title("Combined Weather Analysis")
    plt.xlabel("Hour")
    plt.legend()
    plt.savefig("images/combined_chart.png")
    plt.close()