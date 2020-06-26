'''
Design a Leaderboard class, which has  functions:
Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
Return the score sum of the top K players.
Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.
'''

import heapq
import collections

class Leaderboard:
    def __init__(self):
        self.hm = collections.defaultdict(int)
    
    def addScore(self, id, score):
        self.hm[id] += score
                           
    def top(self, K)
        return sum(heapq.nlargest(K, self.hm.values()))

    def reset(self,id):
        del self.hm[id]


obj = Leaderboard()

'''
[1,73],[2,56],[3,39],[4,51],[5,4]


'''