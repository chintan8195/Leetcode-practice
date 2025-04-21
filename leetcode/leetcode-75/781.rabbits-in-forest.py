#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#


# @lc code=start
from collections import defaultdict


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        map = defaultdict(int)
        result = 0
        for count in answers:
            if count == 0:
                result += 1
            elif count not in map:
                map[count] = count
                result += count + 1
            else:
                map[count] -= 1
                if map[count] == 0:
                    del map[count]
        return result


# @lc code=end
