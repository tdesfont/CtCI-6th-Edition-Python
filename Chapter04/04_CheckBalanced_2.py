"""
    Check Balanced: This is not a valid solution, the use of the print is not the most suitable here
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

is_balanced = True

def height(node):
    global is_balanced
    if not node:
        return 0
    else:
        hr, hl = height(node.left), height(node.right)
        is_balanced = (is_balanced and (abs(hr - hl) < 1))
        return 1 + max(hr, hl)

print(height(unbalanced_tree))
print(is_balanced)
