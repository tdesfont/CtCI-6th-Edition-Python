"""
    Chapter 8: Recursion and Dynamic Programming
    Question 2: Robot in Grid
"""

import random

class Grid:

    def __init__(self, r, c):
        self.rows = r
        self.cols = c
        self.grid = [["|_|" for i in range(self.cols)]
                     for j in range(self.rows)]
        self.annot = "|X|"

    def isValidPosition(self, i, j):
        if (0<=i<self.rows) and (0<=j<self.cols):
            return True
        else:
            return False

    def mark(self, i, j):
        if not self.isValidPosition(i, j):
            return False
        self.grid[i][j] = self.annot
        return True

    def isAvailable(self, i, j):
        if not self.isValidPosition(i, j):
            return False
        return self.grid[i][j] != self.annot

    def __repr__(self):
        string = "\n"
        for row in self.grid:
            string += "".join([str(i) for i in row])+"\n"
        string += "\n"
        return string

def get_paths(grid):
    r = grid.rows
    c = grid.cols
    if not grid.isAvailable(0, 0):
        return False
    if not grid.isAvailable(r-1, c-1):
        return False
    A = [[False for i in range(c)] for j in range(r)]
    A[0][0] = True
    for i in range(r):
        for j in range(c):
            A[i][j] = (grid.isAvailable(i-1, j) or grid.isAvailable(i, j-1))
    print(A)
    return A[i][j]

if __name__ == "__main__":
    grid = Grid(5, 4)
    r = grid.rows
    c = grid.cols
    for i in range(10):
        sample_pos = (random.randint(0, r), random.randint(0, c))
        grid.mark(*sample_pos)
    print(grid)
    is_path = get_paths(grid)
    print(is_path)