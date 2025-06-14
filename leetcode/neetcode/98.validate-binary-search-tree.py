#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.left:
                if curr.val <= curr.left.val:
                    return False
                else:
                    q.append(curr.left)
            if curr.right:
                if curr.val >= curr.right.val:
                    return False
                else:
                    q.append(curr.right)
        return True


# @lc code=end
