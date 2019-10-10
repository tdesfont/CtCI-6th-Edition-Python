"""
    This is the most simple Tree object, it is also often assumed that a tree
    is a binary tree or a binary search tree, this is not true.

    Questions:
        BFS/DFS
        PostOrder, InOrder, PreOrder
        Common Ancestor
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = root

def build_sample_tree():
    """
        This tree is not a binary tree (A has four children)
    """
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")
    A.children = [B, E, F, G]
    B.children = [C, D]
    E.children = [D]
    F.children = [G, H]
    tree = Tree(A)
    return tree