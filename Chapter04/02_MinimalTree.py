input = [2, 5, 8, 10, 12, 15, 20]

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def build_tree(ordered_list):
    n = len(ordered_list)
    if n == 0:
        return None
    root = Node(ordered_list[n//2])
    root.left = build_tree(ordered_list[:n//2])
    root.right = build_tree(ordered_list[n//2+1:])
    return root

tree = build_tree(input)

l = []

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        l.append(node.data)
        in_order_traversal(node.right)

in_order_traversal(tree)
assert l == input
print('test [OK]')
