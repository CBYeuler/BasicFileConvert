import csv
import json

def convert(input_path, output_path) -> None:
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


        