import numpy as np
import pandas as pd
import os
import logging as LOG
from xgboost_utils import split_data,create_features,train_and_evaluate,train_and_evaluate_multiple_targets,plot_model_performance
from scipy.stats import ttest_rel
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error, r2_score

log_directory = os.path.join(os.path.dirname(__file__), "logs")

LOG.basicConfig(
    level=LOG.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        LOG.FileHandler(os.path.join(log_directory, "xgb_logs.txt"), mode="w")  # Guarda logs en un archivo
    ]
)

def xgboost_model(df, int_cols,target_cols,show_graph=False):

    train_data ,test_data = split_data(df,0.8)
    
    train_data = train_data[int_cols]
    test_data = test_data[int_cols]

    # Generar características para entrenamiento y prueba
    train_data = create_features(train_data, target_cols,lags=1,wind=2)
    test_data = create_features(test_data, target_cols,lags=1,wind=2)

    models, predictions, rmse, mse, mae, r2 = train_and_evaluate_multiple_targets(train_data, test_data, target_cols)

    LOG.info("RMSE: %s", rmse)
    LOG.info("MSE: %s", mse)
    LOG.info("MAE: %s", mae)
    LOG.info("R2 Score: %s", r2)

    if show_graph:
        plot_model_performance(test_data,target_cols,predictions)

    return models,predictions, rmse, mse, mae, r2

def main():
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

    # Seleccionar solo las columnas que te interesan
    columnas_interes_pais = ['Date','total_aps_i_pais']
    # # Seleccionar solo las columnas que te interesan
    # columnas_interes_provincias = [
    #     "Date",
    #     'Pinar del Rio',
    #     'Artemisa',
    #     'La Habana',
    #     'Mayabeque',
    #     'Matanzas',
    #     'Villa Clara',
    #     'Cienfuegos',
    #     'Sancti Spiritus',
    #     'Ciego de Ávila',
    #     'Camagüey',
    #     'Las Tunas',
    #     'Holguin',
    #     'Granma',
    #     'Santiago de Cuba',
    #     'Guantánamo',
    #     'Isla de la Juventud'
    # ]

    # Columnas objetivo
    target_cols_pais = ['total_aps_i_pais']
    # target_cols_provincia = ['Pinar del Rio','Artemisa','La Habana','Mayabeque','Matanzas','Villa Clara','Cienfuegos','Sancti Spiritus','Ciego de Ávila','Camagüey','Las Tunas','Holguin','Granma','Santiago de Cuba','Guantánamo','Isla de la Juventud']
    num_runs = 30
    errors = []


    for i in range(num_runs):
        LOG.info(f"Ejecutando XGBoost - Iteración {i + 1}")
        _, _, rmse, mse, mae, r2 = xgboost_model(df, columnas_interes_pais,target_cols_pais,show_graph=False)
        errors.append(mse)

    base_error = errors[0]  # Compare with first iteration
    t_stat, p_value = ttest_rel(errors[1:], [base_error] * (num_runs - 1))

    LOG.info(f"T-statistic: {t_stat:.6f}")
    LOG.info(f"P-value: {p_value:.6f}")

    if p_value < 0.05:
        LOG.info("Los resultados de XGBoost varían significativamente entre ejecuciones (p < 0.05).")
    else:
        LOG.info("No hay suficiente evidencia para decir que los resultados de XGBoost cambian significativamente.")

if __name__ == "__main__":
    main()