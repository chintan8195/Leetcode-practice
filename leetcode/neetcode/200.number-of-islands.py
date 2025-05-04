#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j, grid):
            if (
                len(grid) <= i
                or i < 0
                or len(grid[0]) <= j
                or j < 0
                or grid[i][j] != "1"
            ):
                return None
            grid[i][j] = "0"
            dfs(i - 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)
            dfs(i + 1, j, grid)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    num_islands += 1
        return num_islands


# @lc code=end
