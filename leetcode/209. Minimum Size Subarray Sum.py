'''
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2

2,3,1,2,4,3
| |
2
'''
def subarray_sum(s ,nums):
    if not len(nums):
        return 0
    i,j = 0,0
    minimum_len = float("inf")
    sub_sum = 0
    while j<len(nums):
        sub_sum += nums[j]
        j+=1
        while sub_sum >= s:
            minimum_len = min(minimum_len,j-i)
            sub_sum -= nums[i]
            i+=1
    return 0 if minimum_len == float("inf") else minimum_len

nums = [2,3,1,2,4,3]
print(subarray_sum(7, nums))

nums = [1,1]
print(subarray_sum(3,nums))