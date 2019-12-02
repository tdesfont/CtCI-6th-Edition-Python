"""
    Chapter 4: Trees and Graphs
    Question 4: Check if a tree is balanced
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def checkHeight(root):
    """
    Solution
    :param root:
    :return:
    """
    if not root:
        return -1
    leftHeight = checkHeight(root.left)
    if leftHeight == -float("inf"):
        return -float("inf")
    rightHeight = checkHeight(root.right)
    if rightHeight == -float('inf'):
        return -float('inf')
    heightDiff = leftHeight - rightHeight
    if abs(heightDiff) > 1:
        return -float("inf")
    else:
        return max(leftHeight, rightHeight)+1

def height(root):
    if not root:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    height_diff = abs(leftHeight - rightHeight)
    if height_diff > 1:
        return False
    else:
        return max(leftHeight, rightHeight)+1

if __name__ == "__main__":
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

    print(checkHeight(unbalanced_tree))
    print(bool(height(balanced_tree)))