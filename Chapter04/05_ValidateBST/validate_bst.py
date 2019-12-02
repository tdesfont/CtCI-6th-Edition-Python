"""
    Chapter 4: Trees and Graph
    Question 5: Validate BST
"""

import networkx as nx
import pdb
import random
from collections import defaultdict
import matplotlib.pyplot as plt

def check_bst(node, inf_bound=-float("inf"), sup_bound=+float("inf")):
    if not node:
        return True
    if not inf_bound <= node.value <= sup_bound:
        return False
    return check_bst(node.left, inf_bound=inf_bound, sup_bound=node.value) and check_bst(node.right, inf_bound=node.value, sup_bound=sup_bound)

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

def graph_from_tree(node, graph=None):
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
    array = [i for i in range(2**5-1)]
    tree = build_bst(array)
    print(check_bst(tree))
    graph = graph_from_tree(tree)
    visualise_graph(graph)