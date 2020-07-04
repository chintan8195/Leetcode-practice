'''
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
def permutations_unique(array):
    array = sorted(array)
    res =[] 
    visited = [0]*len(array)   
    dfs(array,[],visited,res)
    return res
    
def dfs(array,path,visited,res):
    if len(path) == len(array):
        res.append(path)
    for i in range(len(array)):
        if not visited[i]:
            if i>0 and visited[i-1] and array[i-1]==array[i]:
                continue
            visited[i] = 1
            dfs(array,path+[array[i]],visited,res)
            visited[i] = 0 

def test():
    assert permutations_unique([1,1,2])== [[1,1,2],[1,2,1],[2,1,1]],"Should be equal"

test()