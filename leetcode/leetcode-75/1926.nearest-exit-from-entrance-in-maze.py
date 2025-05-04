#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        q = deque()
        q.append([start_row, start_col, 0])
        while q:
            curr_row, curr_col, curr_distance = q.popleft()
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                # If there exists an unvisited empty neighbor:
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and maze[next_row][next_col] == "."
                ):

                    # If this empty cell is an exit, return distance + 1.
                    if (
                        0 == next_row
                        or next_row == rows - 1
                        or 0 == next_col
                        or next_col == cols - 1
                    ):
                        return curr_distance + 1

                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = "+"
                    q.append([next_row, next_col, curr_distance + 1])

        # If we finish iterating without finding an exit, return -1.
        return -1


# @lc code=end
