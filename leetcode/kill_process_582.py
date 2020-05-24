import collections

'''
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]

'''



def killProcess(pid,ppid,kill):
    parent = {}
    
    for c, p in zip(pid, ppid):
        if p in parent:
            parent[p].append(c)
        else:
            parent[p] = [c]
    
    res = []
    q = collections.deque([kill])
    
    while q:
        for _ in range(len(q)):
            k = q.popleft()
            res.append(k)
            
            if k in parent:
                q.extend(parent[k])
            
    return res

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
result = killProcess(pid,ppid,kill)
print(result)