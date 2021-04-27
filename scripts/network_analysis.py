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
    
    graph.add_nodes_from(data.keys())
    
    return graph
#------------------------------
def add_edge_directions(graph, pathways):
    
    for key, val in pathways.items():
        
        graph.add_edge(val["in"],val["out"], pathwayName = key)
    
    return graph 
#------------------------------
def make_edges(graph, data):
        
    for key, val in data.items():
        for item in val.keys():
            # add node attribute:
            if item == "relativeAbundance":
                print(val[item])
                graph.nodes[key][item]=val[item]
        
            # Get the directions:
            elif item == "pathways":
                print(val[item])
                graph = add_edge_directions(graph, val[item])
    
    return graph
#--------------------------------
def initialize_graph(data,make_fake=False):
    """
    Initialize networkx graph with specified nodes
    """
    import networkx as nx
    
    if make_fake==True:
        # make an empty directed graph:
        graph = nx.MultiDiGraph()
        
        # add fake nodes: 
        graph_with_nodes = make_nodes(graph, data)

        # add fake edges:
        graph_with_edges = make_edges(graph_with_nodes, data)
        
        return graph_with_edges
     
    # if real input received:
    else: 
        graph = nx.from_pandas_edgelist(data,
                                        "source",
                                        "target",
                                        ["weight"],
                                       create_using=nx.MultiDiGraph())
        
        return graph

#-------------------------------------------

def draw_network_graph(graph):
    """
    Plots the network graph taken from the input
    """
    import matplotlib.pyplot as plt
    import random
    
    for u,v,d in graph.edges(data=True):
        d['weight'] = random.random()

    edges,weights = zip(*nx.get_edge_attributes(graph,'weight').items())

    
    nx.draw_networkx(graph, 
                     with_labels=True,
                     arrows=True, 
                     arrowsize=20,
                     node_size=900,
                     node_color='skyblue',
                     width=6,
                    pos=nx.spring_layout(graph,k=4),
                    edge_cmap=plt.cm.GnBu,
                    edge_color=weights,
                    edgelist=edges,
                    font_size=14)
    
    #plt.figure(figsize=(60,40))
    ax = plt.gca()
    plt.axis("off")
    ax.margins(0.08)
    
    plt.tight_layout()
    plt.show()





