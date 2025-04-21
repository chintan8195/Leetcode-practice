#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#


# @lc code=start
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = y = cur = 0
        for d in differences:
            cur += d
            x = min(x, cur)
            y = max(y, cur)
            if y - x > upper - lower:
                return 0
        return (upper - lower) - (y - x) + 1


# @lc code=end
