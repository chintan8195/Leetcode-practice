#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First pass: left product
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Second pass: right product
        right = 1
        for i in reversed(range(n)):
            answer[i] *= right
            right *= nums[i]

        return answer


# @lc code=end
