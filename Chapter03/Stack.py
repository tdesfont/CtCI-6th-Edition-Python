class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return self.peek() is None

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    print(stack.isEmpty())