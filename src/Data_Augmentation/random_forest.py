import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

path_csv = os.path.join(os.path.dirname(__file__), 'example_input.csv')
output_path = os.path.join(os.path.dirname(__file__), 'example_output.csv')

raw_data = pd.read_csv(path_csv, parse_dates=["Date"])
raw_data = raw_data.sort_values("Date")


# Generar un rango completo de fechas
date_range = pd.date_range(start=raw_data["Date"].min(), end=raw_data["Date"].max(), freq="D")
data_full = pd.DataFrame(date_range, columns=["Date"])

# Combinar los datos originales con el rango completo
data_full = data_full.merge(raw_data, on="Date", how="left")

# Crear otras características temporales para el modelo
data_full["Day"] = data_full["Date"].dt.day
data_full["Month"] = data_full["Date"].dt.month
data_full["Year"] = data_full["Date"].dt.year
data_full["DayOfYear"] = data_full["Date"].dt.dayofyear

# Separar los datos conocidos y desconocidos
known_data = data_full.dropna(subset=["Value"])
missing_data = data_full[data_full["Value"].isna()]

# Separar características y etiquetas
X_known = known_data[["Day", "Month", "Year", "DayOfYear"]]
y_known = known_data["Value"]
X_missing = missing_data[["Day", "Month", "Year", "DayOfYear"]]

# Entrenar el modelo, con todos los datos conocidos para predecir los faltantes
# ? Verificar los valores de los hiperparámetros
model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X_known, y_known)

missing_data["Value"] = model.predict(X_missing)
missing_data["Value"] = missing_data["Value"].round().astype(int)

data_full.update(missing_data)

data_full.to_csv(output_path, index=False)
print("Datos completados guardados en 'data.csv'.")