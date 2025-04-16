#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1,len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            fact1, fact2 = len1 // l, len2 // l
            return str1[:l] * fact1 == str1 and str2[:l] * fact2 == str2
        
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""
# @lc code=end

