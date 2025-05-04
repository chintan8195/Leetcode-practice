def min_travel_time(l: int, position: list[int], time: list[int], k: int) -> int:
    n = len(position)
    S = n - 1  # number of actual segments

    # 1) segment lengths and times
    d = [position[i + 1] - position[i] for i in range(S)]
    t = time[:S]  # only the first S entries correspond to segments

    # 2) prefix‐sums for O(1) block‐cost queries
    D = [0] * (S + 1)
    T = [0] * (S + 1)
    for i in range(S):
        D[i + 1] = D[i] + d[i]
        T[i + 1] = T[i] + t[i]

    M = S - k  # how many segments we end up with
    INF = 10**30

    # dp[i][b] = min cost to partition first i segments into b blocks
    dp = [[INF] * (M + 1) for _ in range(S + 1)]
    dp[0][0] = 0

    # base: one block covering 0..i−1
    for i in range(1, S + 1):
        dp[i][1] = (D[i] - D[0]) * (T[i] - T[0])

    # fill dp for b = 2..M
    for b in range(2, M + 1):
        for i in range(b, S + 1):
            best = INF
            # last block covers segments j..i−1
            for j in range(b - 1, i):
                cost_block = (D[i] - D[j]) * (T[i] - T[j])
                val = dp[j][b - 1] + cost_block
                if val < best:
                    best = val
            dp[i][b] = best

    return dp[S][M]


l = 10
n = 4
k = 1
position = [0, 3, 8, 10]
time = [5, 8, 3, 6]
print(min_travel_time(l, position, time, k))
