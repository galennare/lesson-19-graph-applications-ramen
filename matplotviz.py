import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
import colorsys

import time


def draw_graph(g: nx.Graph):
    hues = np.linspace(0, 1, len(g.edges))
    edge_colors = []
    for hue in hues:
        edge_colors.append(colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    nx.draw(g, with_labels=True, edge_color=edge_colors)
    plt.savefig("graph_plot_{0}.png".format(time.time()))
