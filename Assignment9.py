import csv
import json

csv_filename = "data.csv"
json_filename = "data.json"

# Sample CSV creation for demonstration
with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "role"])
    writer.writerow([101, "Alice", "Developer"])
    writer.writerow([102, "Bob", "Designer"])

# CSV to JSON conversion
data = []
with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

with open(json_filename, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Converted '{csv_filename}' to '{json_filename}' successfully.")
