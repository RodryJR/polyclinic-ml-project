import pandas as pd
import os

# Definir los nombres de las columnas
columnas = [
    'Provincias', 'Hogar_I_Total', 'Hogar_I_<19años', 'Hogar_A_Recuperados', 
    'Hogar_A_Remitidos_ingreso_institucional', 'Hogar_A_Fallecidos', 'Hogar_A_Total', 
    'Hogar_PI_Total', 'Hogar_PI_<19años', 'Policlinico_I_Total', 'Policlinico_I_<19años', 
    'Policlinico_A_Recuperados', 'Policlinico_A_Remitidos_ingreso_hospitalario', 
    'Policlinico_A_Fallecidos', 'Policlinico_A_Total', 'Policlinico_PI_Total', 
    'Policlinico_PI_<19años', 'TotalAPS_I_Total', 'TotalAPS_I_<19años', 
    'TotalAPS_A_Recuperados', 'TotalAPS_A_Remitidos', 'TotalAPS_A_Fallecidos', 
    'TotalAPS_A_Total', 'TotalAPS_PI_Total', 'TotalAPS_PI_<19años', 'PIDA_hogar', 
    'PIDA_hogar_<19años', 'PIDA_hospitalización', 'PIDA_hospitalización_<19años', 
    'Validación_PIactual', 'ADAH_Ingresos', 'ADAH_AltasRecuperados', 'ADAH_Fallecidos', 
    'DH_Ingresos', 'DH_AltasRecuperados', 'DH_Fallecidos', 'AAH_Ingresos', 
    'AAH_AltasRecuperados', 'AAH_Fallecidos', 'ADAP_Ingresos', 'ADAP_AltasRecuperados', 
    'ADAP_Fallecidos', 'DP_Ingresos', 'DP_AltasRecuperados', 'DP_Fallecidos', 
    'AAP_Ingresos', 'AAP_AltasRecuperados', 'AAP_Fallecidos', 'AATotalAPS_Ingresos', 
    'AATotalAPS_AltasRecuperados', 'AATotalAPS_Fallecidos', 'Dia', 'Mes', 'Año'
]
# I= Ingresos del dia
# A= Altas del dia
# PI= Permanecen ingresados
# PIDA= Permanecen ingresados del dia anterior
# ADAH= Acumulado hasta el dia anterior en el hogar
# DH= Dia en el hogar
# AAH= Acumulado Actual En el Hogar
# ADAP= Acumulado hasta el dia anterior Policlínicos con Serv. de hosp.
# DP= Dia en Policlínicos con Servicios de hospitalización
# AAP= Acumulado Actual Pol. Con serv. Hosp.
# AATotalAPS= Acumulado Actual TOTAL APS

# Crear un DataFrame vacío con las columnas
df = pd.DataFrame()

# Ruta donde se encuentran los archivos Excel
folder_path = "Anexos_Circular_ML"

# Lista para almacenar los DataFrames
dataframes = []

# Cargar cada archivo Excel en la carpeta
for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        df_sheet = pd.read_excel(file_path, sheet_name='Atención Primaria',header=None,engine='xlrd')
        dataframes.append(df_sheet)

for dataf in dataframes:

    fila_sexta = dataf.iloc[5]  # Índice 5 porque el índice empieza en 0
    valores = fila_sexta[[1, 2, 3]]  # Columnas en posición 1, 2 y 3
    valores_list = valores.tolist()
    # Eliminar columnas por índice
    dataf = dataf.drop(dataf.columns[[25,31]], axis=1)  
    filas_extraidas = dataf.iloc[9:26]  # Incluye desde x hasta y

    # Añadir las columnas con los valores 
    filas_extraidas['Día'] = valores_list[0]
    filas_extraidas['Mes'] = valores_list[1]
    filas_extraidas['Año'] = valores_list[2]

    df = pd.concat([df, filas_extraidas], ignore_index=True)

# Guardar el DataFrame en un archivo .csv
df.columns=columnas
df.to_csv('anexo_circular_7_atencion_primaria.csv', index=False, encoding='utf-8')