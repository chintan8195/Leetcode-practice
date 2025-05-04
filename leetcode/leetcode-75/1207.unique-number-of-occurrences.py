#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
        occ = set()
        for value in freq.values():
            if value in occ:
                return False
            occ.add(value)
        return True


# @lc code=end
