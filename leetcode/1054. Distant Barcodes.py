'''
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

'''

# Will not work for  uneven integers like [1,2,2,2,5]
def distant(barcodes):
    barcodes = sorted(barcodes)
    i=0
    j=len(barcodes)-1
    while i<j:
        if barcodes[i]==barcodes[i+1]:
            barcodes.insert(i+1,barcodes[j])
            i+=1
            barcodes.pop()
        else:
            i+=1
    return barcodes

#print(distant([2,2,2,1,5]))
# [1,2,2,2,5]
import collections
import heapq
# Using Priority Queue
def distant_barcodes( barcodes):
    heap = []
    count = collections.Counter(barcodes)
    for key,value in count.items():
        heapq.heappush(heap,[-value,key])
    ans = [0]*len(barcodes)
    i = 0 
    while heap:
        freq,code = heapq.heappop(heap)
        for _ in range(-freq):
            if i >= len(barcodes):
                i=1
            ans[i]=code
            i+=2
    return ans
print(distant_barcodes([2,2,2,1,5]))

#Using Counter inbuilt function
def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    count = collections.Counter(barcodes)
    i = 0
    ans = [0]*len(barcodes)
    for code,freq in count.most_common():
        for _ in range(freq):
            if i >= len(barcodes):
                i=1
            ans[i]=code
            i+=2
    return ans
