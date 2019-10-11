"""
    Validate if an input tree is a valid Binary Search Tree
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

tree = A

last_printed = None
def checkBST(node):
    global last_printed
    if not node:
        return True
    if not checkBST(node.left):
        return False
    if last_printed and node.data <= last_printed:
        return False
    last_printed = node.data
    if not checkBST(node.right):
        return False
    return True

print(checkBST(tree))