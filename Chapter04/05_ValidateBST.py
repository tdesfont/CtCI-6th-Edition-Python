"""
    Validate if an input tree is a valid Binary Search Tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

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
bst = Tree(A)

traversal = []

def in_order_traversal(node):
    global traversal
    if node:
        in_order_traversal(node.left)
        traversal.append(node.data)
        in_order_traversal(node.right)

in_order_traversal(bst.root)

def check_is_sorted(l):
    is_sorted = True
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return is_sorted

print(traversal)

print(check_is_sorted(traversal))