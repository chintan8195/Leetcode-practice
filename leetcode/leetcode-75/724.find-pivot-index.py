#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#


# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = result[i - 1] + nums[i]
        right = 0
        for i in reversed(range(len(nums))):
            right += nums[i]
            result[i] -= right
            if result[i] == 0:
                return i
        return -1


# @lc code=end
