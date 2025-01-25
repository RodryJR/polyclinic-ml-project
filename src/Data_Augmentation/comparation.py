import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import os

path_csv = os.path.join(os.path.dirname(__file__), 'example_input.csv')
output_path = os.path.join(os.path.dirname(__file__), 'example_output_allmodels.csv')

# Cargar los datos
raw_data = pd.read_csv(path_csv, parse_dates=["Date"])
raw_data = raw_data.sort_values("Date")

# Generar un rango completo de fechas
date_range = pd.date_range(start=raw_data["Date"].min(), end=raw_data["Date"].max(), freq="D")
data_full = pd.DataFrame(date_range, columns=["Date"])

# Combinar los datos originales con el rango completo
data_full = data_full.merge(raw_data, on="Date", how="left")

# Crear características temporales para el modelo
data_full["Day"] = data_full["Date"].dt.day
data_full["Month"] = data_full["Date"].dt.month
data_full["Year"] = data_full["Date"].dt.year
data_full["DayOfYear"] = data_full["Date"].dt.dayofyear

# Separar los datos conocidos y desconocidos
known_data = data_full.dropna(subset=["Value"])
missing_data = data_full[data_full["Value"].isna()]

if len(known_data) == 0 or len(missing_data) == 0:
    raise ValueError("No hay suficientes datos conocidos o faltantes para entrenar el modelo.")

# Separar características y etiquetas
X_known = known_data[["Day", "Month", "Year", "DayOfYear"]]
y_known = known_data["Value"]
X_missing = missing_data[["Day", "Month", "Year", "DayOfYear"]]


### Random Forest 
model_rf = RandomForestRegressor(random_state=42, n_estimators=100)
model_rf.fit(X_known, y_known)

missing_data["Value_RF"] = model_rf.predict(X_missing)



### Regresión Lineal 
model_lr = LinearRegression()
model_lr.fit(X_known, y_known)
missing_data["Value_LR"] = model_lr.predict(X_missing)



### Interpolación 

data_interpolation = data_full.copy()
data_interpolation.set_index("Date", inplace=True)
data_interpolation["Value"] = data_interpolation["Value"].interpolate(method="time")
data_interpolation.reset_index(inplace=True)


# Guardar los resultados combinados

data_full["Value_RF"] = missing_data["Value_RF"].round().astype(int)
data_full["Value_LR"] = missing_data["Value_LR"].round().astype(int)
data_full["Value_Interp"] = data_interpolation["Value"].round().astype(int)

# ---

plt.figure(figsize=(14, 7))
plt.plot(data_full["Date"], data_full["Value"], label="Datos originales", color="black")
plt.plot(data_full["Date"], data_full["Value_RF"], label="Random Forest", color="blue", linestyle="--")
plt.plot(data_full["Date"], data_full["Value_LR"], label="Regresión Lineal", color="green", linestyle="--")
plt.plot(data_full["Date"], data_full["Value_Interp"], label="Interpolación", color="red", linestyle="--")

plt.xlabel("Fecha")
plt.ylabel("Valor")
plt.title("Comparación de métodos de imputación de datos faltantes")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# export the results
data_full.to_csv(output_path, index=False)