import networkx as nx
import matplotlib.pyplot as plt
import djikstras_setup
import pprint

def solution (G: nx.Graph) -> nx.Graph:
    solution = nx.single_source_dijkstra(G, "Registrar's Office", "Student Gym")
    print("The shortest path from to is: ")
    print(solution)
    return solution

if __name__ == '__main__':
