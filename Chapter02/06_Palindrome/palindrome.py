"""
Chapter 2.6: Check if a Linked List is a Palindrome
"""

class LinkedListNode:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

def check_palindrome(dll):
    """

    :param dll: Doubly Linked List
    :return:
    """
    runner = dll
    length = 1
    while runner.next:
        runner = runner.next
        length += 1
    current = dll
    for i in range(length//2):
        if current.value != runner.value:
            return False
        current = current.next
        runner = runner.prev
    return True

if __name__ == "__main__":
    # Create a palindromic doubly linked list
    N = 9
    Nodes = [LinkedListNode(abs(N//2-i)) for i in range(N)]
    for i in range(len(Nodes)-1):
        Nodes[i].next = Nodes[i+1]
        Nodes[i+1].prev = Nodes[i]
    print(check_palindrome(Nodes[0]))
