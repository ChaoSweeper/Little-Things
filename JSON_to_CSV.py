# Take a JSON file and convert it to a CSV file
import json
import csv

def load_json(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data

def main():
    json_file = "data.json"
    csv_file = "data.csv"
    json_to_csv(json_file, csv_file)

def json_to_csv(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    with open(csv_file, "w") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
