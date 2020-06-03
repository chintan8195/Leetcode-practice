'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

def searchRange(nums, target):
    left = searchLeft(nums,target)
    right = searchRight(nums,target)
    return [left,right] if left<=right else [-1,-1]
    
def searchLeft(nums,target):
    lo,hi = 0,len(nums)-1
    while lo<=hi:
        mid = lo+(hi-lo)//2
        if target>nums[mid]:
            lo=mid+1
        else:
            hi=mid-1
    return lo

def searchRight(nums,target):
    lo,hi=0,len(nums)-1
    while lo<=hi:
        mid = lo+(hi-lo)//2
        if target<nums[mid]:
            hi=mid-1
        else:
            lo=mid+1
    return hi

nums = [5,7,7,8,8,10]
target = 6
result = searchRange(nums,target)
print(result)
