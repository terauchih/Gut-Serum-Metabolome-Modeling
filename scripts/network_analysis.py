"""
Functions to run network analysis from given data

"""
## Hinako Terauchi
## Mar 29 2021
#----------------------------
import networkx as nx

#----------------------------
def make_fake_data():
    """
    Making a small fake data to test
    
    Creates a pre-determined simple set of nodes with attributes.
    Calls make_edges() function to create edges.
    Returns the nodes and the edges after. 
    """
    
    fake_data = {"bacA":{"relativeAbundance":0.1, 
                          "pathways":{"pathA":{"in":"a", "out":("b","c")}}},
                  "bacB":{"relativeAbundance":0.4,
                          "pathways":{"pathB":{"in":"b", "out": "c"}}},
                  "bacC":{"relativeAbundance":0.5,
                          "pathways":{"pathC":{"in":"c", "out":("a", "b")},
                                      "pathD":{"in":"c", "out":"d"}}}
                 }

    print("fake data:",fake_data)
    
    return fake_data
#-----------------------------
def make_nodes(graph, data):
    
    graph.add_nodes_from(nodes)
    
    return graph_with_nodes

#------------------------------
def make_edges():
    
    # stufff
    return None

#--------------------------------
def initialize_graph(data):
    """
    Initialize networkx graph with specified nodes
    """
    import networkx as nx
    
    # make an empty directed graph:
    graph = nx.MultiDiGraph()

    # add nodes: 
    graph_with_nodes = make_nodes(graph, data)
    
    # add edges:
    graph_with_edges = make_edges(graph_with_nodes, data)

    return graph_with_edges

#-------------------------------------------

def draw_network_graph(graph):
    """
    Plots the network graph taken from the input
    """
    
    #graphing
    
    nx.draw(graph, with_labels=True)





