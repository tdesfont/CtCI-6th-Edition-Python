"""
    Chapter 4: Trees and Graph
    Question 2: Minimal Tree
"""

import networkx as nx
import pdb
import random
from collections import defaultdict
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def build_bst(array):
    n = len(array)
    if n == 0:
        return None
    middle = n//2
    node = TreeNode(array[middle])
    node.left = build_bst(array[:middle])
    node.right = build_bst(array[middle+1:])
    return node

def graph_from_tree(node, graph):
    if node:
        if not graph:
            graph = defaultdict(set)
        if node.left:
            graph[node.value].add(node.left.value)
            graph_from_tree(node.left, graph)
        if node.right:
            graph[node.value].add(node.right.value)
            graph_from_tree(node.right, graph)
    return graph

def visualise_graph(graph):
    G = nx.Graph()
    for source in graph:
        for target in graph[source]:
            G.add_edges_from([(source, target)])
    nx.draw(G, with_labels=True, node_color="red")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    array = [i for i in range(2**4-1)]
    tree = build_bst(array)
    graph = graph_from_tree(tree, None)
    visualise_graph(graph)
