import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
import colorsys

import time


def draw_graph(g: nx.Graph) -> str:
    """
        Function that takes in a networkx Graph and draws it to a PNG file. Makes the edges multicolored and writes the labels on your nodes.
        Returns the name of the image file created.
    """
    hues = np.linspace(0, 1, len(g.edges))
    edge_colors = []
    for hue in hues:
        edge_colors.append(colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    nx.draw(g, with_labels=True, edge_color=edge_colors)
    filename = "graph_plot_{0}.png".format(time.time())
    plt.savefig(filename)
    return filename
