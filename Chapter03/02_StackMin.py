class StackMin:

    def __init__(self):
        self.stack = []
        self.rolling_min = []

    def isEmpty(self):
        return bool(self.stack)

    def push(self, data):
        if self.isEmpty():
            currentMin = float('inf')
        else:
            currentMin = self.rolling_min[-1]
        self.stack.append(data)
        if data < currentMin:
            self.rolling_min.append(data)
        else:
            self.rolling_min.append(currentMin)

    def pop(self):
        if not self.isEmpty():
            self.rolling_min.pop()
            return self.stack.pop()

    def min(self):
        if not self.isEmpty():
            return self.rolling_min[-1]

if __name__ == "__main__":
    stack = StackMin()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.min()
    stack.push(-6)
    stack.min()
    stack.pop()
    stack.min()