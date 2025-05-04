#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        connections = set((u,v) for u,v in connections)
        for u,v in connections:
            adj_list[u].add(v)
            adj_list[v].add(u)
            
        queue = deque([0])
        visited  = set([0])
        change_edges = 0
        
        while queue:
            node = queue.popleft()
            for nei in adj_list[node]:
                if nei not in visited:
                    if (node, nei) in connections:
                        change_edges += 1
                    queue.append(nei)
                    visited.add(nei)
        
        return change_edges
            
# @lc code=end

