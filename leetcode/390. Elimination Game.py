def lastRemaining(self, n: int) -> int:
    arr = range(1,n+1)
    while len(arr)>1:
        arr = arr[1::2][::-1]
    return arr[0]