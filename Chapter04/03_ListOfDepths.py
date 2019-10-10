
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

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

tree = A

from collections import deque

visited = defaultdict(bool)
L = {}

def bfs(root):
    queue = deque()
    queue.append(root)
    visited[root] = True
    height = 0
    while queue:
        L[height] = [q.data for q in queue]
        new_queue = []
        for r in queue:
            for node in [r.left, r.right]:
                if node and not visited[node]:
                    new_queue.append(node)
        height += 1
        queue = new_queue

bfs(tree)