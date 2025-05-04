#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def helper(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            down_one = cost[i - 1] + helper(i - 1)
            down_two = cost[i - 2] + helper(i - 2)
            take = min(down_one, down_two)
            memo[i] = take
            return take
        memo = {}
        return helper(len(cost))


# @lc code=end
