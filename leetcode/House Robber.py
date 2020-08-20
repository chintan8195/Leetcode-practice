'''
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

[1,2,3,1]
[1,2,4,4]


Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
[2,7,9,3,1]
[2,7,11,11,12]
'''
def robbery(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    return dp.pop()

print(robbery([2,7,5]))