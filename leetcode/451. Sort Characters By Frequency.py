import collections
import heapq
def frequencySort(s):
    hm = collections.Counter(s)
    pq = []
    for keys in hm:
        heapq.heappush(pq,(-hm[keys],keys))
    res = ''
    for _ in range(len(pq)):
        c,k = heapq.heappop(pq)
        res = res + k*-c
    return res

print(frequencySort('tree'))