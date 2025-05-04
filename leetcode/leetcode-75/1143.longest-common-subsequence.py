#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Properly create an (m+1) x (n+1) DP table of zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[m][n]


# @lc code=end
