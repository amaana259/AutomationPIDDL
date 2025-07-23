import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", required=True, help="1 = SDataset, 2 = MDataset")
args = parser.parse_args()

dataset_num = float(args.dataset)
excel_filename = f"clustering_results_{dataset_num}.csv"

log_files = [
    "../logs/automation/S1.log",
    "../logs/automation/S2.log",
    "../logs/automation/S3.log",
    "../logs/automation/S4.log"
]

log_files_m = [
    "../logs/automationmul/M12.log",
    "../logs/automationmul/M34.log",
    "../logs/automationmul/M56.log"
]


def extract_metrics(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    try:
        start_idx = next(i for i, line in enumerate(lines) if "start clustering" in line.lower())
    except StopIteration:
        return None

    extracted_data = []
    for line in lines[start_idx + 1:]:
        line = line.strip()
        if line:
            extracted_data.append(line)

    return extracted_data

results = []
if dataset_num == 1:
    for file in log_files:
        metrics = extract_metrics(file)
        if metrics:
            results.append({
                "file": os.path.basename(file),
                "output": "\n".join(metrics)
            })
else:
    for file in log_files_m:
        metrics = extract_metrics(file)
        if metrics:
            results.append({
                "file": os.path.basename(file),
                "output": "\n".join(metrics)
            })

df = pd.DataFrame(results)

# df.to_excel(excel_filename, index = False)

df.to_csv(excel_filename, index = False)

print("Done. Results written to .csv files")