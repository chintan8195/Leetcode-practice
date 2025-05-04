#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for num in nums:
            if len(hp) < k:
                heapq.heappush(hp, num)
            elif num > hp[0]:
                heapq.heappushpop(hp, num)
        return hp[0]


# @lc code=end
