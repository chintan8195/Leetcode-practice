#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = 0
        two = len(nums) - 1
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 2:
                nums[two], nums[one] = nums[one], nums[two]
                two -= 1
            else:
                one += 1


# @lc code=end
