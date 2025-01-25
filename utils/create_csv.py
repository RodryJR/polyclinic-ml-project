import pandas as pd
import os

folder_path = os.path.join(os.path.dirname(__file__), '../data/Anexos_7')
output_file_incomes = os.path.join(folder_path, 'total_incomes.csv')
output_file_discharges = os.path.join(folder_path, 'total_discharges.csv')
output_file_hospitalized = os.path.join(folder_path, 'total_hospitalized.csv')

total_incomes = []
total_discharges = []
total_hospitalized = []


files = [f for f in os.listdir(folder_path) if f.endswith('.xls') or f.endswith('.xlsx')]
files.sort()

data_types = [
    ('incomes', 17, total_incomes),
    ('discharges', 22, total_discharges),
    ('hospitalized', 23, total_hospitalized)
]

for filename in files:
    date = '_'.join(filename.split('_')[:3])

    file_path = os.path.join(folder_path, filename)
    xls = pd.ExcelFile(file_path)

    desired_sheets = ['Atención Primaria'] 

    for desired_sheet in desired_sheets:
        if desired_sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=desired_sheet)
            if desired_sheet == 'Atención Primaria':
                
                provinces = df.iloc[8:24, 0].reset_index(drop=True)

                for data_type, col_index, result_list in data_types:
                    values = df.iloc[8:24, col_index].reset_index(drop=True)

                    data_dict = {'Date': date}
                    for province, value in zip(provinces, values):
                        data_dict[province] = value
                    
                    result_list.append(data_dict)


total_incomes_df = pd.DataFrame(total_incomes)
total_incomes_df.to_csv(output_file_incomes, index=False)

total_discharges_df = pd.DataFrame(total_discharges)
total_discharges_df.to_csv(output_file_discharges, index=False)

total_hospitalized_df = pd.DataFrame(total_hospitalized)
total_hospitalized_df.to_csv(output_file_hospitalized, index=False)

print(f'CSV files created:\n- {output_file_incomes}\n- {output_file_discharges}\n- {output_file_hospitalized}')