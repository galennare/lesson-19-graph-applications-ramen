import networkx as nx


class Vertex(str):
    """
        Wrapper class for vertices
    """
    pass


class DisjointSets:
    """
        Disjoint sets implementation from lesson 18
    """
    def __init__(self, nodes: list[Vertex]):
        self.parents = {}
        for node in nodes:
            self.parents[node] = node

    def find(self, current: Vertex) -> Vertex:
        while self.parents[current] != current:
            current = self.parents[current]
        return current

    def union(self, left: Vertex, right: Vertex):
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parents[right_root] = left_root
        return left_root != right_root


def kruskals_algorithm(graph: nx.Graph) -> list[tuple]:
    """
        Kruskal's Algorithm implementation adapted from lesson 18, takes in a networkx graphs and returns a list of
        networkx compatible edges of the Minimum-Spanning Tree.
    """
    vertices = [Vertex(node) for node in graph]
    forest = DisjointSets(vertices)
    mst = []
    edges = sorted([edge for edge in graph.edges.data()], key=lambda edge: edge[2]['weight'])
    c = 1
    for edge in edges:
        left, right = edge[:2]
        result = forest.union(left, right)
        if result:
            mst.append((left, right, edge[2]))
        print(str(c), str(tuple((left, right))), result, forest.parents, '\n')  # Debug statement for alg, comment for less output
        c += 1
    return mst
