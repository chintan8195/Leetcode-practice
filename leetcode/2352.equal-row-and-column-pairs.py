#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0 
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_count[tuple(col)]
        return count
        
# @lc code=end

