import unittest
import pandas as pd
import os
from src.clean_data import clean_and_merge_weather_data

class TestCleanData(unittest.TestCase):

    def setUp(self):
        # Oppretter nødvendige mapper for å lagre testfiler
        os.makedirs("data/raw", exist_ok=True)
        os.makedirs("data/clean", exist_ok=True)

        # Oppretter et lite, gyldig FROST-datasett
        frost_data = pd.DataFrame({
            "Date": ["2020-01-01", "2020-01-02", "2020-01-03"],
            "Temperature": [5, 10, 15],
            "Humidity": [40, 50, 60],
            "Precipitation": [1, 0, 3],
            "Pressure": [1000, 1010, 1020],
            "Wind Speed": [3, 4, 5]
        })

        # Oppretter et tilsvarende NASA-datasett
        nasa_data = pd.DataFrame({
            "Date": ["2020-01-01", "2020-01-02", "2020-01-03"],
            "ALLSKY_SFC_SW_DWN": [100, 110, 120],
            "TS": [270, 275, 280],
            "QV2M": [0.005, 0.006, 0.007],
            "PS": [1010, 1020, 1030]
        })

        # Lagrer disse som CSV-filer som funksjonen forventer
        frost_data.to_csv("data/raw/frost_data.csv", index=False)
        nasa_data.to_csv("data/raw/nasa_extended_data.csv", index=False)

    def test_merge_returns_dataframes(self):
        # Tester at funksjonen returnerer to gyldige datasett
        merged, daily = clean_and_merge_weather_data(
            "data/raw/frost_data.csv", "data/raw/nasa_extended_data.csv"
        )
        self.assertIsInstance(merged, pd.DataFrame)  # Sjekker riktig datatype
        self.assertIsInstance(daily, pd.DataFrame)
        self.assertGreater(len(merged), 0)           # Sjekker at data ikke er tomt
        self.assertGreater(len(daily), 0)

    def test_output_file_is_created(self):
        # Kjører funksjonen og tester at den lagrer utdata riktig
        clean_and_merge_weather_data(
            "data/raw/frost_data.csv", "data/raw/nasa_extended_data.csv"
        )
        self.assertTrue(os.path.exists("data/clean/merged_data.csv"))  # Filen skal eksistere

if __name__ == "__main__":
    unittest.main()
