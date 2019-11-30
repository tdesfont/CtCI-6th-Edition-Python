"""
    2.2 Return Kth to last
"""

class LinkedListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

def kth_to_last(sll, k):
    """
        Runner technique on the singly linked list in order
        to have a node in advance.
    :param sll:
    :param k:
    :return:
    """
    runner = sll
    for i in range(k):
        if not runner:
            return None
        runner = runner.next
    node = sll
    while runner:
        if not runner.next:
            return node.val
        node = node.next
        runner = runner.next

if __name__ == "__main__":

    Nodes = [
             LinkedListNode(0),
             LinkedListNode(1),
             LinkedListNode(2)
             ]
    for i in range(len(Nodes)-1):
        Nodes[i].next = Nodes[i+1]

    print(kth_to_last(Nodes[0], -1))