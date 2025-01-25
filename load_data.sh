#!/bin/bash

# Modify this line if you are using a virtual environment
# source /path/to/your/venv/bin/activate

python utils/rename_xls.py
python utils/create_csv.py
python utils/split_data.py

echo "Scripts executed successfully."
