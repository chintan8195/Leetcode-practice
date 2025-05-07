#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#


# @lc code=start
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        """DFS
        if not rooms:
            return rooms
        wall = -1
        gate = 0
        empty_room = float("inf")
        rows = len(rooms)
        cols = len(rooms[0])

        def dfs(i, j, distance):
            if i < 0 or i >= rows or j < 0 or j >= cols or rooms[i][j] == wall:
                return

            if distance <= rooms[i][j]:
                rooms[i][j] = distance
                distance += 1
                dfs(i + 1, j, distance)
                dfs(i, j + 1, distance)
                dfs(i - 1, j, distance)
                dfs(i, j - 1, distance)

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        return rooms
        
        """

        # BFS
        if not rooms:
            return rooms
        empty_room = 2147483647
        rows = len(rooms)
        cols = len(rooms[0])
        dirs = ([0, 1], [0, -1], [-1, 0], [1, 0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append([i, j])
        while q:
            row, col = q.popleft()
            for dir in dirs:
                i = row + dir[0]
                j = col + dir[1]

                if (
                    i < 0
                    or i >= rows
                    or j < 0
                    or j >= cols
                    or rooms[i][j] != empty_room
                ):
                    continue
                rooms[i][j] = rooms[row][col] + 1
                q.append([i, j])


# @lc code=end
