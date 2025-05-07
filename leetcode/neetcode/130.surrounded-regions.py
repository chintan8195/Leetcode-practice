#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if board[i][j] != "O":
                return
            board[i][j] = "L"
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        for i in range(cols):
            if board[0][i] == "O":
                dfs(0, i)
            if board[rows - 1][i] == "O":
                dfs(rows - 1, i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "L":
                    board[i][j] = "O"


# @lc code=end
