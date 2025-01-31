#!/bin/bash

mkdir -p ./data/results

error_log="error.log"

if ! python utils/rename_xls.py 2> "$error_log"; then
    echo "Error: Failed to execute rename_xls.py"
    echo "Detailed error:"
    cat "$error_log"
    exit 1
fi

if ! python utils/create_csv.py 2> "$error_log"; then
    echo "Error: Failed to execute create_csv.py"
    echo "Detailed error:"
    cat "$error_log"
    exit 1
fi

if ! python -m utils.split_and_augment_data 2> "$error_log"; then
    echo "Error: Failed to execute split_and_augment_data"
    echo "Detailed error:"
    cat "$error_log"
    exit 1
fi

echo "Scripts executed successfully."
