import networkx as nx
import matplotlib.pyplot as plt
from random import choice
from libsmcsv import SpaceMarineChaptersDataset

FILES_OFFICIAL = ["space-marine-chapters.csv", "space-marine-chapters-homebrew-example.csv"]
FILES_HOMEBREW = ["space-marine-chapters.csv", "space-marine-chapters-homebrew.csv"]
files = FILES_OFFICIAL
chapters_dataset = SpaceMarineChaptersDataset(files)

G = nx.DiGraph()

#print(chapters_dataset.get_chapter('Novamarines'))
#print(chapters_dataset.get_lineage('Novamarines'))
values_map = {
    'Renegade/Chaos': 0,
    'Loyalist': 1
    }
values = []

def add_subgraph(chapter_name: str):
    for generation in chapters_dataset.get_descendants(chapter_name):
        for chapter in generation:
            G.add_node(chapter['Name'])
            values.append(values_map[chapter['Allegiance']])
            parents = chapter["Chapter of origin"].split(" & ")
            for parent in parents:
                if parent in G:
                    G.add_edge(parent, chapter['Name'])

legions = chapters_dataset.filter_chapter(
    chapters_dataset.chapters,
    {"Legion": True})
for legion in legions:
    print(legion['Name'])

for chapter in legions:
    add_subgraph(chapter['Name'])

    pos = nx.bfs_layout(G, chapter['Name'])
    nx.draw(G, pos, with_labels=True, cmap=plt.get_cmap('spring'), node_color=values)
    plt.tight_layout()
    #plt.show()
    plt.savefig(
        f"results/{chapter['Name']}.png",
        transparent=True,
        )
    plt.close()

    G = nx.DiGraph()
    values = []