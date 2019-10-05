"""
    A tree node for any tree (Directed Acyclic Graph).
    Not necessarily for Binary Tree.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

if __name__ == "__main__":

    nodes = 6
    graph = {0: [1, 2, 3], 1: [4, 5], 2: [5]}

    index_nodes = []
    for i in range(nodes):
        index_nodes.append(TreeNode(i))

    for node in graph:
        for child in graph[node]:
            index_nodes[node].children.append(child)

    for tree_node in index_nodes:
        print(tree_node.value, tree_node.children)