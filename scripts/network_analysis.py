"""
Functions to run network analysis from given data

"""
import networkx as nx


## Making a fake input data:
fake_nodes = ["metA", "metB", "metC"]

fake_edges = [("metA", "metB", {"weight":2}),
             ("metB", "metC", {"weight":1}),
             ("metA", "metC", {"weight":1})]

def network_analysis(nodes, edges):
    """
    Runs the networkd analysis for the metabolic pathways of bacteria in group.
    """

    # make an empty directed graph:
    G = nx.DiGraph()

    # add nodes and edges from the input:
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    # draw it:
    nx.draw(G)

    return G
