# Backtracking DFS

def generate_parantheses(n):
    res = []
    dfs(n,n,"",res)
    return res

def dfs(leftRemain,rightRemain,path,res):
    if  leftRemain > rightRemain or leftRemain<0 or rightRemain<0:
        return 
    if not leftRemain and not rightRemain:
        res.append(path)
    dfs(leftRemain-1,rightRemain,path+'(',res)
    dfs(leftRemain,rightRemain-1,path+')',res)

# print(generate_parantheses(3))
