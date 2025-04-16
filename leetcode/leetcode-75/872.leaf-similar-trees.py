#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, seq):
            if not node:
                return seq
            if not node.left and not node.right:
                seq.append(node.val)
                return seq
            dfs(node.left, seq)
            dfs(node.right, seq)
            return seq
        l1 = dfs(root1, [])
        l2 = dfs(root2, [])
        return l1 == l2
            
        
# @lc code=end

