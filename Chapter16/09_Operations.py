"""
    16.9 Operations
"""

class Integer():

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Integer(self.val + other.val)

    def __ne__(self, other):
        return self.val != other.val

    def __sub__(self, other):

        mini = min(self.val, other.val)
        maxi = max(self.val, other.val)

        diff = Integer(0)

        mini = Integer(mini)
        maxi = Integer(maxi)

        while (mini + diff) != maxi:
            diff += Integer(1)
        return diff

    def __repr__(self):
        return str(self.val)

if __name__ == "__main__":
    a = Integer(19)
    b = Integer(5)
    print(a + b)
    print(a - b)