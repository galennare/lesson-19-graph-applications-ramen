import networkx as nx

from pprint import *

buildings = ["Registrar's Office", "Student Center", "Library", "Cashier's Office", "Student Gym", "Basketball Arena",
             "Football Stadium", "Health Center", "Dining Hall", "Residence Hall", "Tech Support Center",
             "Student Store", "Physics Lab", "Chemistry Lab", "Testing Center", "Biology Lab", "Machine Shop",
             "Lecture Hall", "Computing Lab", "Music Hall", "Arts Building", "Conference Center", "Business Building",
             "Greenhouse", "Campus Security"]

g = nx.Graph()
for building in buildings:
    g.add_node(building)
    for other in buildings:
        if other is not building:
            g.add_edge(building, other, weight=((hash(building) + hash(other)) % 21) + 1)

pp = PrettyPrinter(indent=4, width=80)
pp.pprint(str(g))
