#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rotten = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.append([i, j])
        time = -1
        dirs = ([0, 1], [0, -1], [-1, 0], [1, 0])

        if fresh == 0:
            return 0
        while rotten:
            time += 1
            level = len(rotten)
            for _l in range(level):
                row, col = rotten.popleft()
                for dir in dirs:
                    i = row + dir[0]
                    j = col + dir[1]

                    if (
                        i < 0
                        or i >= len(grid)
                        or j < 0
                        or j >= len(grid[0])
                        or grid[i][j] != 1
                    ):
                        continue
                    rotten.append([i, j])
                    grid[i][j] = 2
                    fresh -= 1 

        return time if fresh == 0 else -1


# @lc code=end
