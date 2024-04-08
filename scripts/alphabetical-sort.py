"""
This scripts sorts a CSV on the first column alphabetically.
"""

import csv


def extract_name(d: dict):
    return d["Name"]

CSV_FILE = "space-marine-chapters.csv"
with open(CSV_FILE, 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    chapters = sorted(reader, key=extract_name)

with open(CSV_FILE, 'w') as g:
    writer = csv.DictWriter(g, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(chapters)