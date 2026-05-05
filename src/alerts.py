def generate_alerts(df):
    alerts = []

    try:
        if df['temp'].max() > 35:
            alerts.append("🔥 Heat Alert (Temp > 35°C)")

        if df['rain_prob'].max() > 60:
            alerts.append("🌧️ Rain Alert (High Rain Probability)")

        if df['humidity'].mean() > 80:
            alerts.append("💧 High Humidity Alert")

    except Exception as e:
        alerts.append(f"Error generating alerts: {e}")

    return alerts