import pandas as pd
from pandasql import sqldf

def clean_and_merge_weather_data(yr_path, nasa_path):
    """
    Leser, renser og kombinerer værdata fra YR og NASA.
    - Fjerner tidssoner
    - Fyller inn manglende verdier med gjennomsnitt
    - Fjerner uregelmessige verdier
    - Lager ny kolonne med list comprehension
    - Bruker iterator og SQL-spørring for analyse
    """

    # ===== 1. Les inn data fra CSV =====
    yr_df = pd.read_csv(yr_path)
    nasa_df = pd.read_csv(nasa_path)

    # ===== 2. Konverter tidskolonner =====
    yr_df["Time"] = pd.to_datetime(yr_df["Time"])

    # Fjern tidssone og normaliser tid -> dato
    yr_df["Date"] = yr_df["Time"].dt.tz_localize(None).dt.normalize()

    nasa_df.rename(columns={nasa_df.columns[0]: "Date"}, inplace=True)
    nasa_df["Date"] = pd.to_datetime(nasa_df["Date"]).dt.normalize()

    # ===== 3. Fyll inn manglende verdier =====
    print("\n Manglende verdier i YR:\n", yr_df.isnull().sum())
    print("\n Manglende verdier i NASA:\n", nasa_df.isnull().sum())

    for col in yr_df.select_dtypes(include="number").columns:
        mean_val = yr_df[col].mean()
        yr_df[col] = yr_df[col].fillna(mean_val)

    for col in nasa_df.select_dtypes(include="number").columns:
        mean_val = nasa_df[col].mean()
        nasa_df[col] = nasa_df[col].fillna(mean_val)

    # ===== 4. Fjern uregelmessigheter =====
    yr_df = yr_df[yr_df["Precipitation"] >= 0]
    yr_df = yr_df[yr_df["Pressure"] >= 900]

    # ===== 5. Slå sammen datasett =====
    merged_df = pd.merge(yr_df, nasa_df, how="inner", on="Date")

    # ===== 6. List comprehension: komfortindeks =====
    merged_df["ComfortIndex"] = [
        round(temp - 0.55 * (1 - hum / 100) * (temp - 14.5), 2)
        for temp, hum in zip(merged_df["Temperature"], merged_df["Humidity"])
    ]

    # ===== 7. Iterator-eksempel =====
    print("\n Eksempel på temperaturer:")
    for i, row in merged_df.iterrows():
        print(f"{row['Date']} → {row['Temperature']} °C")
        if i >= 2:
            break

    # ===== 8. Daglig aggregering med SQL =====
    query = """
        SELECT 
            Date,
            AVG(Temperature) AS avg_temp,
            AVG("Wind Speed") AS avg_wind,
            AVG(Precipitation) AS avg_precip,
            AVG(Humidity) AS avg_humidity,
            AVG(Pressure) AS avg_pressure,
            AVG(ALLSKY_SFC_SW_DWN) AS avg_solar_radiation,
            AVG(ComfortIndex) AS avg_comfort
        FROM merged_df
        GROUP BY Date
    """

    daily_avg = sqldf(query)

    return merged_df, daily_avg
