#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

"""
{abc}{abc}{b}{b}

keep track of frequency in a particular window.
abc

set = ()



"""
from math import inf


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        window = {}
        max_ = 0
        for end in range(len(s)):
            if s[end] in window:
                start = max(start, window.get(s[end]) + 1) 

            window[s[end]] = end
            max_ = max(max_, end-start+1)
        return max_
# @lc code=end

