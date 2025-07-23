#!/bin/bash

# Download data and setup working directories.
#######
#######
#######

# change _...2 to _... if you want to use the original directory names.
# directories=("../training_data2" "../embedding_data2" "../ground_data2" "../models2" "../logs2")

# for dir in "${directories[@]}"; do
#     if [ -d "$dir" ]; then
#         rm -rf "$dir"
#     fi
# done

# for dir in "${directories[@]}"; do
#     mkdir -p "$dir"
# done

# Would be done at the end with final test of downloading data.

source ~/anaconda3/etc/profile.d/conda.sh
set -e

# OPTIONAL: Remove existing environment.
# conda env remove --name airtag_env_tester || true

# Create or update the conda environment for testing.
echo "Creating airtag_env if needed..."
conda env list | grep airtag_env_tester || conda env create -f env_fulll_airtag.yaml

# Activate the environment.
echo "--- airtag_env contents ---"
conda activate airtag_env_tester 
# conda install -y pandas openpyxl
echo "--- environment activated ---"
# OPTIONAL: Check dependencies inside environment.
conda list

echo "--- running autoscript ---"

# Single-host Datasets Run.
# bash my_effect_auto.sh

# Extract data from logs and into Excel sheet.

echo " Extracting metrics from log files..."
python -u extract_metrics.py --dataset 1

if [ $? -eq 0 ]; then
    echo "Metrics extracted successfully for SDatasets."
else
    echo "Failed to extract metrics for SDatasets."
fi

# Multi-host Datasets Run.
# bash my_effect_m_auto.sh

# Extract data from logs and into Excel sheet.

echo " Extracting metrics from log files..."
python -u extract_metrics.py --dataset 2

if [ $? -eq 0 ]; then
    echo "Metrics extracted successfully for MDatasets."
else
    echo "Failed to extract metrics for MDatasets."
fi

# DEACTIVATE: Once done, deactivate the environment.
conda deactivate