from random import choice
from libsmcsv import SpaceMarineChaptersDataset

FILES_OFFICIAL = ["space-marine-chapters.csv", "space-marine-chapters-homebrew-example.csv"]
FILES_HOMEBREW = ["space-marine-chapters.csv", "space-marine-chapters-homebrew.csv"]
files = FILES_OFFICIAL
chapters_dataset = SpaceMarineChaptersDataset(files)

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

#res = filter_chapters(chapters, {"Legion": True})
#print(get_random_chapter(chapters))
#print(get_random_chapter(filter_chapters(chapters, {"Allegiance": "Loyalist"})))

print(
    SpaceMarineChaptersDataset.filter_chapter(
        chapters_dataset.chapters,
        {
            "Founding": "Ultima",
            "Chapter of origin": "Iron Hands"
            }
        )
    )