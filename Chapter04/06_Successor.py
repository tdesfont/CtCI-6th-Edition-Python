"""
    Successor: Find the next node in the in order traversal.
"""

class Node:

    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.parent = None

    def add_left(self, node):
        self.left = node
        node.parent = self

    def add_right(self, node):
        self.right = node
        node.parent = self

A = Node(8)
B = Node(4)
C = Node(15)
D = Node(1)
E = Node(5)
F = Node(10)
G = Node(19)

A.add_left(B)
B.add_left(D)
B.add_right(E)
A.add_right(C)
C.add_left(F)
C.add_right(G)

tree = A

def inOrderSucc(node):
    if not node:
        return None
    if node.right:
        return leftMostChild(node.right)
    else:
        q = node
        x = q.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x

def leftMostChild(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

print(inOrderSucc(D).data)