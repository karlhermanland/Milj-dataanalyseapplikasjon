import pandas as pd
from pandasql import sqldf
import numpy as np
import os

def clean_and_merge_weather_data(frost_path, nasa_path):
    """
    Leser, renser og kombinerer værdata fra FROST og NASA.
    - Fjerner tidssoner og formaterer datoer
    - Fyller inn manglende verdier med median
    - Fjerner uregelmessige verdier
    - Standardiserer kolonnenavn
    - Sorterer data etter dato
    - Kjører SQL-analyse for aggregert daglig værdata
    """

    print(" Leser inn data fra CSV...")

    # Sjekk at filene finnes
    if not os.path.exists(frost_path):
        raise FileNotFoundError(f"Fil ikke funnet: {frost_path}")
    if not os.path.exists(nasa_path):
        raise FileNotFoundError(f"Fil ikke funnet: {nasa_path}")

    # Les inn data
    frost_df = pd.read_csv(frost_path)
    nasa_df = pd.read_csv(nasa_path)

    # Sjekk at datasettene ikke er tomme
    if frost_df.empty:
        raise ValueError("FROST-datasettet er tomt! Sjekk filen.")
    if nasa_df.empty:
        raise ValueError("NASA-datasettet er tomt! Sjekk filen.")

    print("Data lastet inn!")

    # **ØDELEGGELSE: Simuler dataproblemer for testing**
    print("Introducerer feil for å teste rensing...")
    frost_df.loc[::10, "Temperature"] = np.nan  # Noen temperaturer til NaN
    frost_df.loc[5, "Temperature"] = -999  # Urealistisk temperatur
    frost_df.loc[8, "Humidity"] = 200  # Luftfuktighet over 100%
    frost_df.loc[3, "Date"] = "2020-XX-YY"  # Ugyldig datoformat
    frost_df.loc[6, "Pressure"] = 500  # Ekstremt lavt trykk
    frost_df = frost_df.sample(frac=1).reset_index(drop=True)  # Shuffle data

    print("Feilaktige data generert!")

    print("Rensing av data...")

    # Konverter datoer
    print("Konverterer datoformat...")
    frost_df["Date"] = pd.to_datetime(frost_df["Date"], errors="coerce")
    nasa_df["Date"] = pd.to_datetime(nasa_df["Date"], errors="coerce")

    # Fjern ugyldige datoer
    frost_df = frost_df.dropna(subset=["Date"])
    nasa_df = nasa_df.dropna(subset=["Date"])
    print("Datoer konvertert!")


    # Fyll inn manglende verdier med median
    print("Sjekker og fyller inn manglende verdier...")
    frost_df.fillna(frost_df.median(numeric_only=True), inplace=True)
    nasa_df.fillna(nasa_df.median(numeric_only=True), inplace=True)
    print("Manglende verdier erstattet!")

    # Fjern ekstreme verdier
    print("Fjerner urealistiske verdier...")
    frost_df = frost_df[(frost_df["Temperature"] > -50) & (frost_df["Temperature"] < 50)]
    frost_df = frost_df[(frost_df["Humidity"] >= 0) & (frost_df["Humidity"] <= 100)]
    frost_df = frost_df[(frost_df["Pressure"] >= 900)]
    print("Ugyldige verdier fjernet!")

    # Merge datasettene
    print("Slår sammen FROST- og NASA-data...")
    merged_df = pd.merge(frost_df, nasa_df, how="inner", on="Date")

    # Sorter etter dato
    print("Sorterer datasettet etter dato...")
    merged_df = merged_df.sort_values(by="Date").reset_index(drop=True)
    print("Datasett sortert!")

    # Standardiser kolonnenavn før SQL-analyse
    merged_df.columns = merged_df.columns.str.replace(" ", "_")

    # Beregn komfortindeks
    if "Temperature" in merged_df.columns and "Humidity" in merged_df.columns:
        print("Beregner komfortindeks...")
        merged_df["ComfortIndex"] = [
            round(temp - 0.55 * (1 - hum / 100) * (temp - 14.5), 2)
            for temp, hum in zip(merged_df["Temperature"], merged_df["Humidity"])
        ]
        print("Komfortindeks beregnet!")
    else:
        print("Komfortindeks ikke beregnet (manglende kolonner).")

    # Lagre renset dataset
    os.makedirs("data/clean", exist_ok=True)
    merged_df.to_csv("data/clean/merged_data.csv", index=False)
    print("Sammenflettet dataset lagret i 'data/clean/merged_data.csv'")

    #  SQL-analyse: Daglig aggregering
    print("Kjører SQL-analyse...")
    query = """
        SELECT 
            Date,
            AVG(Temperature) AS avg_temp,
            AVG(Wind_Speed) AS avg_wind,
            AVG(Precipitation) AS avg_precip,
            AVG(Humidity) AS avg_humidity,
            AVG(Pressure) AS avg_pressure,
            AVG(ALLSKY_SFC_SW_DWN) AS avg_solar_radiation,
            AVG(ComfortIndex) AS avg_comfort
        FROM merged_df
        GROUP BY Date
    """
    daily_avg = sqldf(query)
    print("SQL-analyse fullført!")

    return merged_df, daily_avg


# 🔹 Kjør funksjonen dersom scriptet kjøres direkte
if __name__ == "__main__":
    frost_file = "data/raw/frost_data.csv"
    nasa_file = "data/raw/nasa_extended_data.csv"

    print("Starter datarensing og sammenslåing...")
    merged_df, daily_avg = clean_and_merge_weather_data(frost_file, nasa_file)

    print("Funksjonstest fullført! Se de første radene av datasettet:")
    print(merged_df.head())
    print("\nDaglig aggregert data:")
    print(daily_avg.head())

