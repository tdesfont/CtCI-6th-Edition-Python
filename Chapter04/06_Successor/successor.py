"""
    Chapter 4: Trees and Graphs
    Question 6: Successor
"""

def inorder_succ(node):
    if not node:
        return None
    if node.right:
        return leftMostChild(node.right)
    else:
        q = node
        x = q.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x

def leftMostChild(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node