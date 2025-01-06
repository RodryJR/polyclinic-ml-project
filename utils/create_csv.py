import pandas as pd
import os

folder_path = os.path.join(os.path.dirname(__file__), '../data/Anexos_7')
output_file = os.path.join(folder_path, 'results.csv')

results = []

files = [f for f in os.listdir(folder_path) if f.endswith('.xls') or f.endswith('.xlsx')]
files.sort()

for filename in files:
    date = '_'.join(filename.split('_')[:3])

    file_path = os.path.join(folder_path, filename)
    xls = pd.ExcelFile(file_path)

    desired_sheet = 'Atención Primaria'

    if desired_sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=desired_sheet)

            #todo: automate date selection a column selection
        # change the second number to select the column
        provinces = df.iloc[8:24, 0].reset_index(drop=True)
        incomes = df.iloc[8:24, 17].reset_index(drop=True)

        income_dict = {'Date': date}
        for province, income in zip(provinces, incomes):
            income_dict[province] = income

        results.append(income_dict)

results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)

print(f'CSV file created: {output_file}')
