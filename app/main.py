import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Pronóstico", layout="wide")

def main():
    st.title("Pronóstico de Casos de Enfermedades Respiratorias Agudas")
    st.sidebar.header("Secciones")
    
    section = st.sidebar.radio("Ir a", ["Inicio", "Análisis de Datos", "Predicciones", "Acerca de"])
    if section == "Inicio":
        st.header("Muela del objetivo del proyecto")
        st.expander("_Hello_ there")


    if section == "Análisis de Datos":
        st.header("Visualización de los datos por mes")
        st.header("Visualización incidencia de casos por provincias")
        st.header("Mostrar Estadísticas de los datos")
        st.header("Mostrar algun dataframe")

    if section == "Predicciones":
        st.header("AutoML resultados")
        st.header("RNN resultados")
        st.header("ARIMA resultados")
        st.header("XGBoost resultados")
    

if __name__ == '__main__':
    main()