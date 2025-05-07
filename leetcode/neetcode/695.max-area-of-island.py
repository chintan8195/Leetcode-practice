#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, area, grid) -> int:
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(i, j + 1, area, grid) + dfs(i, j - 1, area, grid) + dfs(i - 1, j, area, grid) + dfs(i + 1, j, area, grid)

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j, 0, grid)
                    max_area = max(max_area, area)
        return max_area


# @lc code=end
