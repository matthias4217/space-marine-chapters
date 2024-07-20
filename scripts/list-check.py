import requests
from bs4 import BeautifulSoup

from libsmcsv import SpaceMarineChaptersDataset

# Get the list of Space Marines

page_all = {
    "url": "https://wh40k.lexicanum.com/wiki/Space_Marine_Forces_(List)",
}
page_loyalists = {
    "url": "https://wh40k.lexicanum.com/wiki/Space_Marine_Forces_(List)",
}

web_chapters = SpaceMarineChaptersDataset([])
page = requests.get(page_all["url"])
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(id="Loyalist_Chapters").parent.find_next_sibling()
for row in table.find_all('tr')[1:]:
    chapter_name = row.find('td').text.strip() # name
    web_chapters.add_chapter(chapter_name=chapter_name,allegiance="Loyalist")
#print(web_chapters.chapters)

# Get chapters from CSV
FILES_OFFICIAL = ["space-marine-chapters.csv"]
FILES_HOMEBREW = ["space-marine-chapters.csv", "space-marine-chapters-homebrew.csv"]
files = FILES_OFFICIAL
chapters_dataset = SpaceMarineChaptersDataset(files)

# Compare the two

print(f"Dataset : {len(SpaceMarineChaptersDataset.filter_chapter(chapters_dataset.chapters, {"Allegiance": "Loyalist"}))}")
print(f"Web : {len(web_chapters.chapters)}")
res_web = []
for chapter in web_chapters.chapters:
    res = chapters_dataset.remove_chapter(chapter["Name"])
    if res is None:
        res_web.append(chapter)
    web_chapters.remove_chapter(chapter["Name"])
print("Missiong on Lexicanum :")
for chapter in chapters_dataset.chapters:
    if chapter["Allegiance"] == "Loyalist":
        print(chapter["Name"])
print("Missiong in the dataset :")
for chapter in res_web:
    print(chapter["Name"])
