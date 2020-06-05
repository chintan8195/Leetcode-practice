'''
Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

'''
# Stack solution
def remove_adjacent(s,k):
    stack =[['#',0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1]+=1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c,1])
        print (stack)
    return ''.join(c*k for c,k in stack)
# print(remove_adjacent("deeedbbcccbdaa",3))
# print(remove_adjacent(s = "pbbcggttciiippooaais", k = 2))
# print(remove_adjacent("abcd",2))

# 2 pointer solution
def remove_adjacent_pointers(S,k):
    i,n=0,len(S)
    count = [0]*n
    res = list(S)
    for j in range(n):
        print(res,i,j,count)
        res[i]=res[j]
        if i>0 and res[i-1]==res[j]:
            count[i] = count[i-1]+1
        else:
            count[i]=1
        if count[i]==k: i-=k
        i+=1
    print(res)
    return ''.join(res[:i])

print(remove_adjacent_pointers("deeedbbcccbdaa",3))
print(remove_adjacent_pointers(S = "pbbcggttciiippooaais", k = 2))
print(remove_adjacent_pointers("abcd",2))

