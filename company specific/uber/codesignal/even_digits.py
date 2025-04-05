# Given an array nums of positive integers, return how many of them contain an even number of digits.
def findNumbers(self, nums):
      
    count = 0
    for num in range(len(nums)):
        if len(str(nums[num])) % 2 == 0:
            count += 1
    
    return count