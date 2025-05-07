#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = {node: node for node in range(N + 1)}
        rank = [1] * (N + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU == rootV:
                return False  # Already connected
            if rank[rootU] < rank[rootV]:
                parent[rootU] = rootV
            elif rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
            else:
                parent[rootV] = rootU
                rank[rootU] += 1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


# @lc code=end
