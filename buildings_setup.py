import networkx as nx

from pprint import *

buildings = ["Registrar's Office", "Student Center", "Library", "Cashier's Office", "Student Gym", "Basketball Arena",
             "Football Stadium", "Health Center", "Dining Hall", "Residence Hall", "Tech Support Center",
             "Student Store", "Physics Lab", "Chemistry Lab", "Testing Center", "Biology Lab", "Machine Shop",
             "Lecture Hall", "Computing Lab", "Music Hall", "Arts Building", "Conference Center", "Business Building",
             "Greenhouse", "Campus Security"]

g = nx.Graph()
for i in range(len(buildings)):
    g.add_node(buildings[i])
    for j in range(i, len(buildings)):
        if buildings[j] is not buildings[i]:
            g.add_edge(buildings[i], buildings[j], weight=((hash(buildings[i]) + hash(buildings[j])) % 21) + 1)

pp = PrettyPrinter(indent=4, width=80)
pp.pprint(str(g))
