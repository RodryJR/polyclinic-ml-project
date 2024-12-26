# Introducción

Este artículo revisa los avances recientes en métodos de aprendizaje automático (ML) para la predicción de series temporales económicas y financieras. El ML se ha vuelto crucial para la estimación, selección de modelos y predicciones en economía y finanzas, especialmente con la abundancia de datos en la era del Big Data. El artículo se centra en el aprendizaje supervisado, que busca mapear variables de entrada a salida basándose en datos etiquetados, dejando de lado otros enfoques como el aprendizaje no supervisado y por refuerzo.

Se analizan dos grandes grupos de métodos supervisados:

Modelos lineales: Incluyen técnicas de regularización como Ridge Regression y LASSO, destacando su evolución teórica y aplicaciones.
Modelos no lineales: Consideran redes neuronales (shallow y deep), redes recurrentes, y modelos basados en árboles como Random Forests y Boosted Trees.
También se exploran enfoques híbridos que combinan elementos lineales y no lineales, así como métodos basados en conjuntos, como Bagging y Complete Subset Regression. Finalmente, se introducen pruebas de capacidad predictiva para evaluar la efectividad de estos modelos antes de mostrar una aplicación empírica.

# Resumen del artículo

Además de esta breve introducción, el artículo está organizado de la siguiente manera:

- Los modelos de regresión lineal penalizada.
- Los modelos no lineales de aprendizaje automático.
- Los métodos de conjuntos y métodos híbridos.
- Las pruebas de capacidad predictiva superior.
- Una aplicación empírica.

# Modelos Lineales Penalizados

Los modelos lineales penalizados se utilizan para predecir valores en series temporales cuando el número de predictores $(n)$ es grande o los datos presentan alta correlación entre variables. En estos casos, los métodos tradicionales como los mínimos cuadrados ordinarios (OLS) pueden fallar, ya que el modelo puede sobreajustarse. Para mitigar este problema, se introducen penalizaciones en la función de pérdida, balanceando el ajuste del modelo y la regularización.

# Principales Métodos de Penalización:
1. **Regresión Ridge**: Penaliza con la norma $ℓ_2(∥β∥^2_2)$ para reducir la varianza del estimador, aunque introduce un pequeño sesgo. Es útil para estabilizar modelos, pero no realiza selección de variables.
2. **LASSO**: Penaliza con la norma $ℓ_1(∥β∥_1​)$, lo que produce soluciones dispersas y selecciona automáticamente un subconjunto de predictores relevantes. Es ampliamente usado en entornos con muchos predictores $(n≫T)$.
3. **LASSO Adaptativo (adaLASSO)**: Mejora el LASSO introduciendo pesos derivados de una regresión inicial. Tiene propiedades asintóticas mejoradas y puede manejar más variables que observaciones.
4. **Elastic Net**: Combina las penalizaciones $ℓ_1$  y $ℓ_2$ , seleccionando variables (como LASSO) y estabilizando la solución (como Ridge). Es especialmente útil cuando los predictores están altamente correlacionados.
5. **Penalización Cóncava Plegada**: Penaliza menos a los coeficientes alejados de cero, mejorando la selección de modelos y la predicción en algunos casos. Ejemplo: SCAD (Smoothly Clipped Absolute Deviation).
6. **Penalizaciones Alternativas**:
    - *Group LASSO*: Penaliza grupos de predictores en lugar de variables individuales.
    - *Sparse Group LASSO*: Combina penalización grupal y dispersa $(ℓ_1)$.
    - Métodos adaptativos que incorporan retardos mejoran el rendimiento en aplicaciones específicas, como inflación y primas de riesgo.

**Interpretación Bayesiana**: Algunos métodos tienen una interpretación bayesiana, como Ridge (priors gaussianos) y LASSO (priors Laplacianos), conectando estas técnicas con enfoques de reducción bayesianos.
En resumen, los modelos lineales penalizados ofrecen soluciones eficientes para problemas de alta dimensionalidad y datos correlacionados, permitiendo un equilibrio entre ajuste y simplicidad del modelo.

# Propiedades Teóricas de los Modelos Penalizados

Los modelos de regresión penalizada tienen fuertes fundamentos teóricos, destacando su capacidad para manejar problemas de alta dimensionalidad y dependencias temporales. Las principales propiedades teóricas incluyen:

1. **Consistencia en la Selección de Modelos**: El método identifica correctamente los predictores relevantes $(S_0)$ a medida que el tamaño de la muestra aumenta.
2. **Propiedad de Oráculo**: El estimador penalizado tiene el mismo comportamiento asintótico que un estimador no penalizado considerando solo los predictores correctos.
3. **Cotas de Oráculo**: Proveen límites de error de estimación para muestras finitas, útiles para evaluar el desempeño del modelo bajo condiciones estrictas.

## Principales Resultados:
- **LASSO y AdaLASSO:** Consistencia en selección de modelos y propiedad de oráculo, aplicables a series temporales estacionarias, integradas y con errores dependientes.
- **SCAD y Penalizaciones Cóncavas:** Mejoran el rendimiento en alta dimensión al penalizar menos los coeficientes alejados de cero.
- **Sparse Group LASSO:** Diseñado para datos de series temporales con alta dimensionalidad y diferentes frecuencias de muestreo.

## Extensiones:
Métodos específicos para series no estacionarias y modelos multivariados, como VAR de alta dimensión, han demostrado resultados sólidos en selección de modelos y predicción.

Los métodos de regresión penalizada son herramientas versátiles y efectivas para modelar y predecir en series temporales de alta dimensión, con aplicaciones que abarcan desde entornos estacionarios hasta modelos multivariados complejos.

# Inferencia en Modelos Penalizados

La inferencia en estimadores penalizados es un área activa, especialmente tras la selección de modelos. Se han desarrollado técnicas para abordar los desafíos asociados con los sesgos y la normalidad asintótica:

1. **LASSO Desesparcificado:** Agrega un término al estimador LASSO para eliminar sesgos y recuperar normalidad asintótica.
2. **Método de Doble Selección:** Identifica predictores relevantes y estima parámetros clave en modelos reducidos, garantizando intervalos de confianza válidos.
3. **Inferencia Posterior a la Selección:** Ofrece intervalos de confianza condicionales al modelo seleccionado, válidos para cualquier valor del parámetro de penalización.

## Aplicaciones en Series Temporales:
Métodos como los de Babii et al. (2020a) y Adámek et al. (2020) extienden estas técnicas a series temporales con errores heterocedásticos y dependencias complejas, permitiendo que el número de regresores supere el tamaño de la muestra.

Las nuevas técnicas permiten realizar inferencias robustas en entornos de alta dimensionalidad y dependencias temporales, mejorando la validez de los análisis en modelos penalizados.

# Modelos No Lineales

Cuando la suposición de linealidad es demasiado restrictiva, se utilizan modelos no lineales que permiten mayor flexibilidad. Sin embargo, optimizar sobre espacios funcionales infinitos $(G)$ es inviable, por lo que se usan espacios de aproximación finitos $(G_D)$, conocidos como sieves, que convergen a $G$ en alguna norma.

## Método de Sieves:
- **Sieves Lineales**: Las funciones base $(g_j)$ son conocidas (e.g., polinomios), y se aplican métodos como OLS o estimación penalizada.
- **Sieves No Lineales**: Las funciones base están parametrizadas y requieren métodos de mínimos cuadrados no lineales.

#### Ejemplo: Los polinomios de grado $D−1$ forman un conjunto finito que puede aproximar funciones continuas. Por ejemplo, una base polinómica incluye términos como $1,X_t​ ,X^2_t ,…,X^J_t$ .

El artículo se centra en sieves no lineales ampliamente utilizados, como redes neuronales y árboles de regresión, que son herramientas efectivas para aproximar funciones complejas en modelos no lineales.

# Modelos de Redes Neuronales

1. **Redes Neuronales Superficiales (Shallow Neural Networks - NN)**
    - Utilizan combinaciones de neuronas ocultas para aproximar funciones no lineales.
    - Estructura típica: redes feedforward con funciones de activación como logística, tangente hiperbólica o ReLU. 
    - Tienen la capacidad de aproximar cualquier función continua con suficientes neuronas.
    - Técnicas como dropout ayudan a prevenir el sobreajuste eliminando aleatoriamente neuronas durante el entrenamiento.
2. **Redes Neuronales Profundas (Deep Neural Networks - DNN)**
    - Extienden las redes superficiales añadiendo múltiples capas ocultas, permitiendo modelar funciones más complejas.
    - Las redes profundas son más eficientes, ya que requieren menos parámetros para aproximar funciones complejas.
    - El entrenamiento utiliza descenso de gradiente estocástico y regularización (dropout) para controlar la complejidad del modelo.
3. **Redes Neuronales Recurrentes (Recurrent Neural Networks - RNN)**
    - Diseñadas para secuencias como series temporales, incorporan un estado oculto $(H_t)$ que almacena información previa.
    - Solucionan problemas de dependencia a largo plazo mediante variantes como LSTM (Long Short-Term Memory).
    - LSTM utiliza "puertas" (de entrada, olvido y salida) para filtrar información relevante, mejorando el manejo de datos secuenciales dependientes.

# Modelos de Árboles de Regresión

## Árboles de Regresión
Los árboles de regresión son modelos no paramétricos que aproximan funciones no lineales mediante divisiones recursivas del espacio de covariables. Cada nodo del árbol representa una condición basada en una variable y un umbral (por ejemplo, altura > 1.85 m). Las predicciones se obtienen calculando el promedio de las observaciones en cada nodo terminal (hoja).
Matemáticamente, un árbol de regresión aproxima $f_h(X_t)$ como una combinación lineal de funciones indicadoras que identifican a qué región pertenece cada observación. El crecimiento del árbol requiere seleccionar variables y puntos de corte óptimos en cada nodo.

## Bosques Aleatorios (Random Forests)
Los bosques aleatorios son conjuntos de múltiples árboles de regresión generados a partir de muestras bootstrap del conjunto de datos original. Cada árbol se construye utilizando un subconjunto aleatorio de variables explicativas. La predicción final se calcula como el promedio de las predicciones individuales de todos los árboles.
El método es robusto y mejora la precisión al reducir el riesgo de sobreajuste. Breiman (2001) introdujo este enfoque, y estudios recientes han demostrado su consistencia y normalidad asintótica en datos independientes y distribuidos idénticamente (IID).

## Árboles Potenciados (Boosting Trees)
El boosting es un método iterativo que ajusta los residuos de un modelo inicial mediante pequeños árboles en cada iteración. El modelo final es una suma ponderada de estos árboles ajustados. El parámetro de aprendizaje $(v)$ controla la tasa de convergencia y ayuda a evitar el sobreajuste, siendo recomendado un valor entre 0.1 y 0.2.
El enfoque de Gradient Boosting (Friedman, 2001) utiliza técnicas de descenso de gradiente en el espacio funcional para minimizar la función de pérdida. Este método es particularmente eficaz para datos independientes.

# Inferencia en Modelos No Lineales
La inferencia en métodos de aprendizaje no lineal es compleja. Algunas aproximaciones clave incluyen:
- **Modelos paramétricos**: Tratar especificaciones no lineales como modelos paramétricos, aunque esto limita la generalidad.
- **Método de sieves**: Usar aproximaciones semiparamétricas con consistencia y normalidad asintótica bajo condiciones específicas (Chen y Shen, 1998).
En el caso de los bosques aleatorios, estudios recientes han extendido resultados inferenciales a datos dependientes, como en procesos autorregresivos no lineales (Davis y Nielsen, 2020).

# Otros Métodos

## Bagging (Bootstrap Aggregating)
Bagging es un método propuesto por Breiman (1996) para reducir la varianza de predictores inestables. Es útil cuando el número de predictores es moderadamente grande en comparación con el tamaño de la muestra.
**Aplicación en series temporales:** En contextos de series temporales, se ajusta para considerar la dependencia temporal en las muestras bootstrap.
**Modificaciones:** Si el número de predictores excede el tamaño de la muestra $(n>T)$, se usan estrategias como las propuestas por Garcia et al. (2017) y Medeiros et al. (2021), que seleccionan subconjuntos relevantes de predictores antes de aplicar bagging.

## Regresión de Subconjuntos Completos (CSR)
CSR combina pronósticos promediando todas las regresiones posibles con un número fijo de predictores $(k)$.
**Desafíos:** El número de modelos aumenta rápidamente con $n$ y $k$, volviendo el cálculo impracticable.
**Solución**: Se selecciona un subconjunto reducido de variables relevantes mediante una estrategia basada en estadísticas-$t$, similar al Sure Independence Screening de Fan y Lv (2008). Este enfoque reduce la complejidad computacional mientras mantiene predictores relevantes.

## Métodos Híbridos
Los métodos híbridos combinan características de diferentes modelos para aprovechar sus fortalezas.
**LASSO y Redes Neuronales**: Medeiros y Mendes (2013) combinaron estimación basada en LASSO con redes neuronales (NN). Los términos no lineales son generados aleatoriamente, mientras que los parámetros lineales se estiman con LASSO.
**Redes Neuronales con Componentes Lineales**: Trapletti et al. (2000) propusieron agregar un término lineal a redes neuronales superficiales para capturar solo dependencias no lineales, haciendo el modelo más interpretable.
**Combinación de Random Forests y adaLASSO**: Medeiros et al. (2021) propusieron dos enfoques:
    1. *RF/OLS*: Variables seleccionadas por Random Forest se usan en una regresión OLS.
    2. *adaLASSO/RF*: Variables seleccionadas por adaLASSO se usan en un modelo Random Forest.
**"LASSO Parcialmente Igualitario"**: Diebold y Shin (2019) propusieron un método para combinar pronósticos. Asigna pesos cero a algunos predictores y ajusta otros hacia valores iguales, optimizando la combinación de predicciones

# Comparación de Pronósticos

Con el rápido crecimiento en la cantidad de modelos de predicción impulsados por el aprendizaje automático (ML), es esencial utilizar herramientas estadísticas para comparar diferentes enfoques. La literatura sobre pronósticos ofrece varios métodos para esta tarea, incluidos los siguientes:

# Pruebas Clave:

1. **Prueba de Diebold y Mariano (1995)**:

Evalúa si dos métodos tienen la misma pérdida esperada incondicional bajo la hipótesis nula.
Utiliza un simple $t$-test y tiene una corrección para muestras pequeñas (Harvey et al., 1997).
**Limitación**: Diverge bajo la nula cuando los modelos son anidados, aunque es válido si los pronósticos se derivan en un esquema de ventana móvil (rolling window).

2. **Prueba de Habilidad Predictiva Superior Incondicional (USPA)**:

Propuesta por White (2000) para comparar múltiples modelos contra un método de referencia.
Hansen (2005) señaló que puede ser conservadora si algunos métodos comparados son significativamente inferiores.

3. **Conjunto de Confianza de Modelos (MCS)**:

Introducido por Hansen et al. (2011).
Identifica un conjunto de modelos que contiene el mejor modelo con un nivel de confianza dado.
**Considera las limitaciones de los datos**: conjuntos no informativos producen un MCS grande, mientras que datos informativos generan un MCS reducido.

4. **Prueba de Igualdad de Habilidad Predictiva Condicional (CEPA)**:

Propuesta por Giacomini y White (2006), evalúa si un modelo es superior en ciertas condiciones específicas.
Recientemente, Li et al. (2020) extendieron este marco para realizar pruebas condicionales más generales.

# Conclusiones 

Este artículo presenta una revisión de los desarrollos recientes en aprendizaje automático (ML) y estadísticas de alta dimensionalidad aplicados al modelado y pronóstico de series temporales. Se cubren modelos lineales, no lineales, modelos de ensamble e híbridos, así como pruebas de habilidad predictiva superior.

## Resumen de Resultados:

1. **Modelos Lineales**:
- Métodos penalizados como Ridge, LASSO y sus generalizaciones tienen avances teóricos significativos en datos dependientes.
- Los métodos de ensamble como Bagging y CSR tienen resultados teóricos limitados, ya que la mayoría se basa en datos independientes (IID).

2. **Modelos No Lineales**:
- Métodos basados en árboles como Random Forests (RF) y Boosting tienen desarrollos teóricos para datos IID y conjuntos de regresores de baja dimensionalidad.
- Redes Neuronales (NN): Hay resultados teóricos para datos dependientes en dimensiones bajas (Chen et al., 2007), pero su comportamiento en alta dimensionalidad aún está en estudio, especialmente para redes profundas.

3. **Evidencia Empírica**:
- Los modelos no lineales de ML combinados con grandes conjuntos de datos son útiles y prometedores para el pronóstico económico.

### Conclusión Final:
Aunque se han dejado fuera métodos como Support Vector Regressions, autoencoders y modelos de factores no lineales, el contenido presentado proporciona un marco valioso para quienes buscan aplicar técnicas de ML al pronóstico económico y financiero. Se espera que los avances en estas áreas impulsen el uso de ML en contextos económicos complejos y desafiantes.


# Tabla paper
---

| Campo                      | Detalle |
| -------------------------- | ------- |
| **Título del Paper**       | Machine learning advances for time series forecasting       |
| **Autores**                | Ricardo P. Masini,  Marcelo C. Medeiros, Eduardo F. Mendes       |
| **Año de Publicación**     | 2021       |
| **Objetivo del Estudio**   | Revisar los desarrollos recientes en modelos de ML y estadísticas de alta dimensionalidad aplicados al pronóstico de series temporales.      |
| **Métodos Empleados**      | Modelos lineales penalizados (Ridge, LASSO y generalizaciones), métodos no lineales (Redes Neuronales y Random Forests), métodos híbridos y de ensamble (Bagging, CSR), e inferencia estadística.       |
| **Resultados Principales** |  Métodos lineales penalizados como LASSO muestran fuertes mejoras en pronósticos económicos y financieros. Modelos no lineales, como Random Forests y Redes Neuronales, son útiles cuando se usan grandes conjuntos de datos. Métodos híbridos como la combinación de Random Forests con adaLASSO son prometedores.      |
| **Impacto/Contribución**   | Provee un marco integral para aplicar técnicas de ML al pronóstico económico y financiero, destacando áreas con resultados teóricos limitados y futuras direcciones de investigación.       |
| **Contexto Geográfico**    | Aplicaciones ilustrativas para EE.UU. (inflación, volatilidad de acciones), Brasil (varianza realizada de BOVESPA) y mercados internacionales (índices bursátiles principales).      |
| **Limitaciones**           | Métodos como Bagging y Boosting tienen desarrollos teóricos limitados para datos dependientes. Resultados teóricos de ML no lineal en alta dimensionalidad y dependencias son aún incipientes. Algunos métodos importantes (e.g., Support Vector Regressions, autoencoders) no se incluyeron en el estudio.       |
| **Palabras Clave**         | Machine Learning, Penalized Regressions, Nonlinear Models, Random Forests, Neural Networks, Time-Series Forecasting, High-Dimensional Models.       |

---