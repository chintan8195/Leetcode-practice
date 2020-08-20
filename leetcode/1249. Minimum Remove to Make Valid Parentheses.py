def minRemoveToMakeValid(self, s: str):
    if not s:
        return ""
    i = 0
    stack = []
    res = []
    index = set()
    while i<len(s):
        if s[i]=='(':
            stack.append(i)
        elif s[i]==')':
            if stack:
                stack.pop()
            else:
                index.add(i)
        i+=1
    if stack:
        index = index.union(set(stack))
    for i,c in enumerate(s):
        if i not in index:
            res.append(c)
            
    return ''.join(res)