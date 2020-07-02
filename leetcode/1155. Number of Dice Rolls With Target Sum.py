def numRollsToTarget(d: int, f: int, target: int) -> int:
    hm = {}
    def dp(d, target):
        if d==0:
            return 0 if target>0 else 1
        if (d,target) in hm:
            return hm[(d,target)]
        to_return  = 0
        for k in range(max(0,target-f),target):
            to_return += dp(d-1,k)
        hm[(d,target)] = to_return
        return to_return
    return dp(d,target)%((10**9)+7)
    

d = 1
f = 6
target = 3
print(numRollsToTarget(d,f,target))

d = 2 
f = 6 
target = 7
print(numRollsToTarget(d,f,target))

d = 2 
f = 5 
target = 10
print(numRollsToTarget(d,f,target))

d = 30 
f = 30 
target = 500
print(numRollsToTarget(d,f,target))
