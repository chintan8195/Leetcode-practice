#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        map = defaultdict(int)

        def subarray_sum(node, pre_sum):
            if not node:
                return
            nonlocal result
            pre_sum += node.val
            if pre_sum == targetSum:
                result += 1
            result += map[pre_sum - targetSum]
            map[pre_sum] += 1
            subarray_sum(node.left, pre_sum)
            subarray_sum(node.right, pre_sum)
            map[pre_sum] -= 1

        subarray_sum(root, 0)
        return result


# @lc code=end
