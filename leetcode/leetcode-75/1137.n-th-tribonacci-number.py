#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = helper(i-1) + helper(i-2) + helper(i-3)
            return memo[i]
        memo = {}
        return helper(n)
        
        
# @lc code=end

