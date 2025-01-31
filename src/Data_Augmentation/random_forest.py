import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

def random_forest_augmentation(input_csv, output_csv):
    """
    Completes missing values in a CSV file containing date and multiple value columns 
    using a Random Forest regression model.

    Parameters:
    input_csv (str): Path to the input CSV file with date and value columns.
    output_csv (str): Path to the output CSV file where completed data will be saved.
    """
    raw_data = pd.read_csv(input_csv, parse_dates=["Date"])
    raw_data = raw_data.sort_values("Date")

    date_range = pd.date_range(start=raw_data["Date"].min(), end=raw_data["Date"].max(), freq="D")
    data_full = pd.DataFrame(date_range, columns=["Date"])

    data_full = data_full.merge(raw_data, on="Date", how="left")

    # ? Crear otras características temporales para el modelo
    data_full["Day"] = data_full["Date"].dt.day
    data_full["Month"] = data_full["Date"].dt.month
    data_full["Year"] = data_full["Date"].dt.year
    data_full["DayOfYear"] = data_full["Date"].dt.dayofyear

    known_data = data_full.dropna(subset=data_full.columns[1:])  # Excluyendo la columna 'Date'
    missing_data = data_full[data_full[data_full.columns[1:]].isna().any(axis=1)]

    X_known = known_data[["Day", "Month", "Year", "DayOfYear"]]
    
    for column in known_data.columns[1:]:
        y_known = known_data[column]
        X_missing = missing_data[["Day", "Month", "Year", "DayOfYear"]]

        # Entrenar el modelo, con todos los datos conocidos para predecir los faltantes
        # ? Verificar los valores de los hiperparámetros
        model = RandomForestRegressor(random_state=42, n_estimators=100)
        model.fit(X_known, y_known)

        missing_data[column] = model.predict(X_missing).round().astype(int)

    data_full.update(missing_data)

    data_full.to_csv(output_csv, index=False)
    print(f"Data Augmentation finished'{output_csv}'.")

