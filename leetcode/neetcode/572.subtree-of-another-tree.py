#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def find(p):
            if not p:
                return False
            elif isSameTree(p, subRoot):
                return True
            return find(p.left) or find(p.right)

        def isSameTree(p, q):
            if not q and not p:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        return find(root)


# @lc code=end
