#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#


# @lc code=start
from collections import deque

"""
TOPO_SORT
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        indegree = [0] * (N + 1)
        adj = {i: [] for i in range(1, N + 1)}
        for u, v in edges:
            indegree[v] += 1
            indegree[u] += 1
            adj[u].append(v)
            adj[v].append(u)
        q = deque([u for u in range(1, N + 1) if indegree[u] == 1])
        while q:
            u = q.popleft()
            for next_ in adj[u]:
                indegree[next_] -= 1
                indegree[u] -= 1
                if indegree[next_] == 1:
                    q.append(next_)

        for u, v in reversed(edges):
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]


# @lc code=end
