"""
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

# Solve using template from https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problemsa

def longestSubstring(s, k):
    count = 0
    for i in range(1, 27):
        count = max(count, helper(s, k, i))
    return count

def helper(s, k, numUniqueTarget):
    start = end = numUnique = numNoLessThanK = count = 0
    chMap = [0]*128

    while end < len(s):
        if chMap[ord(s[end])] == 0: numUnique += 1
        chMap[ord(s[end])] += 1
        if chMap[ord(s[end])] == k: numNoLessThanK += 1
        end += 1
        
        while numUnique > numUniqueTarget:
            if chMap[ord(s[start])] == k: numNoLessThanK -= 1
            chMap[ord(s[start])] -= 1
            if chMap[ord(s[start])] == 0: numUnique -= 1
            start += 1
            
        if numUnique == numNoLessThanK: count = max(count, end-start)
        
    return count

def test():
    assert longestSubstring("ababbc",2) == 5,"should be equal to 5"
    assert longestSubstring("aaabb",3) == 3, "should be equal to 5"

test()

        
        
    