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
    if not source in graph or not target in graph:
        return False
    seen = defaultdict(bool)
    seen[source] = True
    queue = [source]
    while queue:
        source = queue.pop()
        for neighbor in graph[source]:
            if not seen[neighbor]:
                queue.append(neighbor)
                seen[neighbor] = True
    return seen[target]

if __name__ == "__main__":
    graph = create_graph(edges=10, nodes=20)
    print(find_route(1, 2, graph))
    visualise_graph(graph)
