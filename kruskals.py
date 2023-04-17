class Vertex(str):
    pass

class Edge(tuple):
    def wgt(self, weight: int):
        self.weight = weight
        return self

class Graph():
    def __init__(self, nodes: list[Vertex], edges: list[Edge]):
        self.nodes = nodes
        self.edges = edges

    def get_weight(self, edge: Edge) -> list[int]:
        return edge.weight

class DisjointSets:
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

def kruskals_algorithm(graph: Graph) -> list[Edge]:
    forest = DisjointSets(graph.nodes)
    mst: List[Edge] = []
    edges: List[Edge] = sorted(graph.edges, key=graph.get_weight)
    c = 1
    for left, right in edges:
        result = forest.union(left, right)
        if result:
            mst.append((left, right))
        print(str(c), str(tuple((left, right))), result, forest.parents, '\n')
        c += 1
    return mst

if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')

    edges =  [Edge((a, b)).wgt(7),\
        Edge((a, d)).wgt(5), Edge((b, c)).wgt(8),\
        Edge((b, d)).wgt(9), Edge((b, e)).wgt(7),\
        Edge((c, e)).wgt(5), Edge((d, e)).wgt(15),\
        Edge((d, f)).wgt(6), Edge((e, f)).wgt(8),\
        Edge((e, g)).wgt(9), Edge((f, g)).wgt(11)]
            
    graph = Graph([a, b, c, d, e, f, g], edges)    
    kruskals_algorithm(graph)
