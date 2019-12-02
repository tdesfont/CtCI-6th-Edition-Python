"""
    Implement a Circular Array class.
"""

class CircularArray:

    def __init__(self):
        self.head = 0
        self.data = []
        self.max_iter = 100

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        for item in items:
            self.data.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        self.head += 1
        self.head = self.head % len(self.data)
        return self.data[self.head]

if __name__ == "__main__":
    ca = CircularArray()
    ca.extend(list(range(10)))
    for i in range(20):
        print(next(ca))
