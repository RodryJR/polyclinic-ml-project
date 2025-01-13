import pmdarima as pm
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
 ##	Policlinico_PI_<19años	TotalAPS_I_Total	TotalAPS_I_<19años	TotalAPS_A_Recuperados	TotalAPS_A_Remitidos	TotalAPS_A_Fallecidos	TotalAPS_A_Total	TotalAPS_PI_Total	TotalAPS_PI_<19años	PIDA_hogar	PIDA_hogar_<19años	PIDA_hospitalizaciÃ³n	PIDA_hospitalizaciÃ³n_<19años	ValidaciÃ³n_PIactual	ADAH_Ingresos	ADAH_AltasRecuperados	ADAH_Fallecidos	DH_Ingresos	DH_AltasRecuperados	DH_Fallecidos	AAH_Ingresos	AAH_AltasRecuperados	AAH_Fallecidos	ADAP_Ingresos	ADAP_AltasRecuperados	ADAP_Fallecidos	DP_Ingresos	DP_AltasRecuperados	DP_Fallecidos	AAP_Ingresos	AAP_AltasRecuperados	AAP_Fallecidos	AATotalAPS_Ingresos	AATotalAPS_AltasRecuperados	AATotalAPS_Fallecidos

def auto_arima_train(province_data_dict, field):
    predictions = {}
    models = {}
    test_sets = {}
    d_from_diff = {}
    train_sets = {}

    # Iterate over each province
    for province in province_data_dict.keys():
        # Filter data for the current province
        province_data = province_data_dict[province]

        # Extract the series to be predicted
        try:
            series = province_data[field]
        except:
            continue
        print(field)
        print(province)
        print()
    
        # Split the data into training and test sets
        train_size = int(len(series) * 0.8)
        train, test = series[:train_size], series[train_size:]
        test_sets[province] = test
        train_sets[province] = train

        # Use auto_arima to find the best parameters on the training set
        model = pm.auto_arima(train, seasonal=False, stepwise=True, suppress_warnings=True)
        models[province] = model
    
        if train.nunique() == 1: 
            print(f"The series for province '{province}' is constant.\n") 
            d_from_diff[province] = 0
            continue
    
        # Check for stationarity and apply differencing if needed
        d = 0
        result = adfuller(train)
        while result[1] > 0.05:
            train = train.diff().dropna()
            d += 1
            result = adfuller(train)
        d_from_diff[province] = d
        print(f"Best parameters for province '{province}': (d={d} from differencing, d={model.order[1]} d from AutoArima)\n")
        # Create subplots for ACF and PACF
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        plot_acf(train, ax=axes[0])
        plot_pacf(train, ax=axes[1])
        axes[0].set_title(f'ACF for {province} (MA={model.order[2]})')
        axes[1].set_title(f'PACF for {province} (AR={model.order[0]})')
        plt.tight_layout()
        plt.show()
    return predictions, models, test_sets, d_from_diff, train_sets



#     # Fit ARIMA model (example with p=1, d=1, q=1)
#     model = ARIMA(series, order=(1, 1, 1))
#     model_fit = model.fit()
#     print(model_fit.summary())
    
#     # Forecast
#     forecast = model_fit.forecast(steps=10)
#     predictions[province] = forecast

# # Print predictions
# for province, forecast in predictions.items():
#     print(f'Predictions for {province}:')
#     print(forecast)


def evaluate_models(models, test_sets, d_from_diff,train_sets, field):

    for province in models.keys():
        auto_model = models[province]
        test = test_sets[province]
    
        auto_predictions = auto_model.predict(n_periods=len(test))
        d = d_from_diff[province]
        # Fit ARIMA model on the training set
        model = ARIMA(train_sets[province], order = (auto_model.order[0], d, auto_model.order[2]))
        model_fit = model.fit()
        # Make predictions on the test set
        predictions = model_fit.forecast(steps=len(test))
        print(f' AutoArima Predictions for {province}: {field}. d = {auto_model.order[1]}') 
        print(auto_predictions)
        print()
        print(f'Arima Predictions for {province}: {field}. d = {d}') 
        print(predictions)


        # Calculate evaluation metrics
        auto_mae = mean_absolute_error(test, auto_predictions)
        auto_mse = mean_squared_error(test, auto_predictions)
        auto_rmse = np.sqrt(auto_mse)
        auto_mape = np.mean(np.abs((test - auto_predictions) / test)) * 100
        auto_nmse = auto_mse / np.var(test)
        # Calculate evaluation metrics
        mae = mean_absolute_error(test, predictions)
        mse = mean_squared_error(test, predictions)
        rmse = np.sqrt(mse)
        mape = np.mean(np.abs((test - predictions) / test)) * 100
        nmse = mse / np.var(test)

        print(f'MAE for autoArima: {auto_mae}')
        print(f'MSE for autoArima: {auto_mse}')
        print(f'RMSE for autoArima: {auto_rmse}')
        print(f'MAPE for autoArima: {auto_mape}%')
        print(f'NMSEfor autoArima: {auto_nmse}')

        print()
        print(f'MAE for ARIMA: {mae}')
        print(f'MSE for ARIMA: {mse}')
        print(f'RMSE for ARIMA: {rmse}')
        print(f'MAPE for ARIMA: {mape}%')
        print(f'NMSE for ARIMA: {nmse}')

        # Plot actual vs predicted values
        plt.figure(figsize=(10, 6))
        plt.plot(test.index, test, 'o', label='Actual') # Use 'o' for markers 
        plt.plot(test.index, auto_predictions, 'x', label='AutoArima Predicted', color='red') # Use 'x' for markers 
        plt.legend()
        plt.show()

        # Plot actual vs predicted values
        plt.figure(figsize=(10, 6))
        plt.plot(test.index, test, 'o', label='Actual') # Use 'o' for markers 
        plt.plot(test.index, predictions, 'x', label='Arima Predicted', color='red') # Use 'x' for markers 
        plt.legend()
        plt.show()
        print(model_fit.summary()) 