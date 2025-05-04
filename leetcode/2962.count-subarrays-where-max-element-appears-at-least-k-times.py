#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        result = 0
        max_num = max(nums)
        max_count = 0

        for end in range(len(nums)):
            if nums[end] == max_num:
                max_count += 1
            while max_count >= k:
                result += len(nums) - end
                if nums[start] == max_num:
                    max_count -= 1
                start += 1
        return result


"""
[1,3,2,3,3]

start = 0
result = 0
max_num = 3
max_count = 0

3

"""

# @lc code=end
