import os
import pandas as pd

log_files = [
    "../logs/automation/S1.log",
    "../logs/automation/S2.log",
    "../logs/automation/S3.log",
    "../logs/automation/S4.log"
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
for file in log_files:
    metrics = extract_metrics(file)
    if metrics:
        results.append({
            "file": os.path.basename(file),
            "output": "\n".join(metrics)
        })

df = pd.DataFrame(results)

# df.to_excel("clustering_results.xlsx", index = False)

df.to_csv("clustering_results.csv", index = False)

print("Done. Results written to clustering_results.csv")