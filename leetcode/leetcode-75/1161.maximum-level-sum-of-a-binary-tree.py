#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        max_sum = -float("inf")
        max_level = 0
        q = deque([root])
        
        while q:
            level += 1
            sum = 0
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                sum += node.val
                if i == level_length-1:
                    if max_sum < sum:
                        max_level = level
                        max_sum = sum                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return max_level
        

# @lc code=end

