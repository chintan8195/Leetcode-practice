#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s)-1
        vowels= ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        while start<end:
            if s[start].lower() not in vowels:
                start+=1
            if s[end].lower() not in vowels:
                end -=1
            if s[start].lower() in vowels and s[end].lower() in vowels:
                s[start], s[end] = s[end], s[start]
                start +=1
                end -=1
        return "".join(s)
# @lc code=end

