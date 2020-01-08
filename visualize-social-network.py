import matplotlib.pyplot as plt
import os
import networkx as nx

def visualize():
    my_graph = nx.Graph()
    path = "a path to the directory"
    files = os.listdir(path)
    filenames = [f for f in files if os.path.isfile(os.path.join(path, f))]
    for filename in filenames:
        if ".edges" in filename:
            edges = nx.read_edgelist(filename)
            my_graph.add_edges_from(edges.edges())
    options = {
        "node_color": "blue",
        "edge_color": "red",
        "node_size": 200,
        "width": 0.3,
        "font_size": 2,
        "alpha": 0.7
    }
    #pos=nx.spring_layout(my_graph)
    nx.draw(my_graph, with_labels=True, **options)
    plt.show()
