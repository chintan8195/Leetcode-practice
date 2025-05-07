#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#


# @lc code=start
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not beginWord or not endWord or endWord not in wordList:
            return 0
        visited = set()
        q = deque()
        q.append((beginWord, 1))
        wordList = set(wordList)
        visited.add(beginWord)
        letters = string.ascii_lowercase
        while q:
            word, count = q.popleft()
            if word == endWord:
                return count
            for i in range(len(word)):
                for l in letters:
                    new_word = word[:i] + l + word[i + 1 :]
                    if new_word in wordList and new_word not in visited:
                        q.append((new_word, count + 1))
                        visited.add(new_word)
        return 0


# @lc code=end
