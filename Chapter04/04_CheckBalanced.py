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

def height(root):
    """
        Measure the height of the tree
    :param root:
    :return:
    """
    if not root:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

def check_balanced_tree(root):
    if not root:
        return True
    if abs(height(root.left)-height(root.right)) > 1:
        print(False)
    else:
        check_balanced_tree(root.left)
        check_balanced_tree(root.right)

check_balanced_tree(unbalanced_tree)
height(unbalanced_tree)