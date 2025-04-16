#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs(root):
            nonlocal max_depth
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1
        return dfs(root)
# @lc code=end

