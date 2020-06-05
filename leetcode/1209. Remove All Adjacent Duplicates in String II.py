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
print(remove_adjacent("deeedbbcccbdaa",3))
print(remove_adjacent(s = "pbbcggttciiippooaais", k = 2))
print(remove_adjacent("abcd",2))