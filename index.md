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
```

# First Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

# Minimally connecting paths between University buildings

**Informal Description**: We have a network of buildings at some university with potential paths
(and the cost to build those paths), we want to find the set of paths that connects all of the buildings
on campus while using as little resources as possible.

> **Formal Description**:
>  * Input: A set of university buildings (nodes) and a dense, procedurally generated set of edges connecting the nodes.
>  * Output:

**Graph Problem/Algorithm**: MST -- Kruskal's Algorithm


**Setup code**:

```python
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

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

