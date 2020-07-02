'''
[2.2.3.4]
[2,2,4]
[2,3,4]
[2,2,4]
'''

def valid_triangle(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)-1,1,-1):
        lo,hi=0,i-1
        while lo<=hi:
            if nums[lo]+nums[hi]> nums[i]:
                count+= hi-lo
                hi-=1
            else:
                lo+=1
    return count

nums= [2,2,3,4]
print(valid_triangle(nums))