#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, max_value):
            if not node:
                return
            max_value = max(max_value, node.val)
            dfs(node.left, max_value)
            dfs(node.right, max_value)
            nonlocal count
            if node.val >= max_value:
                count += 1
                return True
            return False

        dfs(root, -float("inf"))
        return count


# @lc code=end
