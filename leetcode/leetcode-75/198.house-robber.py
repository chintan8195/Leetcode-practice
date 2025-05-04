#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
"""
[1,2,3,1]
= 

"""
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        def rob_helper(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[0]
            nonlocal memo
            if i in memo:
                return memo[i]
            skip = rob_helper(i - 1)
            take = rob_helper(i - 2) + nums[i - 1]
            result = max(skip, take)

            # store result in memo before returning 
            memo[i] = result
            return result 
        return rob_helper(len(nums))
            
# @lc code=end

