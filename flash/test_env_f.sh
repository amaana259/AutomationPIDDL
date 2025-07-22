#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
set -e

echo "Creating flash_env if needed..."
conda env list | grep flash_env_tester || conda env create -f env_tester_f.yaml

echo "--- flash_env contents ---"
conda activate flash_env_tester
conda list
conda deactivate