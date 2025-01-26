import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Forecast", layout="wide")

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/Anexos_7/total_incomes.csv'))
data = pd.read_csv(data_path)
data['Date'] = pd.to_datetime(data['Date'], format='%Y_%m_%d')

def main():
    st.title("Pronóstico de Casos de Enfermedades Respiratorias Agudas")
    st.sidebar.header("Secciones")
    
    section = st.sidebar.radio("Ir a", 
                                ["Inicio", "Análisis de Datos", "Predicciones", "Acerca de"])
    if section == "Inicio":
        st.header("Objetivo del proyecto")
        st.expander("_Hello_ there")

    if section == "Análisis de Datos":
        st.header("Análisis de Datos")
        st.text("En esta sección se muestra un primer análisis básico de los datos de casos de enfermedades respiratorias agudas por provincia.")
        
        visualization = st.selectbox("Selecciona el tipo de visualización", 
                                      options=["Mostrar DataFrame", "Estadísticas",
                                               "Evolución por mes", "Comparación por provincia"])

        start_date = pd.to_datetime('2022-09-01')
        end_date = pd.to_datetime('2023-12-01')
        filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

        if visualization == "Evolución por mes":
            
            monthly_data = filtered_data.groupby(pd.Grouper(key='Date', freq='M')).sum()
            fig = px.line(monthly_data, x=monthly_data.index, y=monthly_data.columns, title="Evolución de casos por mes")
            st.plotly_chart(fig)

        elif visualization == "Comparación por provincia":
            
            total_by_province = filtered_data.select_dtypes(include='number').sum()

            fig = px.bar(total_by_province, 
                         x=total_by_province.index, 
                         y=total_by_province.values,
                         title="Total de casos por provincia")
            st.plotly_chart(fig)

        elif visualization == "Estadísticas":
            st.write("Estadísticas descriptivas:")
            st.dataframe(filtered_data.describe())
            st.write("Estadísticas descriptivas:")

        elif visualization == "Mostrar DataFrame":
            st.write("Datos originales:")
            st.dataframe(filtered_data)

    if section == "Predicciones":
        st.header("Resultados de AutoML")
        st.header("Resultados de RNN")
        st.header("Resultados de ARIMA")
        st.header("Resultados de XGBoost")

if __name__ == '__main__':
    main()
