class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [0]*n
        for i in range(n):
            arr[i] = start + 2*i
        xor_arr = 0
        for i in range(n): 
            xor_arr = xor_arr ^ arr[i] 
        return xor_arr 