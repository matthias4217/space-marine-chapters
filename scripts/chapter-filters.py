from random import choice
import csv

SOURCE_CSVS = ["space-marine-chapters.csv", "space-marine-chapters-homebrew.csv"]

def get_chapters():
    chapters = []
    for file in SOURCE_CSVS:
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                chapters.append({
                    "Name": row["Name"],
                    "Allegiance": row["Allegiance"],
                    "Chapter of origin": row["Chapter of origin"],
                    "Founding": row["Founding"],
                    "Legion": row["Legion"] == "True",
                    "Homebrew": row["Homebrew"] == "True",
                    })
    return chapters

def filter_chapters(chapters: list[dict], filter: dict):
    """
    filter is a dict of keys (attributes of chapters) and values
    """
    res = []
    for chapter in chapters:
        criteria_met = True
        for key in filter.keys():
            if chapter[key] != filter[key]:
                criteria_met = False
                break
        if criteria_met:
            res.append(chapter)
    return res

def get_random_chapter(chapters: list[dict]):
    return choice(chapters)

chapters = get_chapters()
res = filter_chapters(chapters, {"Legion": True})
#print(get_random_chapter(chapters))
print(get_random_chapter(filter_chapters(chapters, {"Allegiance": "Loyalist"})))
