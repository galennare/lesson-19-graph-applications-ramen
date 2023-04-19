import matplotviz as viz
import campus_websites as cw
import dfs

if __name__ == '__main__':
    sp = dfs.dfs(cw.g)
    cw.pp.pprint(sp)
    cw.g.clear_edges()
    for edge in sp:
        cw.g.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    viz.draw_graph(cw.g, show_edge_weights=True)
