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


    def get_chapter(self, chapter_name: str) -> dict|None:
        """
        :param chapter_name: Name of the chapter to be extracted.
        :type chapter_name: str
        :return: The chapter with matching name. If none are found, None.
        """
        try:
            return next(filter(lambda x: x.get('Name') == chapter_name, self.chapters))
        except StopIteration:
            return None
    
    def get_descendants(self, chapter_name: str, recursive=True, include_self=True) -> list[list[dict]]:
        """
        """
        result = []
        next_gen = [self.get_chapter(chapter_name)]
        while next_gen != []:
            current_gen = next_gen 
            next_gen = []
            for gen_descendant in current_gen:
                # find all the direct descendants
                for chapter in self.chapters:
                    parents = chapter["Chapter of origin"].split(" & ")
                    for parent in parents:
                        #print(current_gen)
                        #print(f"Current: {chapter['Name']} - Parent: {parent}")
                        if parent in [c['Name'] for c in current_gen] and chapter not in next_gen:
                            next_gen.append(chapter)
            result.append(current_gen)
        return result

        for chapter in self.chapters:
            if include_self and chapter["Name"] == chapter_name:
                result.append(chapter)
                continue
            parents = chapter["Chapter of origin"].split(" & ")
            for parent_name in parents:
                if parent_name == chapter_name:
                    result.append(chapter)
                elif recursive:
                    lineage = self.get_lineage(parent_name)
                    print(lineage)
                    for lc in lineage:
                        if lc not in result:
                            result.append(lc)
        return result

    def get_lineage(self, chapter_name: str) -> list[dict]:
        """
        """
        lineage = []
        cur_chapter = self.get_chapter(chapter_name)
        lineage.append(cur_chapter)
        while cur_chapter['Chapter of origin'] != '':
            #print(cur_chapter)
            cur_chapter = self.get_chapter(cur_chapter['Chapter of origin'])
            lineage.append(cur_chapter)
        return lineage

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
        """
        Ensure that the chapter list is correct.

        TODO : check for duplicates
        """
        for i in range(len(self.chapters)):
            chapter = self.chapters[i]
            self.validate_chapter(chapter)
            chapters_origin = chapter["Chapter of origin"].split(" & ")
            for co in chapters_origin:
                if co != '' and not co in [c["Name"] for c in self.chapters]:
                    print(f"{chapter['Name']} has incorrect parent ({co}.")
            if chapter['Name'][:4] == 'The ':
                for chapter_bis in self.chapters:
                    if chapter_bis['Name'] == chapter['Name'][4:]:
                        print(f"Warning, both {chapter_bis['Name']} and {chapter['Name']} exist.")
            for j in range(i+1,len(self.chapters)):
                if chapter['Name'] == self.chapters[j]['Name']:
                    print(f"Duplicate chapter {chapter['Name']}.")

    def write_chapters(self, filename: str):
        """
        :param filename: Name of the file in which to write the list of chapters
        :type filename: str
        """
        with open(filename, 'w') as g:
            writer = csv.DictWriter(
                g,
                fieldnames=("Name", "Allegiance", "Faction", "Chapter of origin", "Founding", "Status", "Legion", "Homebrew")
                )
            writer.writeheader()
            writer.writerows(self.chapters)

    @classmethod
    def filter_chapter(cls, chapters: list[dict], criteria: dict) -> list[dict]:
        """
        This will return all the chapters matching all the conditions in criteria.

        :param chapters: List of chapters
        :type chapters: list[dict]
        :param criteria: Criteria used
        :type criteria: list[dict]
        :return: List of chapters matching the criteria
        :rtype: list[dict]
        """
        res = []
        for chapter in chapters:
            criterium_met = True
            for key in criteria.keys():
                if chapter[key] != criteria[key]:
                    criterium_met = False
                    break
            if criterium_met:
                res.append(chapter)
        return res

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

