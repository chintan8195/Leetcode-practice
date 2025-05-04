#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], x: int) -> Optional[TreeNode]:
        if not root:
            return None
        def get_successor(node):
            node = node.right
            while node and node.left:
                node = node.left
            return node
            # If val to be searched is in a subtree
        if root.val > x:
            root.left = self.deleteNode(root.left, x)
        elif root.val < x:
            root.right = self.deleteNode(root.right, x)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # When both children are present
            succ = get_successor(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root
# @lc code=end

