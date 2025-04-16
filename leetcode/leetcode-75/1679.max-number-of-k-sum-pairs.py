#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start, end =0 , len(nums)-1
        nums = sorted(nums)
        result = 0
        while start<end:
            if nums[start] + nums[end] == k:
                result+=1
                start +=1
                end-=1
            elif nums[start] + nums[end] > k:
                end-=1
            else:
                start += 1
                
        return result
        
# @lc code=end

