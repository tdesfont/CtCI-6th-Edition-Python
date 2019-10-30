import numpy as np

def pprintMatrix(mat):
    string = "\n"
    for row in mat:
        string += str(row)
        string += "\n"
    print(string)

class Grid:

    def __init__(self, r, c):
        self.rows = r
        self.cols = c
        self.grid = None
        self.buildGrid()

    def buildGrid(self):
        self.grid = [[1 for i in range(self.cols)] for j in range(self.rows)]

    def markAsUnav(self, r, c):
        if (0 <= r < self.rows) and (0 <= c < self.cols):
            self.grid[r][c] = 0

def getPath(grid):
    r, c = grid.rows, grid.cols
    if not grid.grid[0][0] or not grid.grid[r-1][c-1]:
        return False
    isPath = [[0 for i in range(c)] for j in range(r)]
    isPath[0][0] = 1
    for c in range(grid.cols):
        for r in range(grid.rows):
            if c+1 < grid.cols:
                isPath[r][c+1] += 1 * (isPath[r][c] and grid.grid[r][c+1])
            if r+1 < grid.rows:
                isPath[r+1][c] += 1*(isPath[r][c] and grid.grid[r+1][c])
    pprintMatrix(isPath)
    return bool(isPath[grid.grid[-1][-1]])


if __name__ == "__main__":
    grid = Grid(8, 8)
    for i in range(20):
        grid.markAsUnav(np.random.randint(grid.rows), np.random.randint(grid.cols))
    pprintMatrix(grid.grid)
    getPath(grid)