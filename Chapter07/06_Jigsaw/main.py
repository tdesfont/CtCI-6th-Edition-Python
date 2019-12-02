"""
    Implement the Jigsaw game.
"""
import random

class Board:

    def __init__(self):
        self.board = list(range(9))
        self.board[-1] = "X"
        self.empty_pos = (2, 2)
        print("Create an empty board")
        print(self)

    def __repr__(self):
        string = ""
        line = " ______"
        for i in range(3):
            string += line+"\n"
            string += "|{}|{}|{}|".format(*self.board[i*3:(i+1)*3])+"\n"
        string += line +"\n"
        return string

    def get_pos(self, i):
        return (i//3, i%3)

    def get_index(self, pos):
        return pos[0]*3+pos[1]

    def is_valid_swap(self, tuple1, tuple2):
        dx, dy = abs(tuple1[0]-tuple2[0]), abs(tuple1[1]-tuple2[1])
        dx, dy = sorted([dx, dy])
        return dx == 0 and dy == 1

    def is_valid_pos(self, tuple):
        return 0<=tuple[0]<3 and 0<=tuple[1]<3

    def swap(self, i, j):
        if not (self.board[i] == "X" or self.board[j] == "X"):
            print("Trying to swap non empty tiles")
            return False
        if not 0<=i<9 or not 0<=j<9:
            print('Invalid swap')
            return False
        t1, t2 = self.get_pos(i), self.get_pos(j)
        if not self.is_valid_swap(t1, t2):
            print("Invalid swap")
            return False
        self.board[i], self.board[j] = self.board[j], self.board[i]

    def get_swap_empty_index(self):
        # find empty position
        index_empty = 0
        while self.board[index_empty] != "X":
            index_empty += 1
        pos_empty = self.get_pos(index_empty)
        pos = []
        for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
            potential_pos = (pos_empty[0]+i, pos_empty[1]+j)
            if self.is_valid_pos(potential_pos):
                pos.append(potential_pos)
        return [self.get_index(p) for p in pos]

    def get_empty_index(self):
        index = random.randint(0, 8)
        while self.board[index] != "X":
            index += 1
            index = index % 9
        return index

if __name__ == "__main__":
    board = Board()
    for i in range(100000):
        empty_index = board.get_empty_index()
        moves = board.get_swap_empty_index()
        index_move = random.randint(0, len(moves)-1)
        board.swap(empty_index, moves[index_move])
        print(board)