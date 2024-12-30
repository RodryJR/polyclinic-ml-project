## **Recolección de datos:**

- **Segmentación de datos:** Los datos se dividieron en conjuntos experimentales (octubre 2002 a septiembre 2007) y de validación (octubre 2007 a septiembre 2008).
- **Evaluación de estacionariedad:** Los conjuntos de datos experimentales se evaluaron en términos de estacionariedad utilizando la prueba de Dickey-Fuller aumentada. Los tres conjuntos (comunidad, hospitalizados y PICU) resultaron ser estacionarios.

# **Desarrollo del modelo:**

- **Funciones de autocorrelación y autocorrelación parcial:** Estas funciones se calcularon y graficaron para identificar los modelos base.
- **Modelos base:** Los modelos base fueron modelos autorregresivos (AR) con órdenes determinados por la función de autocorrelación parcial.
- **Optimización del modelo:** Se construyeron múltiples modelos candidatos relativos a los modelos base minimizando el (Akaike’s Information Criterion - AIC). Se utilizó una prueba de máxima verosimilitud para determinar la inclusión o exclusión de parámetros específicos.
- **Inclusión de datos comunitarios:** Los modelos de hospitalizados y PICU incluyeron variables de incidencia comunitaria para representar la relación entre diferentes entornos.

## **Métricas y evaluación**

- **(Root Mean Squared Error - RMSE):** Se utilizó RMSE para evaluar los modelos y calcular los intervalos de confianza al 95%.
- **Selección del modelo:** Los modelos con el RMSE más bajo en las predicciones a 2 semanas fueron considerados óptimos.
- **Intervalos de confianza:** Intervalos de confianza al 95% calculados alrededor de las predicciones del modelo.
