'''
Given a 2D integer array board representing the grid of candy,
different positive integers board[i][j] represent different types of candies. 
A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. 
The given board represents the state of the game following the player's move. 
Now, you need to restore the board to a stable state by crushing candies according to the following rules:

1. If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - 
   these positions become empty.
2. After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, 
    then these candies will drop until they hit a candy or bottom at the same time.
    (No new candies will drop outside the top boundary.)
3. After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
4. If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.

You need to perform the above rules until the board becomes stable, then return the current board.

 

Input:
board =
[
 [110, 5,112,113,114],
 [210,211,5,213,214],
 [310,311,3,313,314],
 [410,411,412,5,414],
 [5,   1, 512, 3, 3],
 [610, 4, 1,613,614],
 [710, 1, 2,713,714],
 [810, 1 ,2, 1,  1],
 [1,   1, 2, 2,  2],
 [4,   1, 4, 4,1014]]
  
Output:
[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[110,0,0,0,114],
[210,0,0,0,214],
[310,0,0,113,314],
[410,0,0,213,414],
[610,211,112,313,614],
[710,311,412,613,714],
[810,411,512,713,1014]]
'''

def candyCrush(board):
    m,n = len(board),len(board[0])

    def crush():
        crush = False
        for i in range(m):
            for j in range(n):
                if j>1 and board[i][j]>0 and board[i][j] == abs(board[i][j-1]) == abs(board[i][j-2]):
                    board[i][j-2:j+1] = [-abs(board[i][j]) for _ in range(3)]
                    crush = True
                if i>1 and board[i][j]>0 and board[i][j] == abs(board[i-1][j]) == abs(board[i-2][j]):
                    if board[i][j] > 0:
                        board[i][j]*=-1
                    if board[i-1][j] > 0:
                        board[i-1][j]*=-1
                    if board[i-2][j] > 0:
                        board[i-2][j]*=-1
                    crush = True
                return crush
    
    def gravity():
        for j in range(n):
            stack = [board[i][j] for i in range(m-1,-1,-1) if board[i][j] >0]
            stack += [0]*(m-len(stack))
            for i in range(m):
                board[i][j] = stack.pop()
                    
    
    while crush(): gravity()
    return board

print(candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))