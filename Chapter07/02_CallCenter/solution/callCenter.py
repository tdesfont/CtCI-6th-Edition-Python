Rank = {0:"Director", 1:"Manager", 2:"Responder"}

class CallHandler:
    def __init__(self):
        self.LEVELS = 3
        self.NUM_RESPONDENTS = 10
        self.NUM_MANAGERS = 4
        self.NUM_DIRECTORS = 2
        self.employeeLevels = ["respondents",
                               "managers",
                               "directors"]
        self.callQueues = []

    def getHandlerForCall(self, call):
        pass

    def dispatchCall(self, caller=None, call=None):
        call = Call(caller)
        self.dispatchCall(call)

    def dispatchCall(self, call):
        emp = self.getHandlerForCall(call)
        if emp:
            emp.receiveCall(call)
            call.setHandler(emp)
        else:
            call.reply("Please wait for free employee to reply")
            self.callQueues.get(call.getRank().getValue()).add(call)

    def assignCall(self, emp):
        pass

class Call:
    def __init__(self, rank, caller, handler):
        self.rank = rank
        self.caller = caller
        self.handler = handler
    def setHandler(self, e):
        self.handler = e
    def reply(self, message):
        pass
    def getRank(self):
        return self.rank
    def setRank(self, r):
        self.rank = r
    def incrementRank(self):
        pass
    def disconnect(self):
        pass

class Employee:
    def __init__(self, handler):
        self.currentCall = None
        self.rank = None
        pass
    def receiveCall(self, call):
        pass
    def callCompleted(self):
        pass
    def escalateAndReassign(self):
        pass
    def assignNewCall(self):
        pass
    def isFree(self):
        return self.currentCall == None
    def getRank(self):
        return self.rank

class Director(Employee):
    # TODO: Search inheritance in Python
    def __init__(self):
        self.rank = Rank["Director"]

class Manager(Employee):
    # TODO: Search inheritance in Python
    def __init__(self):
        self.rank = Rank["Manager"]

class Respondent(Employee):
    # TODO: Search inheritance in Python
    def __init__(self):
        self.rank = Rank["Responder"]