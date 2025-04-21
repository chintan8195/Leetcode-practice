#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#


# @lc code=start
class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        prefix_sum = 0
        max_alt = prefix_sum
        for gain in gains:
            prefix_sum += gain
            max_alt = max(max_alt, prefix_sum)
        return max_alt


# @lc code=end
