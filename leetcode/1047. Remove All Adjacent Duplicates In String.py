'''
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
'''
def remove_adjacent(S):
    stack = []
    for s in S:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)

#print(remove_adjacent("abbaca"))

# 2 pointer approach

def remove_adjacent_pointers(S):        
    i,n=0,len(S)
    res = list(S)
    for j in range(n):
        print(res,i,j)
        res[i]=res[j]
        if i>0 and res[i-1]==res[j]:
            i-=2
        i+=1
    return ''.join(res[:i])

print(remove_adjacent_pointers("abbaca"))

#  public String removeDuplicates(String s) {
#         int i = 0, n = s.length();
#         char[] res = s.toCharArray();
#         for (int j = 0; j < n; ++j, ++i) {
#             res[i] = res[j];
#             if (i > 0 && res[i - 1] == res[i]) // count = 2
#                 i -= 2;
#         }
#         return new String(res, 0, i);
#     }

