'''

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

'''

class TicTacToe:
    def __init__(self,n):
        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.antidiag = 0
        self.n = n

    def move(self, row,col,player):
        offset = 1 if player==1 else -1
        self.row[row] += offset
        self.col[col] += offset
        if row==col:
            self.diag += offset
        if row+col == self.n-1:
            self.antidiag+=offset
        if self.n in [self.row[row], self.col[col], self.diag, self.antidiag]:
            return 1
        if -self.n in [self.row[row], self.col[col], self.diag, self.antidiag]:
            return 2
        return 0

toe = TicTacToe(3)
print(toe.move(0,0,1))
print(toe.move(0,2,2))
print(toe.move(2,2,1))
print(toe.move(1,1,2))
print(toe.move(2,0,1))
print(toe.move(1,0,2))
print(toe.move(2,1,1))            
        