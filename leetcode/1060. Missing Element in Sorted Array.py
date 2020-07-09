"""
Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

"""
def missing_element(nums,k):
    if not nums or k==0:
        return 0
    diff = - nums[0] + nums[-1] + 1
    missing = diff - len(nums)
    if k>missing:
        return nums[-1]+k - missing

    left,right=0,len(nums)-1
    while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
    return nums[left] + k # k should be between left and right index in the end

print(missing_element([4,7,9,10],1))