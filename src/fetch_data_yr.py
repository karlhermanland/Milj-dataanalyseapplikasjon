import requests
import pandas as pd

def fetch_yr_data():
    # API-endepunkt for Yr (sanntidsvær)
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

    # Lokasjonsparametere (endre til ønsket sted)
    params = {
        "lat": 59.0,  # Breddegrad
        "lon": 10.0   # Lengdegrad
    }

    # Headers - Krever User-Agent (Yr blokkerer anonyme forespørsler)
    headers = {
        "User-Agent": "MiljodataApplikasjon/1.0 (kontakt@dinemail.com)"  # Endre til din kontaktinfo
    }

    # Hente data
    response = requests.get(url, params=params, headers=headers)

    # Sjekke respons
    if response.status_code == 200:
        data = response.json()

        # Hente ut time-for-time værdata
        timeseries = data["properties"]["timeseries"]

        # Konvertere til DataFrame
        weather_data = []
        for entry in timeseries:
            time = entry["time"]
            details = entry["data"]["instant"]["details"]

            # Hent spesifikke værdata
            temp = details.get("air_temperature", None)
            wind_speed = details.get("wind_speed", None)
            wind_direction = details.get("wind_from_direction", None)
            precipitation = entry["data"].get("next_1_hours", {}).get("details", {}).get("precipitation_amount", 0)
            humidity = details.get("relative_humidity", None)
            pressure = details.get("air_pressure_at_sea_level", None)

            weather_data.append([time, temp, wind_speed, wind_direction, precipitation, humidity, pressure])

        # Opprette DataFrame med flere værparametere
        df = pd.DataFrame(weather_data, columns=["Time", "Temperature", "Wind Speed", "Wind Direction", "Precipitation", "Humidity", "Pressure"])

        # Konverter 'Time' til datetime-format
        df["Time"] = pd.to_datetime(df["Time"])

        # Lagre til CSV
        df.to_csv("data/raw/yr_extended_weather_data.csv", index=False)
        print("Data lagret som yr_extended_weather_data.csv")

    else:
        print(f"Feil: {response.status_code}, {response.text}")
