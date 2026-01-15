import json
import csv

def convert(input_path, output_path):
    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        return

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
