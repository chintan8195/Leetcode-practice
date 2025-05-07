#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

"""python
UNOPTIMISED:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(i, j, parent):
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= parent:
                return 0
            current = matrix[i][j]
            return (
                max(
                    dfs(i + 1, j, current),
                    dfs(i - 1, j, current),
                    dfs(i, j + 1, current),
                    dfs(i, j - 1, current),
                )
                + 1
            )

        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j, -1))
        return longest_path

"""


# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[-1] * cols for _ in range(rows)]

        def dfs(i, j, parent):
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= parent:
                return 0
            current = matrix[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            left = dfs(i + 1, j, current)
            right = dfs(i - 1, j, current)
            top = dfs(i, j + 1, current)
            bottom = dfs(i, j - 1, current)
            dp[i][j] = max(left, right, top, bottom) + 1
            return dp[i][j]

        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j, -1))
        return longest_path


# @lc code=end
