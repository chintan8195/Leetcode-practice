#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
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
                return 0
            if rank[rootU] < rank[rootV]:
                parent[rootU] = rootV
            elif rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
            else:
                parent[rootV] = rootU
                rank[rootU] += 1
            return 1

        result = n
        for i in range(n):
            for j in range(n):
                if find(i) != find(j) and isConnected[i][j] == 1:
                    result -= union(i, j)

        return result


# @lc code=end
