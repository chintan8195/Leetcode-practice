def canMakeArithmeticProgression(arr):
        arr.sort()
        count = arr[1]-arr[0]
        for i in range(2,len(arr)):
            diff = arr[i]-arr[i-1]
            if diff != count:
                return False
        return True