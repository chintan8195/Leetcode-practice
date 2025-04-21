#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#


# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = 0
        start = 0
        longest_sub = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                window += 1
            while window > k:
                if nums[start] == 0:
                    window -= 1
                start += 1

            longest_sub = max(longest_sub, end - start + 1)

        return longest_sub


# @lc code=end
