import xgboost as xgb
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Cargar tu dataset (por ejemplo, desde un archivo CSV)
train_data = pd.read_csv("../../data/total_incomes_augmented_training_data.csv")
test_data = pd.read_csv("../../data/total_incomes_test_data.csv")

    # # Concatenar los DataFrames
df = pd.concat([train_data, test_data], ignore_index=True)
df['Date'] = pd.to_datetime(df['Date'])

    # # Ordenar el DataFrame por la columna 'Date' de más reciente a más antigua
df = df.sort_values(by='Date', ascending=True)
columnas_a_sumar = [
        'Pinar del Rio',
        'Artemisa',
        'La Habana',
        'Mayabeque',
        'Matanzas',
        'Villa Clara',
        'Cienfuegos',
        'Sancti Spiritus',
        'Ciego de Ávila',
        'Camagüey',
        'Las Tunas',
        'Holguin',
        'Granma',
        'Santiago de Cuba',
        'Guantánamo',
        'Isla de la Juventud'
        ]
df['total_aps_i_pais'] = df[columnas_a_sumar].sum(axis=1)

X = pd.DataFrame(df, columns=['Date','total_aps_i_pais'])
y = df['total_aps_i_pais']

X["Year"] = X["Date"].dt.year
X["Month"] = X["Date"].dt.month
X["Day"] = X["Date"].dt.day
X = X.drop(columns=["Date"])

# Convertir a DMatrix de XGBoost
dtrain = xgb.DMatrix(X, label=y, enable_categorical=True)


params = {
    'objective': 'reg:squarederror',  # Para regresión
    'eval_metric': 'rmse',  # Error cuadrático medio
    'max_depth': 3,
    'eta': 0.01,
    'min_child_weight': 15,
    'gamma':0.1,
}

cv_results = xgb.cv(
    params=params,
    dtrain=dtrain,
    num_boost_round=1000,  # Número de árboles
    nfold=5,  # Número de folds
    #early_stopping_rounds=10,  # Para detener si no mejora el rendimiento
    metrics="rmse",
    as_pandas=True,
    seed=42
)

# Mostrar los resultados
print(cv_results)
print(f"Mejor RMSE medio de validación: {cv_results['test-rmse-mean'].min()}")
# Graficar la curva de aprendizaje
plt.figure(figsize=(10, 5))
plt.plot(cv_results.index, cv_results["train-rmse-mean"], label="Train RMSE", linestyle='dashed')
plt.plot(cv_results.index, cv_results["test-rmse-mean"], label="Validation RMSE", color='red')

# Etiquetas y título
plt.xlabel("Boosting Rounds")
plt.ylabel("RMSE")
plt.title("Curva de Aprendizaje - XGBoost")
plt.legend()
plt.grid(True)
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import xgboost as xgb
# from xgboost import XGBRegressor
# from sklearn.model_selection import cross_val_score, KFold
# from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import train_test_split

# # Definir el modelo con los parámetros especificados
# model = XGBRegressor(
#     objective='reg:squarederror',
#     n_estimators=1000, 
#     learning_rate=0.05, 
#     max_depth=7, 
#     min_child_weight=3, 
#     gamma=0.1, 
#     random_state=42
# )

# # Definir K-Fold Cross Validation
# kf = KFold(n_splits=5, shuffle=True, random_state=42)

# # Almacenar RMSE para cada iteración
# rmse_train = []
# rmse_val = []

# # Realizar K-Fold manualmente para graficar curva de aprendizaje
# for train_index, val_index in kf.split(X):
#     X_train, X_val = X.iloc[train_index], X.iloc[val_index]
#     y_train, y_val = y.iloc[train_index], y.iloc[val_index]
    
#     model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
    
#     # Obtener predicciones en train y test
#     y_train_pred = model.predict(X_train)
#     y_val_pred = model.predict(X_val)
    
#     # Calcular RMSE
#     rmse_train.append(mean_squared_error(y_train, y_train_pred))
#     rmse_val.append(mean_squared_error(y_val, y_val_pred))

# # Graficar la curva de aprendizaje
# plt.figure(figsize=(10, 5))
# plt.plot(range(1, kf.get_n_splits() + 1), rmse_train, label="Train RMSE", linestyle='dashed', marker='o')
# plt.plot(range(1, kf.get_n_splits() + 1), rmse_val, label="Validation RMSE", color='red', marker='s')

# # Etiquetas y título
# plt.xlabel("Fold")
# plt.ylabel("RMSE")
# plt.title("Curva de Aprendizaje - K-Fold XGBoost")
# plt.legend()
# plt.grid(True)
# plt.show()

# # Imprimir el promedio del RMSE en validación
# print(f"Promedio de RMSE en validación: {np.mean(rmse_val):.4f}")