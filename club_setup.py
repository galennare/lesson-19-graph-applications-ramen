import networkx as nx

from pprint import *

members = ["Rob", "Matthew", "Tom", "Kyle", "Jared", "Alex", "Giovanni", "Tyler", "Brett", "Bart", "Amber", "Alisson", "Paige", 
           "Nicole", "Kelsey", "Ashley", "Anna", "Shannon", "Jamie", "Emma"]

g = nx.Graph()

for i in range(len(members)):
    g.add_node(members[i])
    for j in range(i, (i + 3) % len(members)):
        if not g.has_edge(members[i], members[j]):
            g.add_edge(members[i],members[j])

pp = PrettyPrinter(indent=4, width=80)
pp.pprint(str(g))