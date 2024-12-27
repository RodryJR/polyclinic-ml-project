### Deep Learning for Time Series Forecasting: A Survey
## Lo más relevante
# Componentes series de tiempo

Las series de tiempo suelen caracterizarse por tres elementos: 

1. Tendencia (Trend). Es el movimiento general que exhibe la serie de tiempo durante el período de observación, sin considerar la estacionalidad ni las irregularidades. En algunos textos, este componente también se conoce como variación a largo plazo. Aunque existen diferentes tipos de tendencias en las series de tiempo, las más populares son las lineales, exponenciales o parabólicas.

2. Estacionalidad (Seasonality). Este componente identifica variaciones que ocurren en intervalos regulares específicos y puede proporcionar información útil cuando los períodos de tiempo presentan patrones similares. Integra efectos razonablemente estables en el tiempo, magnitud y dirección. La estacionalidad puede estar causada por diversos factores como el clima, ciclos económicos o incluso festividades.

3. Residuos (Residuals). Una vez calculadas y eliminadas la tendencia y las oscilaciones cíclicas, quedan algunos valores residuales. Estos valores pueden ser, en ocasiones, lo suficientemente altos como para enmascarar la tendencia y la estacionalidad. En este caso, se utiliza el término "valores atípicos" (outliers) para referirse a estos residuos, y usualmente se aplican estadísticas robustas para manejarlos. Estas fluctuaciones pueden tener diversos orígenes, lo que hace que la predicción sea casi imposible. Sin embargo, si por alguna razón se puede detectar o modelar este origen, podrían considerarse como precursores de cambios en la tendencia.

# Short- and long time series forecasting
# Deep-Learning Architectures for Forecasting
1. Deep feed forward neural network
2. Recurrent neural network
3. Elman RNN
4. Deep recurrent neural network
5. Convolutional neural networks