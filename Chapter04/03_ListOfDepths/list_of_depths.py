"""
    Chapter 4: Trees and Graphs
    Question 3: List of Depths
"""

import networkx as nx
import pdb
import random
from collections import defaultdict
import matplotlib.pyplot as plt

# Build a tree

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

# Solve the problem

from collections import deque

def tree_exploration(root):
    queue = [root]
    depths_list = {0: [i.value for i in queue]}
    depth = 0
    tmp_queue = []
    while queue:
        for node in queue:
            depth += 1
            if node.left:
                tmp_queue.append(node.left)
            if node.right:
                tmp_queue.append(node.right)
        queue = tmp_queue
        tmp_queue = []
        if queue:
            depths_list[depth] = [i.value for i in queue]
    return depths_list

if __name__ == "__main__":
    array = [i for i in range(2**4-1)]
    tree = build_bst(array)
    print(tree_exploration(tree))

