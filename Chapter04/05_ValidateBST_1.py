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

index = 0
def copyBST(root, array):
    global index
    if not root:
        return
    copyBST(root.left, array)
    array[index] = root.data
    index += 1
    copyBST(root.right, array)

def checkBST(root, size):
    array = [None for i in range(size)]
    copyBST(root, array)
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

print(checkBST(A, 6))