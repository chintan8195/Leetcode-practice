# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6

'''
["0000"]
[]
'''
import collections 
def avoid_deadends(deadends,target):
    q = collections.deque([("0000",0)])
    visited = set(deadends)
    
    while q:
        size = len(q)
        for i in range(size):
            comb, depth = q.popleft()
            if comb in visited:
                continue 
            if comb==target:
                return depth
            visited.add(comb)
            values = neighbors(comb)
            for neighbor in values:
                if neighbor not in visited:
                    q.append((neighbor,depth+1))
    return -1

def neighbors(node):
    res = []
    for i,c in enumerate(node):
        num = int(c)
        res.append(node[:i]+str((num-1)%10)+node[i+1:])
        res.append(node[:i]+str((num+1)%10)+node[i+1:])
    return res
    
def test():
    assert avoid_deadends(["0201","0101","0102","1212","2002"],"0202") == 6,"Answer should be 6 instead got" + print(avoid_deadends(["0201","0101","0102","1212","2002"],"0202"))

test()
