'''
Input: [3,4,5,1,2] 
Output: 1

Input: [4,5,6,7,0,1,2]
Output: 0

Input: [0,1,2,3,4,5]

func(arr):
    lo,hi = 0, len(arr)
    m = inf
    while lo<=hi:
        mid = lo+hi/2
        m = min(m,mid)
        if lo<mid:
            if mid>hi:
                lo = mid+1
            else:
                hi = mid-1
        else:
            if hi>mid:
                hi = mid-1
            else:
                lo = mid+1
    return m    
'''

def find_min( arr):
    if not arr:
        return 0
    lo,hi = 0,len(arr)-1
    minimum = float("inf")
    while lo<=hi:
        mid = (lo + hi)//2
        if arr[mid]<arr[mid-1]:
            return arr[mid]
        if arr[mid]>arr[mid+1]:
            return arr[mid+1]   
        if arr[mid]>arr[0]:
            lo = mid+1
        else:
            hi = mid-1

print(find_min([3,4,5,1,2]))
print(find_min([4,5,6,7,0,1,2]))
print(find_min([1,2,3,4,0]))