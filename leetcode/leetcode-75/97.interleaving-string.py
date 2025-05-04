#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def dfs(s1, s2, s3, i, j, k, invalid):
            if invalid[i][j] is True:
                return False
            if k == len(s3):
                return True
            valid = (
                i < len(s1) and s1[i] == s3[k] and dfs(s1, s2, s3, i+1, j, k+1, invalid)
            ) or (j < len(s2) and s2[j] == s3[k] and dfs(s1, s2, s3, i, j+1, k+1, invalid))
            if not valid:
                invalid[i][j] = True
            return valid

        c1 = list(s1)
        c2 = list(s2)
        c3 = list(s3)
        m = len(s1)
        n = len(s2)
        o = len(s3)

        if m + n != o:
            return False
        invalid = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        return dfs(c1, c2, c3, 0, 0, 0, invalid)


# @lc code=end
