import h2o
import pandas as pd
from h2o.automl import H2OAutoML
from DataReader import new_df
h2o.init()

h2o_df = h2o.H2OFrame(new_df)

time_col = 'Date'
target_col = 'Target'

response = target_col
predictors = [col for col in h2o_df.columns if col != time_col and col != target_col]

# Run H2O AutoML to create the model
aml = H2OAutoML(max_models=10, seed=1)
aml.train(y=response, x=predictors, training_frame=h2o_df)

lb = aml.leaderboard
print(lb)

# Get the best model
best_model = aml.leader

# Make predictions
predictions = best_model.predict(h2o_df)

# Convert predictions to a pandas DataFrame
predictions_df = predictions.as_data_frame()

print(predictions_df)

h2o.shutdown()