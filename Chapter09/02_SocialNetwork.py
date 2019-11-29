"""
    Implement a Bidirectional Breadth First-Search
"""

class SocialNetwork:

    def __init__(self):
        self.graph = {}

    def add_link(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        else:
            self.graph[a].append(b)

    def connect(self, a, b):
        self.add_link(a, b)
        self.add_link(b, a)

def findPathBiBFS(people, source, destination):
    sourceData = BFSData(people.source)
    destData = BFSData(people.destination)
    while not sourceData.isFinished and not destData.isFinished:
        # Search out from source
        collision = searchLevel(people, sourceData, destData)
        if collision:
            return mergePaths(sourceData, destData, collision.id)
        collision = searchLevel(people, destData, sourceData)
        if collision:
            return mergePaths(sourceData, destData, collision.id)
    return None

def searchLevel(people, primary, secondary):
    count = lenght(primary.toVisit())
    for i in range(count):
        pathNode = primary.toVisit().poll()
        personID = pathNode.getPerson().getID()
        if secondary.visited.containsKey(personID):
            return pathNode.getPerson()
        person = pathNode.getPerson()
        friends = person.getFriends()
        for friendId in friends:
            if not friendId in primary.visited:
                friend = people.get(friendId)
                next = PathNode(friend, pathNode)
                primary.visited.put(friendId, next)
                primary.toVisit.add(next)

    return None

def mergePaths(bfs1, bfs2, connection):
    end1 = bfs1.visited.get(connection)
    end2 = bfs2.visited.get(connection)
    pathOne = end1.collapse(False)
    pathTwo = end2.collapse(True)
    pathTwo.removeFirst()
    pathOne.addAll(pathTwo)
    return pathOne

class PathNode:
    def __init__(self, p, previous):
        self.person = p
        self.previousNode = previous
    def getPerson(self):
        return self.person
    def collapse(self, startsWithRoot):
        path = Person()


if __name__ == "__main__":
    graph = SocialNe
    links = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (4, 5), (5, 6), (5, 7), (6, 7)]
    for link in links:
        graph.connect(link)