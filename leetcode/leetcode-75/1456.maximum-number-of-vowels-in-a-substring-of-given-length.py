#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#


# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = 0
        start = 0
        max_vowels = float("-inf")

        for end in range(len(s)):
            if s[end] in "aeiou":
                window += 1
            if end - start + 1 == k:
                max_vowels = max(max_vowels, window)
                if s[start] in "aeiou":
                    window -= 1
                start += 1
        return max_vowels


# @lc code=end
