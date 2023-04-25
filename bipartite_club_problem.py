import matplotviz as viz
import club_setup as cs
import BFS

if __name__ == "__main__":
    viz.draw_graph(cs.g, show_edge_weights=False)
    print(BFS.is_bipartite(cs.g, "Rob"))