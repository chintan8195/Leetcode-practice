"""
There is a new alien language which uses the Latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""
Explanation: The order is invalid, so return "".

Note:

Assume all letters are in lowercase.
Assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

"""

from collections import deque


def alien_dictionary(words):
    adj_list = {c: set() for word in words for c in word}
    indegree = {c: 0 for c in adj_list}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj_list[w1[j]]:
                    adj_list[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    q = deque([c for c in indegree if indegree[c] == 0])
    order = []
    while q:
        c = q.popleft()
        order.append(c)
        for v in adj_list[c]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    if len(order) != len(indegree):
        return ""
    return order


input = ["wrt", "wrf", "er", "ett", "rftt"]
print(alien_dictionary(input))
