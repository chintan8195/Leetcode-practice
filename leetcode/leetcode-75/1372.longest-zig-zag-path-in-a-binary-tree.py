#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def dfs(node, left, right):
            if not node:
                return 0
            nonlocal max_length
            max_length = max(max_length, max(left, right))
            dfs(node.left, right + 1, 0)
            dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return max_length


# @lc code=end
