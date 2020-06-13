import collections

def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    def helper(self,place,level,root,dic):
        if not root:
            return
        dic[place].append((level,root.val))
        self.helper(place-1,level+1,root.left,dic)
        self.helper(place+1,level+1,root.right,dic)
    dic = collections.defaultdict(list)
    helper(0,0,root,dic)
    result =[]
    for i in sorted(dic):
        temp=[]
        for j in sorted(dic[i]):
            temp.append(j[1])
        result.append(temp)
    return result
