#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        visited = set()

        q.append(0)
        visited.add(0)
        while q:
            other_keys = q.pop()
            for key in rooms[other_keys]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return len(visited) == len(rooms)


# @lc code=end
