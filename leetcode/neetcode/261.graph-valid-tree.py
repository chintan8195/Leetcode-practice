#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#


# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        1. Exactly n–1 edges (a tree with n nodes must have n–1 edges).
        2. No cycles and fully connected.
        """
        if len(edges) != n - 1:
            return False
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for v in graph[node]:
                if v == parent:
                    continue

                if v in visited:
                    return False
                if not dfs(v, node):
                    return False
            return True

        # 3. Run DFS from node 0
        if not dfs(0, -1):
            return False

        # 4. Ensure all nodes are connected
        return len(visited) == n


# @lc code=end
