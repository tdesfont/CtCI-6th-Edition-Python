"""
	The simplest TreeNode data-structure, not necessarily for Binary Search Tree but 
	for any Directed Acyclic Graph.
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":

    nodes = 7
    graph = {1: (2, 3), 2: (4, 5), 3: (6, 7)}

    index_nodes = [None]
    for i in range(1, nodes+1):
        index_nodes.append(BinaryTreeNode(i))

    for node in graph:
        index_nodes[node].left, index_nodes[node].right = graph[node]

    for tree_node in index_nodes[1:]:
        print(tree_node.value, tree_node.left, tree_node.right)

    print(index_nodes)