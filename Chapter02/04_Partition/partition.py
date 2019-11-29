"""
    Partition
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(node, x):
    head = node
    tail = node
    while node:
        next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head

if __name__ == "__main__":
    values = [8, 3, 2, 1, 4, 9, 19]
    nodes = []
    for v in values:
        node = Node(v)
        nodes.append(node)
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    head = partition(nodes[0], 5)
    node = head
    while node:
        print(node.data)
        node = node.next