import matplotviz as viz
import buildings_setup as bs
import kruskals

if __name__ == '__main__':
    mst = kruskals.kruskals_algorithm(bs.g)
    bs.pp.pprint(mst)
    bs.g.clear_edges()
    for edge in mst:
        bs.g.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    viz.draw_graph(bs.g, show_edge_weights=True)
