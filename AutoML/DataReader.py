import os
import pandas as pd
from typing import Dict

def extract_substring(s):
    # Find the position of the last two underscores
    last_underscore = s.rfind('_')
    second_last_underscore = s.rfind('_', 0, last_underscore)
    
    # Extract the substring between the last two underscores
    if second_last_underscore != -1:
        return s[second_last_underscore + 1:last_underscore]
    return None  # In case there are less than two underscores

def extract_date(string:str)->str:
    date= extract_substring(string)

    return date.replace('-', '/')

def get_csv_dataframes_with_substring(folder_path, substring)->Dict[str,pd.DataFrame]:
    """
    Reads all CSV files in the specified folder that contain the given substring in their filenames
    and returns a dictionary of pandas DataFrames.

    :param folder_path: Path to the folder containing CSV files.
    :param substring: Substring to search for in filenames.
    :return: Dictionary with filenames as keys and corresponding DataFrames as values.
    """
    dataframes = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv") and substring in file_name:
            file_path = os.path.join(folder_path, file_name)
            try:
                df: pd.DataFrame= pd.read_csv(file_path)
                dataframes[file_name] = df
            except Exception as e:
                print(f"Failed to read {file_name}: {e}")
    return dataframes

# Example usage:
folder = "AutoML/Data"  # Replace with the path to your folder
substring = "Atención Primaria"  # Replace with your desired substring
csv_dataframes = get_csv_dataframes_with_substring(folder, substring)

provinces_data:Dict[str,list[list]]=dict()
target_variable=[]
dates=[]
# Operation to make per dataframe

for filename, dataframe in csv_dataframes.items():
    # Working with Pinar del Rio
    province_name:str= dataframe.iloc[8,0]
    target_to_add=dataframe.iloc[8,3]
    column_to_drop = dataframe.columns[3] #tumbando variable objetivo
    column_to_drop2=dataframe.columns[0] #tumbando nombre de la provincia 
    new_row = dataframe.loc[8].drop(column_to_drop).drop(column_to_drop2)
    new_row.dropna()
    
    
    #Extracting date
    dates.append(extract_date(filename))
    #taking target and other variables values

    target_variable.append(target_to_add)
    
    provinces_data.setdefault(province_name,list())
    provinces_data[province_name].append(new_row)
    
    # print(f"DataFrame from {filename}:")
    # print(dataframe.iloc[8,0])  # Display the first few rows of the DataFrame

new_df=pd.DataFrame(provinces_data[list(provinces_data.keys())[0]])
new_df['Target']= target_variable
new_df['Date']=dates
print(new_df.head())    


