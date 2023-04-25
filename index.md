# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Galen Nare (gnare@udel.edu)
* Dylan Giletto (dgiletto@udel.edu)
* Daniel Yang (daniely@udel.edu)
* Fourth member (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# The Shortest Path on Campus

**Informal Description**: The University of Mars has an important task for you. Since Mars is a relatively new planet to colonize, we need to be efficient with land.
We are asking you to find the shortest pathing between the Registrar's Office and the Student Gym. Each edge weight symbolizes the distance in meters between each building.

> **Formal Description**:
>  * Input: A graph where each edge weight represents the distance between buildings.
>  * Output: Prints the shortest path with its length and the nodes visited in order.

**Graph Problem/Algorithm**: Djikstra's Algorithm


**Setup code**:

```G = nx.Graph()

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
```

**Visualization**:

![Image goes here](djikstras.png)

**Solution code:**

```def solution (G: nx.Graph) -> nx.Graph:
    solution = nx.single_source_dijkstra(G, "Registrar's Office", "Student Gym")
    print("The shortest path from Registrar's Office to Student Gym is: ")
    print(solution)
    return solution

solution(G)
```

**Output**

```The shortest path from Registrar's Office to Student Gym is: 
(180, ["Registrar's Office", 'Student Center', "Cashier's Office", 'Football Stadium', 'Health Center', 'Residence Hall', 'Biology Lab', 'Machine Shop', 'Lecture Hall', 'Student Gym'])
```

**Interpretation of Results**:

With the use of Djikstra's Algorithm on the graph of the University of Mars' campus, we can calculate the shortest path between two locations very easily. 
Now we know the shortest distance between the Registrar's Office and the Student Gym, while also finding the locations visited in-between. We can also use
this algorithm for any other pair of destinations on this graph.

