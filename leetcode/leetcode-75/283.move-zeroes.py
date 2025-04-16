#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_ = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr_] = nums[i]
                curr_ += 1
        nums[curr_:len(nums)] = [0] * (len(nums)-curr_)
        return nums


        
# @lc code=end

