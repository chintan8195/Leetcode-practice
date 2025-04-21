#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#


# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = 0
        start = 0
        longest_sub = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                window += 1
            while window > 1:
                if nums[start] == 0:
                    window -= 1
                start += 1

            longest_sub = max(longest_sub, end - start)

        return longest_sub


# @lc code=end
