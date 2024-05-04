import csv
from enum import StrEnum

class SpaceMarineChaptersDataset:
    """
    """
    
    chapters: list[dict]

    def __init__(self, files: list[str]):
        self.chapters = []
        for file in files:
            self.chapters += self.import_chapters_from_file(file)

    def import_chapters_from_file(self, file: str):
        chapters = []
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

    def sort_chapters_by(self, attribute: str):
        self.chapters = sorted(self.chapters, key=lambda c: c[attribute])

    @classmethod
    def validate_chapter(cls, chapter: dict):
        if not chapter["Allegiance"] in [str(x) for x in Allegiance]:
            print(f"{chapter['Name']} has incorrect allegiance ({chapter['Allegiance']}).")
        if not chapter["Faction"] in [str(x) for x in Faction]:
            print(f"{chapter['Name']} has incorrect faction ({chapter['Faction']}).")
        if not chapter["Status"] in [str(x) for x in Status]:
            print(f"{chapter['Name']} has incorrect status ({chapter['Status']}).")
    
    def validate(self):
        for chapter in self.chapters:
            self.validate_chapter(chapter)
            chapters_origin = chapter["Chapter of origin"].split(" & ")
            for co in chapters_origin:
                if co != '' and not co in [c["Name"] for c in self.chapters]:
                    print(f"{chapter['Name']} has incorrect parent ({co}.")
            if chapter['Name'][:4] == 'The ':
                for chapter_bis in self.chapters:
                    if chapter_bis['Name'] == chapter['Name'][4:]:
                        print(f"Warning, both {chapter_bis['Name']} and {chapter['Name']} exist.")
        
        # TODO check *The*

    @classmethod
    def filter_chapter(cls, chapters: list[dict], criteria: dict) -> list[dict]:
        """
        Criteria : list of dict ?
        """
        pass

    @classmethod
    def get_chapter(cls, chapter_name: str) -> dict:
        """
        """
        pass


class Allegiance(StrEnum):
    LOYALIST = 'Loyalist'
    RENEGADE_CHAOS = 'Renegade/Chaos'

class Faction(StrEnum):
    EMPTY = ''
    IMPERIUM = 'Imperium'
    RENEGADE = 'Renegade'
    CHAOS_UNDIVIDED = 'Chaos Undivided'
    KHORNE = 'Khorne'
    MALICE = 'Malice'
    NURGLE = 'Nurgle'
    SLAANESH = 'Slaanesh'
    TZEENTCH = 'Tzeentch'

class Status(StrEnum):
    EMPTY = ''
    ACTIVE = 'Active'
    DESTROYED = 'Destroyed'
    MERGED = 'Merged'
    RENAMED = 'Renamed'

