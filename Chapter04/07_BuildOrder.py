"""
    Exercise 4.7 Build Order

        - Valid if we have one root project and its dependencies
        - Not valid if we several connected components
"""
from collections import defaultdict

class Project:
    def __init__(self, name):
        self.name = name
        self.dependencies = []
    def add_dependencies(self, project):
        self.dependencies.append(project)

a = Project("a")
b = Project("b")
c = Project("c")
d = Project("d")
e = Project("e")
f = Project("f")

a.add_dependencies(b)
a.add_dependencies(c)
b.add_dependencies(d)
d.add_dependencies(e)
c.add_dependencies(f)

root = a

visited = defaultdict(bool)
topological_order = []

def dfs(root):
    visited[root] = True
    for child in root.dependencies:
        if not visited[child]:
            dfs(child)
    topological_order.append(root)

dfs(root)

print([p.name for p in topological_order])