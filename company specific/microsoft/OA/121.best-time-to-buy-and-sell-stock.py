#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_ = float("inf")
        for price in prices:
            if price < min_:
                min_ = price
            elif price - min_ > result:
                result = price - min_
        return result
        
# @lc code=end

