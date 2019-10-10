class Heap:
    def __init__(self, items):
        self.n = 0
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, x):
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x)
        self.rank[x] = i
        self.up(i)

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()
        if self:
            self.heap[1] = x
            self.rank[x] = 1
        return root

    def up(self, i):
        x = self.heap[i]
        while i > 1 and x < self.heap[i //2]:
            self.heap[i] = self.heap[i//2]
            self.rank[self.heap[i//2]] = i
            i //= 2
        self.heap[i] = x
        self.rank[x] = i

    def down(self, i):
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2 * i
            right = left + 1
            if right < n and self.heap[right] < self.heap[left]:
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i
                i = right
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i
                i = left
            else:
                self.heap[i] = x
                self.rank[x] = i
                return

    def update(self, old, new):
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:
            self.down(i)
        else:
            self.up(i)


if __name__ == "__main__":
    heap = Heap([10, 22, 16])
    print(heap.rank)
    heap.pop()
    print(heap.rank)
    heap.push(4)
    print(heap.rank)