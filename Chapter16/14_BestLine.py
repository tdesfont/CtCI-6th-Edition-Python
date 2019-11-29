"""
    16.14 Best Line Ransac
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

x = np.linspace(-10, 10, 10)
y = x

N = 100
X = np.random.random(N)*20 - 10
Y = np.random.random(N)*20 - 10

plt.figure(figsize=(15, 5))
plt.scatter(x, y, edgecolor="k", c="r")
plt.scatter(X, Y, edgecolor="k")
plt.grid()
plt.show()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector:

    def __init__(self, origin, end):
        x1, y1 = end.x, end.y
        x2, y2 = origin.x, origin.y
        norm = sqrt((x1-x2)**2+(y1-y2)**2)
        if norm == 0:
            raise Exception
        self.x = (x2-x1)/norm
        self.y = (y2-y1)/norm
        if self.x < 0:
            self.x *= -1
            self.y *= -1

    def isColinear(self, vector):
        return self.x * vector.y == self.y * vector.x

from collections import deque
from collections import defaultdict

def bestLine(X, Y):
    """
        Find the line that pass by the greatest number of points.
    :param X: x-coordinates of points (a list or an array)
    :param Y: y-coordinates of points (a list or an array)
    :return:
    """
    # Build the stack of points
    stack = deque()
    for x, y in zip(X, Y):
        stack.append(Point(x, y))
    # Do the RANSAC
    hash = defaultdict(list)
    while stack:
        source = stack.pop()
        for target in stack:
            unitVec = Vector(source, target)
            hash[(unitVec.x, unitVec.y)].append(target)

    for key in hash:
        if len(hash[key]) != 1:
            print('Set of points:')
            for point in hash[key]:
                print(point.x, point.y)

if __name__ == "__main__":
    bestLine(list(X)+list(x), list(Y)+list(y))
