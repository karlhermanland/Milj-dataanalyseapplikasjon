
import os
from src.clean_data import clean_and_merge_weather_data

def main():
    print("Starter datarensing og sammenkobling...")

    # Sørg for at output-mappen finnes
    os.makedirs("data/clean", exist_ok=True)

    # Kjør datarensing og sammenslåing
    merged_df, daily_avg = clean_and_merge_weather_data(
        "data/raw/yr_extended_weather_data.csv",
        "data/raw/nasa_extended_data.csv"
    )

    # Lagre renset og aggregert data
    merged_df.to_csv("data/clean/cleaned_combined_weather_data.csv", index=False)
    daily_avg.to_csv("data/clean/cleaned_daily_weather_summary.csv", index=False)

    print("Ferdig! Data lagret i 'data/clean/'")

if __name__ == "__main__":
    main()