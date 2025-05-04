#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        if fresh == 0:
            return 0
        time = -1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            time += 1
            for cells in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = 0
                for next in dirs:
                    next_row = row + next[0]
                    next_col = col + next[1]
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        q.append([next_row, next_col])
                        grid[next_row][next_col] = 2
                        fresh -= 1

        return time if fresh == 0 else -1


# @lc code=end
