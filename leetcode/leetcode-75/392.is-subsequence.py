#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c1 = c2 =  0

        while c1 < len(s) and c2 < len(t):
            if s[c1] == t[c2]:
                c1 += 1
            c2 += 1
        return c1 == len(s)
        
        
# @lc code=end

