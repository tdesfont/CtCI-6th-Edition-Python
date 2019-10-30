from queue import deque

class BasicNode:
    def __init__(self, level):
        self.level = level
        self.isAvailable = True
        self.parent = None
    def setParent(self, node):
        self.parent = node
    def getParent(self):
        return self.parent

class CallPool:
    def __init__(self):
        self.pool = deque()
        director = BasicNode(level="Director")
        for _ in range(3):
            manager = BasicNode("Manager")
            manager.setParent(director)
            for _ in range(3):
                respondent = BasicNode("Respondent")
                respondent.setParent(manager)
                self.pool.append(respondent)

    def incomingCall(self):
        print('A call is incoming...')
        interlocutor = self.pool.pop()
        if interlocutor.isAvailable:
            interlocutor.isAvailable = False
            self.pool.appendleft(interlocutor)
            print('Respondent has been reached')
        else:
            if interlocutor.parent.isAvailable:
                print('Manager has been reached')
        # TODO: Should recursively go up in the tree to get the closer hierarchical parent
        pass

if __name__ == "__main__":
    callCenter = CallPool()
