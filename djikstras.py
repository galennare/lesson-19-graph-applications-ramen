import networkx as nx
from pprint import *
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = [["Registrar's Office", 1, 1],["Student Center", 1, 8],["Library", 2, 4],["Cashier's Office", 3, 1],["Basketball Arena", 3, 9],
         ["Football Stadium", 2, 6],["Health Center", 4, 2],["Dining Hall", 4, 5],["Residence Hall", 5, 8],["Tech Support Center", 5, 2],
         ["Student Store", 6, 6],["Physics Lab", 7, 2],["Chemistry Lab", 8, 3],["Testing Center", 7, 5],["Biology Lab", 6, 9],
         ["Machine Shop", 7, 9],["Lecture Hall", 6, 2],["Computing Lab", 8, 1],["Music Hall", 8, 7],["Student Gym", 9, 9]]

for node in nodes:
    G.add_node(node[0], pos = (node[1], node[2]))

edges = [
    ["Registrar's Office", "Student Center", 14],
    ["Registrar's Office", "Library", 18],
    ["Library", "Basketball Arena", 20],
    ["Library", "Cashier's Office", 30],
    ["Student Center", "Cashier's Office", 15],
    ["Cashier's Office", "Football Stadium", 10],
    ["Football Stadium", "Health Center", 28],
    ["Health Center", "Residence Hall", 10],
    ["Cashier's Office", "Dining Hall", 32],
    ["Dining Hall", "Residence Hall", 25],
    ["Health Center", "Tech Support Center", 17],
    ["Tech Support Center", "Biology Lab", 30],
    ["Residence Hall", "Biology Lab", 17],
    ["Residence Hall", "Student Store", 33],
    ["Student Store", "Physics Lab", 40],
    ["Physics Lab", "Chemistry Lab", 38],
    ["Chemistry Lab", "Computing Lab", 29],
    ["Computing Lab", "Music Hall", 19],
    ["Music Hall", "Student Gym", 12],
    ["Student Store", "Testing Center", 12],
    ["Biology Lab", "Testing Center", 27],
    ["Biology Lab", "Machine Shop", 25],
    ["Machine Shop", "Lecture Hall", 29],
    ["Lecture Hall", "Student Gym", 32],
]

for pair in edges:
    G.add_edge(pair[0], pair[1], weight = int(pair[2]))

#Drawing Graph: 

# nodes
nx.draw_networkx_nodes(G, pos = nx.get_node_attributes(G,'pos'), node_size=1600)

# edges
nx.draw_networkx_edges(G, pos = nx.get_node_attributes(G,'pos'), width=2)
nx.draw_networkx_edges(G, pos = nx.get_node_attributes(G,'pos'), width=2, alpha=1, edge_color="y")

# node labels
nx.draw_networkx_labels(G, pos = nx.get_node_attributes(G,'pos'), font_size=5, font_family="cursive")

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos = nx.get_node_attributes(G,'pos'), edge_labels=edge_labels)

ax = plt.gca()
ax.margins(0.02)
plt.axis("off")
plt.tight_layout()
plt.show()

def solution (G: nx.Graph) -> nx.Graph:
    solution = nx.single_source_dijkstra(G, "Registrar's Office", "Student Gym")
    print("The shortest path from Registrar's Office to Student Gym is: ")
    print(solution)
    return solution

solution(G)

