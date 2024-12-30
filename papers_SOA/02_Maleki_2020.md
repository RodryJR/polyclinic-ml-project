# Modelo Autorregresivo Basado en Distribuciones TP-SMN Asimétricas/Colas Pesadas (TP-SMN-AR)

- Este estudio utiliza un tipo específico de modelo autorregresivo conocido como **TP-SMN-AR**, basado en **distribuciones de mezcla de escala normal de dos piezas (TP-SMN)**.
- Este modelo permite distribuciones de error asimétricas y de colas pesadas, lo que lo hace más flexible que los modelos estándar que asumen errores gaussianos simétricos.

## Datos y Transformaciones

- Los datos consisten en reportes diarios de casos confirmados y recuperados de COVID-19.
- Las gráficas de series temporales muestran tendencias crecientes, lo que indica que no son estacionarias.
- Para abordar esto, los datos fueron transformados para lograr estacionariedad antes de aplicar el modelo TP-SMN-AR.

## Selección del Modelo

- Tras las transformaciones, se ajustaron modelos **TP–SMN–AR** a las series estacionarias de casos confirmados y recuperados.

## Evaluación del Modelo y Predicción

- Para evaluar la precisión de los modelos, se eliminaron los últimos 10 días de datos (del 21 al 30 de abril de 2020) y se realizaron predicciones.
- Métrica utilizada: **Error Relativo Medio Porcentual (MAPE)**.
  - MAPE para casos confirmados: **0.22%**.
  - MAPE para casos recuperados: **1.6%**.
- Se presentaron las predicciones con intervalos de confianza al 98% (Tabla 1).

### Distribución de Errores

- Los residuos del modelo seguían distribuciones **TP-SMN**, más adecuadas que las gaussianas para estos datos.
- Estas distribuciones permiten capturar errores con asimetría y colas pesadas.

### Criterios de Selección del Modelo

- Los **modelos TP-SMN-AR** se seleccionaron basándose en:
  - **Criterio de Información de Akaike (AIC)**.
  - **Criterio de Información Bayesiano (BIC)**.
  - Pruebas de Box-Pierce y Ljung-Box en los residuos.

### Comparación con Otros Modelos

- Los modelos estándar de series temporales asumen residuos simétricos (gaussianos), lo que limita su aplicabilidad.
- Los modelos **TP-SMN-AR** incluyen casos especiales o límites de los modelos autorregresivos más estándar.

## Notas Adicionales

Los autores sugieren que las distribuciones TP-SMN podrían usarse en procesos ciclostacionarios o casi ciclostacionarios en trabajos futuros.
