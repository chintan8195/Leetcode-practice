def solution(A):
    N = len(A)

    # Edge case: if all elements are the same, return 0
    if all(x == A[0] for x in A):
        return 0

    # Case 1: fix i = 0, find furthest j from end such that A[0] != A[j]
    i = 0
    j = N - 1
    while i < j and A[i] == A[j]:
        j -= 1
    max_dist = j - i

    # Case 2: fix j = N-1, find furthest i from start such that A[i] != A[N-1]
    j = N - 1
    i = 0
    while i < j and A[i] == A[j]:
        i += 1
    max_dist = max(max_dist, j - i)

    return max_dist

A = list(range(75001))
print(solution(A))
