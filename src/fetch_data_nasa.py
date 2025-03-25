import requests
import pandas as pd

def fetch_nasa_data():
    # NASA POWER API-endepunkt
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"

    # Gyldige API-parametere – Henter solinnstråling, bakketemperatur, luftfuktighet og lufttrykk
    params = {
        "parameters": "ALLSKY_SFC_SW_DWN,TS,QV2M,PS",  
        "community": "RE",
        "longitude": 10.718, 
        "latitude": 59.943,   # Koordinatene til Oslo-Blindern
        "start": "20200101",  # Startdato (YYYYMMDD)
        "end": "20250130",  # Sluttdato (YYYYMMDD)
        "format": "JSON"
    }

    # Hente data
    response = requests.get(url, params=params)

    # Sjekke respons
    if response.status_code == 200:
        data = response.json()

        # Sjekke at dataene finnes i responsen
        if "properties" in data and "parameter" in data["properties"]:
            parameters = data["properties"]["parameter"]

            # Opprette DataFrame med utvalgte variabler
            df = pd.DataFrame.from_dict(parameters, orient="index").T
            df.index = pd.to_datetime(df.index)  # Konverterer indeksen til datoformat

            # Lagre til CSV
            df.to_csv("data/raw/nasa_extended_data.csv")
            print("Data lagret som nasa_extended_data.csv")

    else:
        print(f"Feil: {response.status_code}, {response.text}")
