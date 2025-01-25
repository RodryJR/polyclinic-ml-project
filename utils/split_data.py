import pandas as pd
import os

total_incomes_file = os.path.join(os.getcwd(), 'data/Anexos_7/total_incomes.csv')
total_discharges_file = os.path.join(os.getcwd(), 'data/Anexos_7/total_discharges.csv')
total_hospitalized_file = os.path.join(os.getcwd(), 'data/Anexos_7/total_hospitalized.csv')

training_folder = os.path.join(os.getcwd(), 'data/Anexos_7/training')
test_folder = os.path.join(os.getcwd(), 'data/Anexos_7/test') 

os.makedirs(training_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

cutoff_date = pd.to_datetime('2023-10-10')

def process_csv(file_path, training_folder, test_folder):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y_%m_%d', errors='coerce')

    # Split the data 
    training_data = data[data['Date'] <= cutoff_date]
    test_data = data[data['Date'] > cutoff_date]

    # Save the training and test data 
    base_name = os.path.basename(file_path).replace('.csv', '')
    training_data.to_csv(os.path.join(training_folder, f'{base_name}_training_data.csv'), index=False)
    test_data.to_csv(os.path.join(test_folder, f'{base_name}_test_data.csv'), index=False)

# Process each CSV file
process_csv(total_incomes_file, training_folder, test_folder)
process_csv(total_discharges_file, training_folder, test_folder)
process_csv(total_hospitalized_file, training_folder, test_folder)

print('Training and test data have been saved as separate files in the training and test folders.')
