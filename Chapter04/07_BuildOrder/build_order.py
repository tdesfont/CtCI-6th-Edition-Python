"""
    Chapter 4: Trees and Graph
    Question 7: Build Order
"""

from collections import defaultdict

def build_order(projects, dependencies):
    graph = {}
    for p in projects:
        graph[p] = []
    for source, target in dependencies:
        graph[target].append(source)
    return graph

def incoming_nodes(graph):
    counter = defaultdict(int)
    for source in graph:
        for target in graph[source]:
            counter[target] += 1
    end_nodes = set()
    for source in graph:
        if source not in counter:
            end_nodes.add(source)
    return end_nodes

def dfs_iter(source, graph):
    seen = defaultdict(bool)
    seen[source] = True
    stack = [source]
    path = []
    while stack:
        node = stack.pop()
        path.append(node)
        seen[node] = True
        for neighbor in graph[node]:
            if not seen[neighbor]:
                stack.append(neighbor)
                seen[neighbor] = True
    return path

def dfs_alter(source, graph, seen=None):
    """
    This a dfs algorithm with just a modification on the common
    seen list.
    :param source:
    :param graph:
    :param seen:
    :return:
    """
    if not seen:
        seen = defaultdict(bool)
    seen[source] = True
    stack = [source]
    path = []
    while stack:
        node = stack.pop()
        path.append(node)
        seen[node] = True
        for neighbor in graph[node]:
            if not seen[neighbor]:
                stack.append(neighbor)
                seen[neighbor] = True
    return path, seen

def get_build_order(projects, dependencies):
    graph = build_order(projects, dependencies)
    starting_nodes = incoming_nodes(graph)
    if not starting_nodes:
        return False
    path = []
    seen = None
    for node in starting_nodes:
        single_path, seen = dfs_alter(node, graph, seen)
        for tmp_node in single_path[::-1]:
            path.append(tmp_node)
    return path[::-1]

if __name__ == "__main__":
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("d","a"),("b","f"),("d","b"),("a","f"),("c","d"), ("a", "e")]
    print(get_build_order(projects, dependencies))
