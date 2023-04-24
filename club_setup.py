import networkx as nx

from pprint import *

boys = ["Rob", "Matthew", "Tom", "Kyle", "Jared", "Alex", "Giovanni", "Tyler", "Brett", "Bart"]
girls = ["Amber", "Alisson", "Paige", "Nicole", "Kelsey", "Ashley", "Anna", "Shannon", "Jamie", "Emma"]

g = nx.Graph()

g.add_nodes_from(boys)
g.add_nodes_from(girls)
for i in range(len(boys)):
    for j in range(1 , 5):
        if not g.has_edge(boys[i], girls[(i + j) % len(girls)]):
            g.add_edge(boys[i],girls[(j + i) % len(girls)])

pp = PrettyPrinter(indent=4, width=80)
pp.pprint(str(g))