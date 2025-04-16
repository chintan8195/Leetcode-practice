#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        c1 = 0
        while c1<max(len(word1), len(word2)):
            if c1<len(word1):
                result.append(word1[c1])
            if c1<len(word2):
                result.append(word2[c1])
            c1+=1
        return ''.join(result)
            


        
# @lc code=end

