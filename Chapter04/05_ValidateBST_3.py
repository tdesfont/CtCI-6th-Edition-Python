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

def checkBST(node, mini, maxi):
    if not node:
        return True
    if (mini != None and node.data <= mini) or (maxi != None and node.data > maxi):
        return False
    if (not checkBST(node.left, mini, node.data)) or (not checkBST(node.right, node.data, maxi)):
        return False
    return True

print(checkBST(tree, None, None))