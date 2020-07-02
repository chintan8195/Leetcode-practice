def maximal_square(grid):
    if grid is None or len(grid) < 1:
            return 0
    m = len(grid)
    n = len(grid[0]) 
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_side = 0  
    for i in range(m):
        for j in range(n):
            if grid[i][j]=="1":
                dp[i+1][j+1] = min(dp[i+1][j],dp[i][j],dp[i][j+1])+1
                max_side = max(max_side,dp[i+1][j+1])
    return max_side * max_side


# Without extra row and col
def maximal_square(matrix):
    if not matrix: return 0
    m , n = len(matrix), len(matrix[0])
    dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 0
    
    res = max(max(row) for row in dp)
    return res ** 2