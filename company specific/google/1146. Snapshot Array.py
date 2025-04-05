from collections import defaultdict


class snapshot_array:

    def __init__(self, length):
        self.map = defaultdict(list)
        self.snap_id = 0

    def set(self, index, val):
        if self.map[index] and self.map[index][-1][0] == self.snap_id:
            self.map[index][-1][1] = val
        self.map[index].append([self.snap_id, val]) 

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1 

    def get(self, index, snap_id):
        arr = self.map
        left,right,ans = 0, len(arr), -1
        while left<=right:
            mid =(left+right)//2
            if arr[mid][0]<=snap_id:
                ans = mid
                left = mid +1
            else:
                right = mid - 1
        if ans == -1: return 0
        return arr[ans][1]