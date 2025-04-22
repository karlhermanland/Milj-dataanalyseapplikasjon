# Ettersom tilstanden er tilbakestilt, må vi laste inn og kjøre hele scriptet med ComfortIndex-analyse på nytt

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import timedelta
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    mean_absolute_percentage_error,
)

# Stil
sns.set(style="whitegrid")

# --- 1. Last inn data ---
file_path = Path("data/clean/merged_data.csv")
df = pd.read_csv(file_path, parse_dates=["Date"])
df.drop(columns=["Unnamed:_0", "Wind_Direction"], inplace=True, errors="ignore")
df.fillna(df.mean(numeric_only=True), inplace=True)
df = df.sort_values("Date")

# --- 2. Legg til dato-funksjoner ---
df["Month"] = df["Date"].dt.month
df["DayOfYear"] = df["Date"].dt.dayofyear
df["Sin_Day"] = np.sin(2 * np.pi * df["DayOfYear"] / 365)
df["Cos_Day"] = np.cos(2 * np.pi * df["DayOfYear"] / 365)

# --- 3. SVR: Temperatur og Solinnstråling ---
features = [
    "Humidity", "Pressure", "ALLSKY_SFC_SW_DWN", "TS", "QV2M", "PS", "Month", "Sin_Day", "Cos_Day"
]
X = df[features]
y_temp = df["Temperature"]
y_solar = df["ALLSKY_SFC_SW_DWN"]

scaler_X = StandardScaler()
scaler_y_temp = StandardScaler()
scaler_y_solar = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_temp_scaled = scaler_y_temp.fit_transform(y_temp.values.reshape(-1, 1)).flatten()
y_solar_scaled = scaler_y_solar.fit_transform(y_solar.values.reshape(-1, 1)).flatten()

model_temp = SVR(kernel="rbf")
model_solar = SVR(kernel="rbf")
model_temp.fit(X_scaled, y_temp_scaled)
model_solar.fit(X_scaled, y_solar_scaled)

# --- 4. Prediksjon 1 år frem i tid ---
num_days = 365
start_date = df["Date"].max()
future_rows = []

for i in range(num_days):
    future_date = start_date + timedelta(days=i + 1)
    month = future_date.month
    day_of_year = future_date.timetuple().tm_yday
    sin_day = np.sin(2 * np.pi * day_of_year / 365)
    cos_day = np.cos(2 * np.pi * day_of_year / 365)

    sample_input = df[df["Month"] == month][features].sample(1).iloc[0].copy()
    sample_input["Month"] = month
    sample_input["Sin_Day"] = sin_day
    sample_input["Cos_Day"] = cos_day

    scaled_input = scaler_X.transform([sample_input])
    pred_temp_scaled = model_temp.predict(scaled_input)[0]
    pred_solar_scaled = model_solar.predict(scaled_input)[0]

    pred_temp = scaler_y_temp.inverse_transform([[pred_temp_scaled]])[0, 0]
    pred_solar = scaler_y_solar.inverse_transform([[pred_solar_scaled]])[0, 0]

    future_rows.append({
        "Date": future_date,
        "Pred_Temperature": pred_temp,
        "Pred_Solar": pred_solar
    })

future_df = pd.DataFrame(future_rows)
future_df["Smooth_Temperature"] = future_df["Pred_Temperature"].rolling(window=7, center=True).mean()
future_df["Smooth_Solar"] = future_df["Pred_Solar"].rolling(window=7, center=True).mean()

# --- 5. ComfortIndex-analyse ---
comfort_features = [
    "Temperature", "Wind_Speed", "Humidity", "Pressure",
    "ALLSKY_SFC_SW_DWN", "TS", "QV2M", "PS"
]
X_comfort = df[comfort_features]
y_comfort = df["ComfortIndex"]
X_train, X_test, y_train, y_test = train_test_split(X_comfort, y_comfort, test_size=0.2, random_state=42)

comfort_model = LinearRegression()
comfort_model.fit(X_train, y_train)
y_pred = comfort_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("📊 ComfortIndex-modellens ytelse:")
print(f" - MSE:  {mse:.2f}")
print(f" - MAE:  {mae:.2f}")
print(f" - MAPE: {mape:.2%}")
print(f" - R²:   {r2:.2f}")

# --- 6. Lag alle visualiseringene ---
import seaborn as sns

plt.figure(figsize=(6, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_comfort.min(), y_comfort.max()], [y_comfort.min(), y_comfort.max()], "r--")
plt.xlabel("Faktisk ComfortIndex")
plt.ylabel("Predikert ComfortIndex")
plt.title("Predikert vs Faktisk ComfortIndex")
plt.tight_layout()
plt.savefig("plot_pred_vs_actual.png")

residuals = y_test - y_pred
plt.figure(figsize=(8, 4))
sns.histplot(residuals, kde=True, bins=20, color="orange")
plt.title("Fordeling av residualer")
plt.xlabel("Feil (Residual)")
plt.ylabel("Antall observasjoner")
plt.tight_layout()
plt.savefig("plot_residuals.png")

plt.figure(figsize=(8, 5))
scatter = plt.scatter(df["Temperature"], df["ComfortIndex"], c=df["Humidity"], cmap="viridis")
cbar = plt.colorbar(scatter)
cbar.set_label("Luftfuktighet (%)")
plt.title("Temperatur vs ComfortIndex")
plt.xlabel("Temperatur (°C)")
plt.ylabel("ComfortIndex")
plt.tight_layout()
plt.savefig("plot_temp_vs_comfortindex.png")

plt.figure(figsize=(12, 5))
plt.plot(future_df["Date"], future_df["Smooth_Temperature"], label="Glattet Temperatur", linestyle="--")
plt.title("SVR-prediksjon: Temperatur for neste år")
plt.xlabel("Dato")
plt.ylabel("Temperatur (°C)")
plt.legend()
plt.tight_layout()
plt.savefig("svr_forecast_temperature_smoothed.png")

plt.figure(figsize=(12, 5))
plt.plot(future_df["Date"], future_df["Smooth_Solar"], label="Glattet Solinnstråling", linestyle="--")
plt.title("SVR-prediksjon: Solinnstråling for neste år")
plt.xlabel("Dato")
plt.ylabel("ALLSKY_SFC_SW_DWN (W/m²)")
plt.legend()
plt.tight_layout()
plt.savefig("svr_forecast_solar_smoothed.png")
