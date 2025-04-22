
import os
import sys
import subprocess
from src.fetch_data_nasa import fetch_nasa_data
from src.fetch_data_frost import fetch_data_frost
from src.clean_data import clean_and_merge_weather_data

def main():

    # Sørg for at output-mappen finnes
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/clean", exist_ok=True)

    #Hent data
    print("Henter data...")
    fetch_nasa_data()
    fetch_data_frost()

    # Definer filstier
    frost_path = "data/raw/frost_data.csv"
    nasa_path = "data/raw/nasa_extended_data.csv"

    # Rens og sammenkoble data
    print("Renser og sammenkobler data...")
    merged_df, daily_avg = clean_and_merge_weather_data(frost_path, nasa_path)

    # Print ut de første radene for å verifisere at alt fungerer
    print("\nSammenslått datasett:")
    print(merged_df.head())

    print("\nDaglig aggregert data:")
    print(daily_avg.head())

    #Kjør analyser og visualiseringer
    print("Kjører prediktiv analyse og lager grafer...")
    import sys
    subprocess.run([sys.executable, "src/train_data.py"], check=True)
    print("Analyse og visualisering fullført! Sjekk .png-filene i prosjektmappen.")



if __name__ == "__main__":
    main()