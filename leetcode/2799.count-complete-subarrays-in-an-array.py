#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq = len(set(nums))
        mpp = defaultdict(int)
        start = 0 
        result = 0
        for end in range(len(nums)):
            mpp[nums[end]] += 1
            while mpp[nums[end]] == freq:
                result += len(nums) - start
                mpp[nums[start]] -=1
                start += 1
        return result
                
                
        
        
# @lc code=end

