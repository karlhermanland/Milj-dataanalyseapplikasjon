import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import pandas as pd

from src.fetch_data_nasa import fetch_nasa_data

class TestFetchNasaData(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("pandas.DataFrame.to_csv")
    @patch("requests.get")
    def test_fetch_nasa_data_success(self, mock_get, mock_to_csv, mock_file):
        """Tester at fetch_nasa_data fungerer som forventet når API svarer OK"""

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "properties": {
                "parameter": {
                    "ALLSKY_SFC_SW_DWN": {
                        "2020-01-01": 100.0,
                        "2020-01-02": 110.0
                    },
                    "TS": {
                        "2020-01-01": 3.2,
                        "2020-01-02": 3.4
                    },
                    "QV2M": {
                        "2020-01-01": 0.6,
                        "2020-01-02": 0.7
                    },
                    "PS": {
                        "2020-01-01": 1012,
                        "2020-01-02": 1011
                    }
                }
            }
        }

        mock_get.return_value = mock_response

        fetch_nasa_data()

        mock_get.assert_called_once()
        mock_to_csv.assert_called_once()  # Sjekker at vi forsøkte å lagre til fil

    @patch("requests.get")
    def test_fetch_nasa_data_failure(self, mock_get):
        """Tester at fetch_nasa_data håndterer feilrespons (f.eks. 500) korrekt"""

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        fetch_nasa_data()

        mock_get.assert_called_once()  # Vi har gjort kall
        # Ingen unntak betyr testen bestod

if __name__ == "__main__":
    unittest.main()
