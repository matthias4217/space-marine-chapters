from bs4 import BeautifulSoup
import csv

PAGE_FILES = ["page1.html", "page2.html"]
FANDOM_SM_FILE = "fandom-list-space-marine-chapters.html"
FANDOM_CSM_FILE = "fandom-list-chaos-space-marine-chapters.html"
OUTPUT_FILE = "space-marine-chapters.csv"

"""
⚠ This code is quick and dirty. Any improvement is welcome. ⚠

The goal of this script was first to get a random existing Space Marine chapter, whether they were
loyalist or traitor.
It was then expanded to generate a CSV database of these chapters, to be used by other software.

Data from :
    * https://wh40k.lexicanum.com/wiki/Pictorial_List_of_Space_Marine_Chapters_A-L
    * https://wh40k.lexicanum.com/wiki/Pictorial_List_of_Space_Marine_Chapters_M-Z
    * https://warhammer40k.fandom.com/wiki/List_of_Space_Marine_Chapters
    * https://warhammer40k.fandom.com/wiki/List_of_Chaos_Space_Marine_Warbands
    * https://wh40khomebrew.fandom.com/wiki/Warhammer_40,000_Homebrew_Wiki
Chapter file :
    * Chapter name
    * Chapter allegiance
    * Chapter of origin
    * Founding
    * Is it one of the legions ?
    * Is it homebrew ?

For Homebrew chapters, we could add the source and the creator.

* The duplicates :
  * [x] Cleaved, The
  * [x] Flawless Host, The
  * [x] Purge, The
  * [x] Pyre, The
  * [x] Reborn, The
  * [x] Sanctified, The
  * [x] Scourged, The
"""

def get_chapters_from_lexicanum():
    chapters = []
    for page_file in PAGE_FILES:
        with open(page_file, "r") as f:
            page_content = f.read()
        soup = BeautifulSoup(page_content, 'html.parser')
        letter = soup.find('span', 'mw-headline').parent
        while letter.name == "h2":
            header = True
            for chapter_in_letter in letter.next_sibling.next_sibling.find_all('tr'):
                if header:
                    header = False
                    continue
                chapter_name = chapter_in_letter.contents[3].contents[0].get_text()
                chapters.append({
                    "Name": chapter_name,
                    "Allegiance": "",
                    "Faction": "",
                    "Chapter of origin": "",
                    "Founding": "",
                    "Legion": False,
                    "Homebrew": False,
                    })
            letter = letter.next_sibling.next_sibling.next_sibling.next_sibling
    return chapters

def add_fandom_sm(chapters):
    with open(FANDOM_SM_FILE, "r") as f:
        page_content = f.read()
    soup = BeautifulSoup(page_content, 'html.parser')
    letter = soup.find('span', 'mw-headline').parent
    while letter is not None:
        header = True
        for chapter_in_letter in letter.next_sibling.next_sibling.find_all('tr'):
            if header:
                header = False
                continue
            chapter_name = chapter_in_letter.contents[1].contents[0].get_text()
            chapter_of_origin = chapter_in_letter.contents[3].contents[0].get_text().strip()
            chapter_founding = chapter_in_letter.contents[5].contents[0].get_text().strip()
            is_chapter_found = False
            for chapter in chapters:
                if chapter["Name"] == chapter_name:
                    is_chapter_found = True
                    chapter["Allegiance"] = "Loyalist"
                    chapter["Chapter of origin"] = chapter_of_origin
                    chapter["Founding"] = chapter_founding
            if not is_chapter_found:
                chapters.append({
                    "Name": chapter_name,
                    "Allegiance": "Loyalist",
                    "Faction": "Imperium",
                    "Chapter of origin": chapter_of_origin,
                    "Founding": chapter_founding,
                    "Legion": False,
                    "Homebrew": False,
                    })
        letter = letter.next_sibling
        while letter is not None and letter.name != "h3":
            letter = letter.next_sibling
    return chapters

def add_fandom_csm(chapters):
    with open(FANDOM_CSM_FILE, "r") as f:
        page_content = f.read()
    soup = BeautifulSoup(page_content, 'html.parser')
    letter = soup.find('span', {"id": "Renegade_Space_Marine_Chapters_&_Chaos_Space_Marine_Warbands"}).parent.next_sibling.next_sibling
    while letter is not None:
        header = True
        for chapter_in_letter in letter.next_sibling.next_sibling.find_all('tr'):
            if header:
                header = False
                continue
            chapter_name = chapter_in_letter.contents[1].contents[0].get_text()
            chapter_of_origin = chapter_in_letter.contents[3].contents[0].get_text().strip()
            chapter_founding = chapter_in_letter.contents[5].contents[0].get_text().strip()
            is_chapter_found = False
            for chapter in chapters:
                if chapter["Name"] == chapter_name:
                    is_chapter_found = True
                    chapter["Allegiance"] = "Renegade/Chaos"
                    chapter["Chapter of origin"] = chapter_of_origin
                    chapter["Founding"] = chapter_founding
            if not is_chapter_found:
                chapters.append({
                    "Name": chapter_name,
                    "Allegiance": "Renegade/Chaos",
                    "Faction": "",
                    "Chapter of origin": chapter_of_origin,
                    "Founding": chapter_founding,
                    "Legion": False,
                    "Homebrew": False,
                    })
        letter = letter.next_sibling
        while letter is not None and letter.name != "h3":
            letter = letter.next_sibling
    return chapters

def set_legions(chapters: list[list]):
    legions = ["Dark Angels", "Emperor's Children", "Iron Warriors", "White Scars", "Space Wolves", "Imperial Fists", "Night Lords", "Blood Angels", "Iron Hands", "World Eaters", "Ultramarines", "Death Guard", "Thousand Sons", "Sons of Horus", "Word Bearers", "Salamanders", "Raven Guard", "Alpha Legion"]
    for legion in legions:
        for chapter in chapters:
            if chapter["Name"] == legion:
                chapter["Legion"] = True
    return chapters
    

def write_chapters(chapters: list[list]):
    fieldnames = ['Name', 'Allegiance', "Faction", 'Chapter of origin', 'Founding', 'Legion', 'Homebrew']
    with open(OUTPUT_FILE, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(chapters)

chapters = set_legions(add_fandom_csm(add_fandom_sm(get_chapters_from_lexicanum())))
#print(chapters)
write_chapters(chapters)
#print(get_random_chapter(chapters))


