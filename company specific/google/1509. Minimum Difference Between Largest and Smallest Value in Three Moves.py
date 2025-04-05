def min_difference(arr):
    if len(arr)<=4:
        return 0

    arr.sort()
    return min(arr[-1]- arr[3], arr[-2]- arr[2], arr[-3] - arr[1], arr[-4] - arr[0])
