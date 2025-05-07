#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


# @lc code=start
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS

        # 1. Build adjacency list: edge b → a for [a, b]
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        # 2. State array for cycle detection: 0=unvisited, 1=visiting, 2=visited
        state = [0] * numCourses
        stack = []

        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            state[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            state[course] = 2
            stack.append(course)
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []
        return stack
        """
        """
            Return a topological ordering of courses given prerequisites,
            or [] if no such ordering exists (i.e., there is a cycle),
            using Kahn's Algorithm.
        """
        # 1. Build adjacency list and in-degree array

        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 2. Initialize queue with all courses having in-degree 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        topo_order: List[int] = []

        # 3. Process until queue is empty
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            # “Remove” edges u → v
            for v in graph[u]:
                indegree[v] -= 1
                # When a node’s in-degree drops to zero, enqueue it
                if indegree[v] == 0:
                    queue.append(v)

        # 4. If we scheduled all courses, return order; else there was a cycle
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []


# @lc code=end
