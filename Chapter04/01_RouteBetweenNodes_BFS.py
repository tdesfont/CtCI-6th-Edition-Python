"""
    Given a directed graph, design an algorithm to find out whether there
    is a route between nodes.
"""

from collections import defaultdict, deque

# Build the graph
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [3, 4]
graph[2] = [0, 4, 5]
graph[5] = [6]

visited = defaultdict(bool)

def bfs(root):
    queue = deque()
    queue.append(root)
    visited[root] = True
    while queue:
        root = queue.pop()
        visited[root] = True
        for node in graph[root]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

def isPath(graph, source, target):
    bfs(source)
    return visited[target]

print(isPath(graph, 0, 6))
