#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#


# @lc code=start
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)
        if frequency_word1.keys() != frequency_word2.keys():
            return False
        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())

        return sorted_values_word1 == sorted_values_word2 and (
            frequency_word1.keys != frequency_word2.keys
        )


# @lc code=end
