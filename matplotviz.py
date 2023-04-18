import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
import colorsys

import time


def draw_graph(graph: nx.Graph, show_edge_weights=False) -> str:
    """
        Function that takes in a networkx Graph and draws it to a PNG file. Makes the edges multicolored and writes the labels on your nodes.
        Scales the edge width by its weight if show_edge_weights=True
        Returns the name of the image file created.
    """
    # Make the default size bigger; it needs to be with very dense graphs
    size = max(len(graph.nodes) / 2, 5)
    plt.rcParams['figure.figsize'] = [size, size]

    # Calculate edge colors
    hues = np.linspace(0, 1, len(graph.edges))
    edge_colors = []
    if show_edge_weights:
        for hue in hues:
            r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            edge_colors.append((r, g, b, 0.5))
    else:
        for hue in hues:
            edge_colors.append(colorsys.hsv_to_rgb(hue, 1.0, 1.0))

    # Draw the thing
    if not show_edge_weights:
        nx.draw(graph, with_labels=True, edge_color=edge_colors, node_size=600)
    else:
        nx.draw(graph, with_labels=True, edge_color=edge_colors, node_size=600, width=[edge[2]['weight'] / 2 for edge in graph.edges.data()])
    filename = "graph_plot_{0}.png".format(time.time())
    plt.savefig(filename)
    return filename
