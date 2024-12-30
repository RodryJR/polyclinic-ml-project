# Comparison of four different time series methods to forecast hepatitis A virus

Este documento compara diferentes métodos de series temporales para predecir infecciones por el virus de la Hepatitis A (HAV), centrándose en su precisión y rendimiento.

## Técnicas Utilizadas y Aspectos Clave

### Métodos de Pronóstico Comparados

El estudio compara cuatro métodos de predicción de series temporales para predecir infecciones de HAV:

- **ARIMA** (Auto-Regressive Integrated Moving Average): Un método estadístico tradicional.
- **MLP** (Multi-Layer Perceptron): Una red neuronal artificial.
- **RBF** (Radial Basis Function): Otro tipo de red neuronal artificial.
- **TDNN** (Time Delay Neural Network): Una red neuronal dinámica.

### Datos

- El estudio utilizó 13 años de registros mensuales de infecciones por HAV en Turquía (enero de 1992 a junio de 2004).
- Los datos se dividieron en:
  - Subconjuntos de entrenamiento, validación cruzada y prueba para los modelos de RNA (redes neuronales artificiales).
  - Datos combinados de entrenamiento y validación cruzada, y un subconjunto de prueba para el modelo ARIMA.

### Modelado ARIMA

- El enfoque ARIMA involucra tres etapas:
  1. Identificación de parámetros.
  2. Estimación de componentes.
  3. Diagnóstico de residuos para garantizar un buen modelo.
- Selección del mejor modelo utilizando el **Criterio de Información de Akaike (AIC)**.
- Modelo elegido: **ARIMA(1,0,1)(0,1,1)**, que incluye componentes no estacionales y estacionales.

### Redes Neuronales Artificiales (RNA)

- **Función General**: Las RNA son aproximadores universales de funciones, adecuados para eventos no lineales en series temporales.
- **TDNN**:
  - Utiliza variables de entrada retrasadas y/o salidas retrasadas de unidades ocultas para el análisis de series temporales.
- **MLP**:
  - Entrenada mediante retropropagación.
  - Configuración del estudio: 2 unidades de entrada, 4 unidades ocultas, 1 unidad de salida.
- **RBF**:
  - Utiliza una función gaussiana en la capa oculta.
  - Configuración del estudio: 2 unidades de entrada, 10 centros de clúster, 1 unidad de salida.

### Evaluación de Modelos

- Métricas utilizadas:
  - **Error Cuadrático Medio (MSE)**.
  - **Error Cuadrático Medio Normalizado (NMSE)**.
  - **Error Absoluto Medio (MAE)**.
- Resultados:
  - **MLP** tuvo los valores más bajos de MSE, NMSE y MAE, destacándose como el mejor modelo.

### Conclusiones Clave

![alt text](/papers_SOA/images/0.png)

- **MLP** fue el modelo más preciso para predecir infecciones por HAV.
- Las RNA no están limitadas por suposiciones de linealidad y pueden manejar ruido, muestreo irregular y series temporales cortas.
- El estudio sugiere explorar técnicas de pronóstico más sofisticadas en investigaciones futuras.
