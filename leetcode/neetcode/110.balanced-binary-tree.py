#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        if not root:
            return True
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# @lc code=end
