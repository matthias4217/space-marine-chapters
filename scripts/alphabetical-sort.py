"""
This scripts sorts a CSV on the first column alphabetically.
"""

from libsmcsv import SpaceMarineChaptersDataset

FILE = "space-marine-chapters.csv"

chapters_dataset = SpaceMarineChaptersDataset([FILE])
chapters_dataset.sort_chapters_by("Name")
chapters_dataset.write_chapters(FILE)