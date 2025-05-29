#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#


# @lc code=start
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.keyToFreq = {}
        self.freqs = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyToFreq:
            return -1
        # get old freq and val
        freq = self.keyToFreq[key]
        # remove val from freq bucket
        val = self.freqs[freq].pop(key)
        # add key to next bucket
        self.freqs[freq + 1][key] = val
        self.keyToFreq[key] += 1
        # increment minFreq if it was the freq and the old bucket is now empty
        if self.minFreq == freq and not self.freqs[freq]:
            self.minFreq += 1

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToFreq:
            self.get(key)
            self.freqs[self.keyToFreq[key]][key] = value
            return

        # evict LFU
        if len(self.keyToFreq) == self.capacity:
            popKey, _ = self.freqs[self.minFreq].popitem(last=False)
            self.keyToFreq.pop(popKey)
        self.keyToFreq[key] = 1
        self.freqs[1][key] = value
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
