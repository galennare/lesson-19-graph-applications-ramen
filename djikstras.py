import networkx as nx
import matplotlib.pyplot as plt
import djikstras_setup
import heapq
import pprint


# Daniel Yang
# The Problem
# The University of Mars has an important task for you. Since Mars is a relatively new planet to colonize, we need to be efficient with land.
# We are asking you to find the shortest pathing through our graph of the buildings so that we can efficiently reserve land to build our campus.

def solution (G: nx.Graph) -> nx.Graph:
    solution = nx.single_source_dijkstra(G, "", "")
    print("The shortest path from to is: ")
    print(solution)
    return solution

solution(G)
