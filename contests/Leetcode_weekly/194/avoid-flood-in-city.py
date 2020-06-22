class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        [1,2,3,4]
        [1,2,0,0,2,1]
        [1,2,0,1,2]
        [69,0,0,0,69]
        [10,20,20]
        [1,0,2,3,0,1,2]
        """
        lookup = collections.defaultdict(lambda:collections.deque())
        for index, x in enumerate(rains):
            lookup[x].append(index)  
        heap = []     
        s = set()
        ans = []
        for index, x in enumerate(rains):
            if x > 0:
                if x in s:
                    return []
                s.add(x)
                while len(lookup[x]) > 0 and lookup[x][0] <= index:
                    lookup[x].popleft()
                if len(lookup[x]) > 0:
                    heapq.heappush(heap, (lookup[x][0], x))
                ans.append(-1)
            else:
                if len(heap) > 0:
                    _, y = heapq.heappop(heap)
                    s.remove(y)
                    ans.append(y)
                else:
                    ans.append(1)
        return ans