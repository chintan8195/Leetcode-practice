#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
            
        node = root
        while node and node.val != val:
            if not node:
                return None
            if node.val > val:
                node = node.left
            else:
                node = node.right
            
        return node
                
                
# @lc code=end

