import requests
import csv
from collections import defaultdict
import os

def fetch_data_frost():

    """
    Henter og lagrer daglige værdata fra Frost API for en gitt periode.

    Funksjonen bruker MET Norway sitt Frost API for å hente observasjoner for værstasjonen SN18700.
    Den samler inn daglige gjennomsnitt for temperatur, vindhastighet, vindretning, relativ luftfuktighet,
    lufttrykk ved havnivå, og daglig nedbør. Dataene aggregeres etter dato og lagres som en CSV-fil
    i katalogen `data/raw/frost_data.csv`.

    Bruker autentisering via en klient-ID og sender en GET-forespørsel til Frost API.
    Dersom forespørselen lykkes, struktureres og lagres dataene. Hvis ikke, skrives en feilmelding ut.

    CSV-filen inneholder følgende kolonner:
    - Date
    - Temperature
    - Wind Speed
    - Wind Direction
    - Precipitation
    - Humidity
    - Pressure

    Avhengigheter:
        - requests
        - csv
        - collections.defaultdict
        - os
    """
      
    client_id = "c533be15-1b26-4225-bf7d-cc5e5c81beb5"
    endpoint = "https://frost.met.no/observations/v0.jsonld"

    start = "2020-01-01"
    end = "2025-01-31"

    # P1D krever at vi bruker sum(...) eller mean(...)
    elements = {
        'mean(air_temperature P1D)': 'Temperature',
        'mean(wind_speed P1D)': 'Wind Speed',
        'mean(wind_from_direction P1D)': 'Wind Direction',
        'sum(precipitation_amount P1D)': 'Precipitation',
        'mean(relative_humidity P1D)': 'Humidity',
        'mean(air_pressure_at_sea_level P1D)': 'Pressure'
    }

    print(f"Henter daglige data for perioden {start} til {end} ...")

    params = {
        'sources': 'SN18700',
        'elements': ','.join(elements.keys()),
        'referencetime': f'{start}/{end}',
        'timeresolutions': 'P1D',
        'fields': 'referenceTime,elementId,value'
    }

    response = requests.get(endpoint, params=params, auth=(client_id, ''))

    if response.status_code == 200:
        data = response.json().get('data', [])
        combined = defaultdict(dict)

        for entry in data:
            time = entry.get('referenceTime')[:10]  # Hent kun dato-delen
            for obs in entry.get('observations', []):
                element = obs.get('elementId')
                value = obs.get('value')
                label = elements[element]
                combined[time][label] = value

        os.makedirs("data/raw", exist_ok=True)

        with open("data/raw/frost_data.csv", mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Date'] + list(elements.values())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for date in sorted(combined.keys()):
                row = {'Date': date}
                for label in elements.values():
                    row[label] = combined[date].get(label)
                writer.writerow(row)

        print("Daglige data lagret i 'data/raw/frost_data.csv'")

    else:
        print(f"Feil {response.status_code}: {response.text}")
