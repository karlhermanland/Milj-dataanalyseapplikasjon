
import os
from src.fetch_data_nasa import fetch_nasa_data
from src.fetch_data_frost import fetch_data_frost
from src.clean_data import clean_and_merge_weather_data

def main():
    print("Starter datarensing og sammenkobling...")

    # Sørg for at output-mappen finnes
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/clean", exist_ok=True)


    #Hent data
    fetch_nasa_data()
    fetch_data_frost()

if __name__ == "__main__":
    main()