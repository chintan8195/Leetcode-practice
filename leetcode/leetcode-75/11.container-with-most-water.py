#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_area = 0
        while start < end:
            area = min(height[start], height[end]) * (end-start)
            max_area = max(max_area, area)
            if height[start] < height[end]:
                start+=1
            else: 
                end-=1
        return max_area
    
# @lc code=end

