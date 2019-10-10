"""
    Implementation of a Binary Tree

    Questions:
        Check that tree is binary
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

if __name__ == "__main__":
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    tree = Tree(A)