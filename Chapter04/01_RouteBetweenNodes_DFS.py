"""
    Given a directed graph, design an algorithm to find out whether there
    is a route between nodes.
"""

# Graph In-Memory
from collections import defaultdict

graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [3, 4]
graph[2] = [0, 4, 5]
graph[5] = [6]

visited = defaultdict(bool)

def dfs(graph, source):
    visited[source] = True
    for child in graph[source]:
        if not visited[child]:
            dfs(graph, child)

def isPath(graph, source, target):
    dfs(graph, source)
    return visited[target]

print(isPath(graph, 0, 6))
