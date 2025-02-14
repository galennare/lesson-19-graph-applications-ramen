# Team Ramen - Graph Applications Problems

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Galen Nare (gnare@udel.edu)
* Second member (email)
* Third member (email)
* Fourth member (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```

# First Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

# Minimally connecting paths between University buildings

**Informal Description**: We need to connect a wired Internet network of buildings at some university with potential cable paths
(and the cost to build those paths as the weight of the edges), we want to find the set of paths that connects all the buildings
on campus while using as little resources as possible.

> **Formal Description**:
>  * Input: A set of university buildings (25 nodes) and a dense, procedurally generated set of edges connecting the nodes.
    Uses the formula `((hash(left_node) + hash(right_node)) % 20) + 1` for the weights.
>  * Output: A set of edges that connect all nodes in a Minimum Spanning Tree

**Graph Problem/Algorithm**: MST -- Kruskal's Algorithm


**Setup code**:

```python
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
```

**Visualization**:

"Before" graph (weights are represented by edge thickness, 
ranging from 1 to 20; using `matplotlib`:
![before](images/kruskals_buildings_before.png)

**Solution code:**

```python
import matplotviz as viz
import buildings_setup as bs
import networkx as nx

if __name__ == '__main__':
    mst = nx.minimum_spanning_tree(bs.g, algorithm="kruskal")
    bs.pp.pprint(mst)
    bs.g.clear_edges()
    for edge in mst.edges(data=True):
        print(edge)
        bs.g.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    viz.draw_graph(bs.g, show_edge_weights=True)
```

**Output**

Edges selected for the Minimum Spanning Tree calculated by Kruskal's Algorithm:
```python
("Registrar's Office", 'Library', {'weight': 1})
("Registrar's Office", 'Testing Center', {'weight': 1})
("Registrar's Office", 'Conference Center', {'weight': 1})
("Registrar's Office", 'Student Gym', {'weight': 4})
('Student Center', 'Business Building', {'weight': 1})
('Student Center', 'Biology Lab', {'weight': 2})
('Library', 'Football Stadium', {'weight': 1})
('Library', 'Physics Lab', {'weight': 1})
("Cashier's Office", 'Residence Hall', {'weight': 1})
("Cashier's Office", 'Student Store', {'weight': 3})
('Student Gym', 'Dining Hall', {'weight': 1})
('Student Gym', 'Tech Support Center', {'weight': 1})
('Student Gym', 'Health Center', {'weight': 2})
('Student Gym', 'Basketball Arena', {'weight': 3})
('Student Gym', 'Machine Shop', {'weight': 3})
('Dining Hall', 'Chemistry Lab', {'weight': 1})
('Dining Hall', 'Lecture Hall', {'weight': 1})
('Dining Hall', 'Arts Building', {'weight': 2})
('Residence Hall', 'Business Building', {'weight': 2})
('Student Store', 'Arts Building', {'weight': 1})
('Student Store', 'Greenhouse', {'weight': 1})
('Student Store', 'Computing Lab', {'weight': 2})
('Biology Lab', 'Music Hall', {'weight': 1})
('Music Hall', 'Campus Security', {'weight': 1})
```

Visualization of the MST (edge weights visualized with line thickness):
![after](images/kruskals_result.png)

**Interpretation of Results**:
    
With Kruskal's Algorithm we are able to find the least expensive way to connect all the
University buildings on this wired Internet network. This setup can find the solution for this type
of problem quickly, with any number of "buildings to connect". This could help network engineers
prototype a cost-effective solution for Universities or other multi-building campuses.
