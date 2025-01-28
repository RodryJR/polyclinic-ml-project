import os
import pandas as pd
import sys
from datetime import datetime

def save_predictions(predictions, model_name, extra_info=""):
    model_name = os.makedirs(f'../data/results/{model_name}')

    if not os.path.exists(model_name):
        os.makedirs(model_name)

    # todo manage different models 
    df = pd.DataFrame(predictions, columns=['Date', 'Prediction'])

    file_name = f"predictions_{model_name}_{extra_info}.csv"
    file_path = os.path.join(model_name, file_name)

    df.to_csv(file_path, index=False)
    print(f"Predictions saved in: {file_path}")
