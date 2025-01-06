import pandas as pd
import os

# Load the original CSV file
csv_file = os.path.join(os.getcwd(), 'data/Anexos_7/results.csv')
data = pd.read_csv(csv_file)

training_folder = os.path.join(os.path.join(os.getcwd(), 'data/Anexos_7/training'))
test_folder = os.path.join(os.path.join(os.getcwd(), 'data/Anexos_7/test')) 

os.makedirs(training_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%Y_%m_%d')

# Define the cutoff date for training data
cutoff_date = pd.to_datetime('2023-10-10')

# Split the data into training and test sets
training_data = data[data['Date'] <= cutoff_date]
test_data = data[data['Date'] > cutoff_date]

# Save the training and test data to separate CSV files
training_data.to_csv(os.path.join(training_folder, 'training_data.csv'), index=False)
test_data.to_csv(os.path.join(test_folder, 'test_data.csv'), index=False)

print('Training and test data have been saved as training_data.csv and test_data.csv.')
