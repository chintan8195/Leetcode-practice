def countSquares(grid):
    if grid is None or len(grid)==0:
        return 0

    rows = len(grid)
    columns = len(grid[0])

    result = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j]==1:
                if i ==0 or j == 0:
                    result +=1
                else:
                    val = min(grid[i-1][j], grid[i-1][j-1], grid[i][j-1]) + grid[i][j]
                    result += val
                    grid[i][j] = val
    return result
