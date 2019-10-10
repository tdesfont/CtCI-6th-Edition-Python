"""
    Implementation of a Binary Tree

    Questions:
        Check that the tree is a Binary Search Tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)

if __name__ == "__main__":
    A = Node(8)
    B = Node(4)
    C = Node(10)
    D = Node(2)
    E = Node(6)
    F = Node(20)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F
    tree = Tree(A)

    in_order_traversal(tree.root)