'''
Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
'''

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    def dfs(curr,path):
        if curr==len(graph)-1:
            res.append(path)
        else:
            for i in graph[curr]:
                dfs(i,path+[i]) 
    res=[]
    dfs(0,[0])
    return res