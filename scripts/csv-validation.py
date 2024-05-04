from libsmcsv import SpaceMarineChaptersDataset

FILES_OFFICIAL = ["space-marine-chapters.csv", "space-marine-chapters-homebrew-example.csv"]
FILES_HOMEBREW = ["space-marine-chapters.csv", "space-marine-chapters-homebrew.csv"]
files = FILES_OFFICIAL
chapters_dataset = SpaceMarineChaptersDataset(files)
chapters_dataset.validate()