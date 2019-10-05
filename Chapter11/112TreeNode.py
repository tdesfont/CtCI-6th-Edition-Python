"""
	The simplest TreeNode data-structure, not necessarily for Binary Search Tree but 
	for any Directed Acyclic Graph.
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