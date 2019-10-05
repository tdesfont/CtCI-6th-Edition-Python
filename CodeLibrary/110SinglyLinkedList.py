"""
    Implement a Singly Linked List in Python.
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def appendToTail(self, d):
        end = Node(d)
        n = self
        while n.next:
            n = n.next
        n.next = end

    def __str__(self):
        n = self
        string = ""
        while n.next:
            string += str(n.value)
            string += "->"
            n = n.next
        string += str(n.value)
        return string


class SinglyLinkedList:

    def __init__(self, d):
        self.head = Node(d)

    def deleteNode(self, d):
        """
            Delete the node which value is d without deallocation.
        :param d:
        :return:
        """
        n = self.head
        if n.value == d:
            self.head = n
        while n.next:
            if n.next.data == d:
                n.next = n.next.next # Cross the node to be deleted
                return self
            n = n.next

if __name__ == "__main__":
    l = SinglyLinkedList(0)
    l.head.appendToTail(1)
    l.head.appendToTail(2)
    l.head.appendToTail(3)
    l.head.appendToTail(4)
    print(l.head)