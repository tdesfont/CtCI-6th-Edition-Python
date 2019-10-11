"""
    Check Balanced: Inefficient Solution in O(N.log(N))
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

def getHeight(root):
    if not root:
        # Base case
        return -1
    return max(getHeight(root.left), getHeight(root.right)) + 1

def isBalanced(root):
    if not root:
        return True
    heightDiff = getHeight(root.left) - getHeight(root.right)
    if abs(heightDiff) > 1:
        return False
    else:
        return isBalanced(root.left) and isBalanced(root.right)

print(isBalanced(unbalanced_tree))