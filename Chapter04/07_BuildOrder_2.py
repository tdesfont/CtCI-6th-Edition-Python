"""
    Exercise 4.7 Build Order
"""

from collections import defaultdict

projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("d", "a"), ("b", "f"), ("d", "b"), ("a", "f"), ("c", "d")]

visited = [False for p in projects]

graph = defaultdict(list)

for vertex in dependencies:
    graph[vertex[0]].append(vertex[1])

nbr_incoming_edges = defaultdict(int)
for vertex in dependencies:
    nbr_incoming_edges[vertex[0]] += 1

c = [(k, v) for k, v in zip(nbr_incoming_edges.keys(), nbr_incoming_edges.values())]
c.sort()