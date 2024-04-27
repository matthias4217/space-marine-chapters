import csv
from enum import StrEnum

SOURCE_CSVS = ["space-marine-chapters.csv"] #, "space-marine-chapters-homebrew.csv"]

class Allegiance(StrEnum):
    LOYALIST = 'Loyalist'
    RENEGADE_CHAOS = 'Renegade/Chaos'

class Faction(StrEnum):
    EMPTY = ''
    IMPERIUM = 'Imperium'
    CHAOS_UNDIVIDED = 'Chaos Undivided'
    KHORNE = 'Khorne'
    MALICE = 'Malice'
    NURGLE = 'Nurgle'
    SLAANESH = 'Slaanesh'
    TZEENTCH = 'Tzeentch'
    RENEGADE = 'Renegade'

class Status(StrEnum):
    EMPTY = ''
    ACTIVE = 'Active'
    DESTROYED = 'Destroyed'
    RENAMED = 'Renamed'

def get_chapters():
    chapters = []
    for file in SOURCE_CSVS:
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                chapters.append({
                    "Name": row["Name"],
                    "Allegiance": row["Allegiance"],
                    "Faction": row["Faction"],
                    "Chapter of origin": row["Chapter of origin"],
                    "Founding": row["Founding"],
                    "Status": row["Status"],
                    "Legion": row["Legion"] == "True",
                    "Homebrew": row["Homebrew"] == "True",
                    })
    return chapters

def validate_chapter(chapter: dict):
    if not chapter["Allegiance"] in [str(x) for x in Allegiance]:
        print(f"{chapter['Name']} has incorrect allegiance ({chapter['Allegiance']}).")
    if not chapter["Faction"] in [str(x) for x in Faction]:
        print(f"{chapter['Name']} has incorrect faction ({chapter['Faction']}).")
    if not chapter["Status"] in [str(x) for x in Status]:
        print(f"{chapter['Name']} has incorrect status ({chapter['Status']}).")
    chapters_origin = chapter["Chapter of origin"].split(" & ")
    for co in chapters_origin:
        if co != '' and not co in [c["Name"] for c in chapters]:
            print(f"{chapter['Name']} has incorrect parent ({co}).")

chapters = get_chapters()
for chapter in chapters:
    validate_chapter(chapter)
