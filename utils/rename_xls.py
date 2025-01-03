import os
import re


RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m" 

folder_path = os.path.join(os.path.dirname(__file__), '../data')

os.chdir(folder_path)

files_to_delete = [
    "Anexos Circular 7_05-10-2023 (1).xls",
    "Anexos Circular 7_06-10-2023 (1).xls",
    "Anexos Circular 7_12-09-2023 (1).xls",
    "Anexos Circular 7_15-08-2023 (1).xls"
]

for filename in files_to_delete:
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{RED}Deleted: {filename}')

# regular exp
pattern = re.compile(r'Anexos[ _]Circular[ _](\d+)[ _]?(\d{1,2})[-_](\d{1,2})[-_](\d{4})')

for filename in os.listdir(folder_path):
    match = pattern.search(filename)

    if match:
        circular_number = match.group(1)
        day = match.group(2)
        month = match.group(3)
        year = match.group(4)

        # format
        new_filename = f"{year}_{month.zfill(2)}_{day.zfill(2)}_Anexo_Circular_{circular_number}.xls"
        os.rename(filename, new_filename)

        print(f'Renamed: {RED}{filename}{RESET} to {GREEN}{new_filename}{RESET}')
