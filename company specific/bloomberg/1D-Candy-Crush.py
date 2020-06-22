'''
Write a function to crush candy in one dimensional board.
In candy crushing games, groups of like items are removed from the board. 
In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. 
This process should be repeated as many time as possible. You should greedily remove characters from left to right.

Example 1:

Input: "aaabbbc"
Output: "c"
Explanation:
1. Remove 3 'a': "aaabbbc" => "bbbc"
2. Remove 3 'b': "bbbc" => "c"
Example 2:

Input: "aabbbacd"
Output: "cd"
Explanation:
1. Remove 3 'b': "aabbbacd" => "aaacd"
2. Remove 3 'a': "aaacd" => "cd"
Example 3:

Input: "aabbccddeeedcba"
Output: ""
Explanation:
1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
3. Remove 3 'c': "aabbcccba" => "aabbba"
4. Remove 3 'b': "aabbba" => "aaa"
5. Remove 3 'a': "aaa" => ""

Example 4:

Input: "aaabbbacd"
Output: "acd"
Explanation:
1. Remove 3 'a': "aaabbbacd" => "bbbacd"
2. Remove 3 'b': "bbbacd" => "acd"
I solved it with recursion and also discussed the stack based approach.

Follow-up:
What if you need to find the shortest string after removal?

Example:

Input: "aaabbbacd"
Output: "cd"
Explanation:
1. Remove 3 'b': "aaabbbacd" => "aaaacd"
2. Remove 4 'a': "aaaacd" => "cd"

aabbbbaabbcd => 
'''

def candy_crush(s):
    stack = [['#',0]]
    for i in range(len(s)):
        print(stack,s[i])
        if stack[-1][0] ==s[i]:
            stack[-1][1]+=1
        else:
            if stack[-1][1]>=3:
                stack.pop()
            if stack and stack[-1][0]!=s[i]:
                stack.append([s[i],1])
    if stack[-1][1]>=3:
        stack.pop()
    result = ''.join(c*k for c,k in stack)
    print(result)
    return result

if __name__ == "__main__":
    assert candy_crush("aaabbbc") == "c"
    # assert candy_crush("aabbbacd") == "cd"
    assert candy_crush("baaabbbabbccccd") == "abbd"
    assert candy_crush("") == ""
    assert candy_crush("bbbbbbb") == ""
    assert candy_crush("aaabbbacd") == "acd"
    assert candy_crush("ccddccdcaacabbbaaccaccddcdcddd") == ""

