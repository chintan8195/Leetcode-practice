#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#


# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window from k to the end of the list
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        # Maximum average
        return max_sum / k


# @lc code=end
