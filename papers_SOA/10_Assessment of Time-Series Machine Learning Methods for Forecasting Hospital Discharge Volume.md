## Breve introducción

La introducción destaca el desafío que enfrentan los hospitales debido a las variaciones en los volúmenes de altas, ya que un personal adecuado es esencial para optimizar los resultados de los pacientes, pero también representa un costo fijo significativo. Aunque existen herramientas para predecir altas en unidades específicas, su implementación generalizada es limitada por la alta demanda de recursos. Esto resalta la necesidad de métodos de pronóstico escalables y prácticos para su uso operativo.

El estudio explora el uso de un enfoque de pronóstico bayesiano desarrollado por Facebook, originalmente diseñado para asignar recursos computacionales, para predecir volúmenes de altas hospitalarias. Este método aprovecha patrones repetitivos en el tiempo y requiere mínima sintonización de hiperparámetros, lo que lo hace práctico y generalizable. Además, se analiza la importancia de la cantidad de datos de entrenamiento y la frecuencia de actualización del modelo.

El objetivo principal es evaluar el desempeño de este método para facilitar su adopción en sistemas hospitalarios, comparándolo con enfoques simples, como "último valor trasladado hacia adelante" y métodos autoregresivos previamente estudiados en este contexto.

## Métodos

El análisis estadístico del estudio se centró en pronosticar el volumen diario de altas hospitalarias para el año 2010 utilizando cinco modelos: tres variaciones simples de "valores previos trasladados hacia adelante", un modelo SARIMA y el modelo Prophet de Facebook. La precisión del pronóstico se evaluó mediante el error total y el error absoluto total, con un horizonte de pronóstico de un año.

**Prophet**, un modelo bayesiano de código abierto (disponible con interfaces en Python y R), utiliza estacionalidad anual y semanal, días festivos y tendencias generales para ajustar curvas y realizar pronósticos. Los modelos simples incluyeron:
1. El volumen del día correspondiente del año anterior.
2. El volumen del día correspondiente de la semana anterior.
3. El promedio de estos dos.

En el análisis principal, Prophet se entrenó con datos de 2005 a 2009 para predecir 2010, incorporando días festivos específicos de cada hospital. SARIMA y Prophet utilizaron estos datos en sus modelos, y cada hospital se analizó de forma independiente.

La precisión se midió correlacionando los valores pronosticados y observados, reportando valores de R² y errores en términos de altas hospitalarias. También se consideró el impacto de errores negativos y acumulativos para evaluar el desempeño general de los modelos.

**Se investigaron dos aspectos clave del modelo Prophet para su implementación en pronósticos de altas hospitalarias:**

1. Cantidad de Datos de Entrenamiento:

- Se evaluó el impacto de usar entre 1 y 5 años de datos previos para entrenar el modelo. Esto permitió analizar si un hospital con pocos datos podría beneficiarse del modelo y si la precisión mejora con más datos. También se incluyeron años adicionales (2011-2014) de un hospital como objetivos de pronóstico, respetando el límite de 5 años para garantizar comparabilidad.
2. Frecuencia de Actualización del Modelo:

- Se comparó la precisión al ejecutar el modelo una vez al año frente a una actualización mensual. Esto ayudó a evaluar cómo la precisión del pronóstico se degrada con el tiempo y cuán frecuentemente debería regenerarse el modelo para mantener la precisión.

Estos experimentos, realizados únicamente con el modelo Prophet, proporcionaron información sobre la cantidad de datos necesarios y la frecuencia ideal de actualizaciones para lograr un desempeño óptimo en entornos clínicos.

## Resultados 

El modelo **Prophet** fue el más preciso para pronosticar el volumen diario de altas hospitalarias en 2010, con un error absoluto promedio de 11.5 altas por día en el hospital 1 y 11.7 en el hospital 2. Los modelos de "valores trasladados hacia adelante" tuvieron un desempeño ligeramente inferior, con errores absolutos promedio de 13.7 y 14.3 altas por día, respectivamente. Prophet superó a otros modelos en la mayoría de las métricas de desempeño, incluyendo calibración (R² de 0.843 y 0.726) y días con errores mayores a 1 desviación estándar del volumen diario.

En términos de error neto, el modelo de promedio de valores trasladados fue superior porque sus sobreestimaciones y subestimaciones se cancelaban entre sí, mientras que Prophet mostró una tendencia consistente a sobreestimar, aunque con errores absolutos menores.

El análisis secundario mostró que agregar más años de datos de entrenamiento mejoró ligeramente la precisión de Prophet, mientras que actualizar el modelo mensualmente tuvo un impacto mínimo en su desempeño. En general, Prophet demostró ser una herramienta robusta y precisa para el pronóstico de volúmenes hospitalarios.

## Discusión

El estudio encontró que el modelo **Prophet**, originalmente diseñado para modelar la carga de servidores, es una herramienta efectiva y accesible para predecir volúmenes de altas hospitalarias. Ofrece mejores resultados que los modelos autorregresivos y de "valores trasladados hacia adelante", con un entrenamiento simple que requiere pocos datos y recursos computacionales mínimos, lo que lo hace ideal para una amplia adopción.

Incluso predicciones aproximadas pueden ayudar a los administradores hospitalarios a equilibrar las necesidades de personal y pacientes, optimizando la calidad y los costos operativos. Factores como los días festivos y las altas en horarios o días atípicos subrayan la importancia de contar con pronósticos confiables para tomar decisiones de personal.

## Limitaciones

El estudio reconoce varias limitaciones en los resultados. Aunque los errores promedio son pequeños, en días específicos pueden ser significativos, superando los 25 pacientes en menos del 10% de los días. Esto sugiere la necesidad de modelos de personal flexibles incluso con predicciones precisas.

## Conclusión personal

A pesar de que **Prophet** nos ofrece una solución sencilla y práctica en este caso para poder aplicarla deberiamos buscar bases de datos de varios años para poder ajustar el modelo correctamente. En caso de tener los datos suficientes para entrenar el modelo, **Prophet** sería una solución práctica para mejorar la planificación clínica en el corto plazo mientras se desarrollan modelos más avanzados  


### Código de Prophet: https://github.com/facebook/prophet 
### Para instalar en python: *pip install prophet*

# Tabla Paper

---

| Campo                      | Detalle |
| -------------------------- | ------- |
| **Título del Paper**       | Assessment of Time-Series Machine Learning Methods for Forecasting Hospital Discharge Volume       |
| **Autores**                | Thomas H. McCoy Jr, MD; Amelia M. Pellegrini, BA; Roy H. Perlis, MD, MSc       |
| **Año de Publicación**     | 2018      |
| **Objetivo del Estudio**   | Evaluar el desempeño de un método de aprendizaje automático en series temporales para predecir volúmenes de altas hospitalarias en comparación con métodos más simples.       |
| **Métodos Empleados**      | Modelos de predicción basados en Prophet, autoregresión (SARIMA) y métodos simples de extrapolación de valores previos (última semana, último año).       |
| **Resultados Principales** | Prophet tuvo mejor calibración (R² = 0.843 y 0.726) y menor error absoluto promedio (11.5 y 11.7 altas/día) en comparación con modelos simples.       |
| **Impacto/Contribución**   | Demuestra la viabilidad de aplicar métodos de aprendizaje automático accesibles para mejorar la planificación hospitalaria y la asignación de recursos.       |
| **Contexto Geográfico**    | Dos grandes centros médicos académicos de Nueva Inglaterra, Estados Unidos.      |
| **Limitaciones**           | Variabilidad entre hospitales, grandes errores absolutos en días específicos, falta de integración de factores externos como clima o infecciones estacionales.       |
| **Palabras Clave**         | Machine learning, hospital discharge, time-series forecasting, Prophet, healthcare resource planning.       |

---




