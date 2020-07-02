def subsets(nums):
    res = []
    dfs(sorted(nums),res,[],0)
    return res

def dfs(arr,res,path,index):
    res.append(path)
    for i in range(index,len(arr)):
        dfs(arr,res,path+[arr[i]],i+1)

print(subsets([1,2,3]))