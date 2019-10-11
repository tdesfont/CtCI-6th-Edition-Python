"""
    Check Balanced: Efficient solution in O(N)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

A = Node("A")
B = Node("B")
E = Node("E")
F = Node("F")
C = Node("C")
D = Node("D")
I = Node("I")
J = Node("J")
A.left = B
A.right = D
B.left = E
B.right = F
F.right = C
D.right = I
I.right = J

unbalanced_tree = A

X = Node("X")
Y = Node("Y")
Z = Node("Z")
X.left = Y
X.right = Z

balanced_tree = X

def checkHeight(root):
    if not root:
        return -1
    leftHeight = checkHeight(root.left)
    if leftHeight == -float('inf'):
        return -float('inf')
    rightHeight = checkHeight(root.right)
    if rightHeight == -float('inf'):
        return -float('inf')
    heightDiff = leftHeight - rightHeight
    if abs(heightDiff) > 1:
        return -float('inf')
    else:
        return max(leftHeight, rightHeight)+1

def isBalanced(root):
    return checkHeight(root) != -float('inf')

print(isBalanced(balanced_tree))