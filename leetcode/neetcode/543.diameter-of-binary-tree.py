#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal diameter
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        dfs(root)
        return diameter


# @lc code=end
