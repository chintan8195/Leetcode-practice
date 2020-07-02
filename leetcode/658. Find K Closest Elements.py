'''

arr = [1,2,3,4,5], k = 4, x = 3

'''
def closest(arr,k,x):
    #Base cases
    if x<0:
        return arr[:k]
    if x>len(arr):
        return arr[k:]
    # Implement Binary search
    l,r = 0,len(arr)-k
    while l<r:
        mid = (l+r)//2
    # Find the starting element, i.e l and return arr[start:start+k]
    # Condition for 1st iteration 2>5-3 = 2>2 will enter else: r = -1 return arr[0,4] 
    # We can take 3 cases as the explanation:
    # 1. arr[mid] and arr[mid+k] are both larger than x; then x-arr[mid] is negative and arr[mid+k]-x is positive, this case we should assign hi = mid.
    # 2. arr[mid] and arr[mid+k] are both less than x; then x-arr[mid] is positive and arr[mid+k]-x is negative, this case we should assign lo = mid.
    # 3. arr[mid] < x < arr[mid+k]; in this case they are both positive and we should choose the closer one.
        if x-arr[mid] > arr[mid+k]-x:
            l = mid+1
        else:
            r = mid
    return arr[l:l+k]
arr = [1,2,3,4,5]
k = 4
x = 3

print(closest(arr,k,x))