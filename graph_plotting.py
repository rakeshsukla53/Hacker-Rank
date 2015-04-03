__author__ = 'rakesh'

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):

    #for extracting nodes from the graph

    #nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    nodes = set([n1 for n1 in graph])

    print nodes

    G = nx.Graph()

    for node in nodes:
        G.add_node(node)

    #for edge in graph:
    #    G.add_edge(edge[0], edge[1])   #add edges between the nodes

    G.add_edge(10, 9)
    G.add_edge(2, 1)
    G.add_edge(3, 1)
    G.add_edge(4, 3)
    G.add_edge(5, 2)
    G.add_edge(6, 1)
    G.add_edge(7, 2)   #add edges between the vertices
    G.add_edge(8, 6)
    G.add_edge(9, 8)
    G.add_edge(10, 8)

    #print G.edge  #print out the edges of the graph

    print G.edges(1)  #f you want to find out the number of edges from 10

    print G.edges()  #gives you list of all the edges

    #print G.edge  #gives you a very propert format

    pos = nx.shell_layout(G)

    nx.draw(G, pos)

    plt.show()

graph = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]

draw_graph(graph)

#We can create graph like a dictionary with the keys representing the numbers

'''
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

The keys of the dictionary above are the nodes of our graph. The corresponding values are lists with the nodes, which are connecting by an edge. There is no simpler and more elegant way to represent a graph.

An edge can be seen as a 2-tuple with nodes as elements, i.e. ("a","b")

Function to generate the list of all edges:

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

print(generate_edges(graph))

This code generates the following output, if combined with the previously defined graph dictionary:


$ python3 graph_simple.py
[('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('b', 'c'), ('b', 'e'), ('e', 'c'), ('e', 'b'), ('d', 'c')]
'''