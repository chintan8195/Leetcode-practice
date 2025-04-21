#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#


# @lc code=start
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU == rootV:
                return 0  # Already connected
            if rank[rootU] < rank[rootV]:
                parent[rootU] = rootV
            elif rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
            else:
                parent[rootV] = rootU
                rank[rootU] += 1
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1,n2)        

        return result

# @lc code=end
