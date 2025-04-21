#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start

from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = longest_array = 0
        map = defaultdict(int)
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == k:
                longest_array = i + 1
            if prefix_sum - k in map:
                longest_array = max(longest_array, i - map[prefix_sum - k])
            if prefix_sum not in map:
                map[prefix_sum] = i
        return longest_array
                
# @lc code=end

