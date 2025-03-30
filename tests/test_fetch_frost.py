import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
from src.fetch_data_frost import fetch_data_frost

class TestFetchDataFrost(unittest.TestCase):

    def setUp(self):
        self.output_path = "data/raw/frost_data.csv"
        os.makedirs("data/raw", exist_ok=True)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    @patch("src.fetch_data_frost.requests.get")
    def test_fetch_data_creates_csv_file(self, mock_get):
        # Simulert API-respons med struktur som Frost bruker
        mock_data = {
            "data": [
                {
                    "referenceTime": "2020-01-01T00:00:00Z",
                    "observations": [
                        {"elementId": "mean(air_temperature P1D)", "value": 5.2},
                        {"elementId": "mean(wind_speed P1D)", "value": 3.4},
                        {"elementId": "mean(wind_from_direction P1D)", "value": 120},
                        {"elementId": "sum(precipitation_amount P1D)", "value": 1.0},
                        {"elementId": "mean(relative_humidity P1D)", "value": 85},
                        {"elementId": "mean(air_pressure_at_sea_level P1D)", "value": 1013.2},
                    ]
                }
            ]
        }

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Kjør funksjonen
        fetch_data_frost()

        # Sjekk at filen faktisk ble opprettet
        self.assertTrue(os.path.exists(self.output_path))

        # Sjekk innholdet i CSV
        df = pd.read_csv(self.output_path)
        expected_columns = ['Date', 'Temperature', 'Wind Speed', 'Wind Direction', 'Precipitation', 'Humidity', 'Pressure']
        self.assertListEqual(list(df.columns), expected_columns)
        self.assertEqual(df.iloc[0]['Date'], '2020-01-01')

    @patch("src.fetch_data_frost.requests.get")
    def test_fetch_data_handles_api_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        # Skal ikke kaste feil selv om API feiler, men skrive til konsoll
        try:
            fetch_data_frost()
        except Exception as e:
            self.fail(f"Funksjonen kastet en feil ved API-feil: {e}")

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

if __name__ == '__main__':
    unittest.main()
