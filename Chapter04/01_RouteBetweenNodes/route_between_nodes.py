"""
    Chapter 4: Route Between Nodes
    The question is to find if there is a route between the nodes
     source and target, to answer this question we first
     use DFS or BFS but we do not have the full route at the end,
     in a second approach we will come up with a solution where
     we store the route.
"""

import networkx as nx
import pdb
import random
from collections import defaultdict
import matplotlib.pyplot as plt

def create_graph(edges, nodes, undirected=True):
    """
    Function for graph creation
    :param E:
    :param V:
    :return:
    """
    graph = defaultdict(set)
    for i in range(edges):
        n1 = random.randint(0, nodes)
        n2 = n1
        while n2 == n1:
            n2 = random.randint(0, nodes)
        graph[n1].add(n2)
        if undirected:
            graph[n2].add(n1)
    return graph

def visualise_graph(graph):
    G = nx.Graph()
    for source in graph:
        for target in graph[source]:
            G.add_edges_from([(source, target)])
    nx.draw(G, with_labels=True, node_color="red")
    plt.axis('off')
    plt.show()

def find_route(source, target, graph):
    """
    DFS to see if there is a route.
    :param source:
    :param target:
    :param graph:
    :return:
    """
    if not source in graph or not target in graph:
        return False
    seen = defaultdict(bool)
    seen[source] = True
    stack = [source]
    while stack:
        source = stack.pop()
        for neighbor in graph[source]:
            if not seen[neighbor]:
                stack.append(neighbor)
                seen[neighbor] = True
    return seen[target]

from collections import deque

def get_route(source, target, graph):
    root = source
    if not source in graph or not target in graph:
        return False
    seen = defaultdict(bool)
    seen[source] = True
    previous = {source: None}
    queue = deque([source])
    while queue:
        source = queue.pop()
        for neighbor in graph[source]:
            if not seen[neighbor]:
                seen[neighbor] = True
                queue.appendleft(neighbor)
                if neighbor not in previous:
                    previous[neighbor] = source
    if seen[target]:
        node = target
        path = [node]
        while node != root:
            node = previous[node]
            path.append(node)
        return path[::-1]
    else:
        return None

if __name__ == "__main__":
    graph = create_graph(edges=40, nodes=10)
    print(get_route(1, 2, graph))
    visualise_graph(graph)
