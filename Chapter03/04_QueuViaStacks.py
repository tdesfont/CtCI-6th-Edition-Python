class Queue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, data):
        self.in_stack.append(data)

    def pop(self, data):
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()

    def isEmpty(self):
        return not (self.in_stack or self.out_stack)

    def first(self):
        if not self.isEmpty():
            if self.in_stack:
                return self.out_stack[-1]
            else:
                return self.in_stack[0]

    def last(self):
        if not self.isEmpty():
            if self.in_stack:
                return self.in_stack[-1]
            else:
                return self.out_stack[0]

if __name__ == "__main__":
    queue = Queue()
    queue.push(0)
    queue.push(1)
    queue.push(2)
    queue.pop()
    queue.push(3)
    queue.pop()
    queue.push(4)