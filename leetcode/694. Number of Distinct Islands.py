'''
Example 1:
11000
11000
00011
00011

Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.
'''

def distinct_islands(grid):
    if not grid:
        return 0
    visited = set()
    paths = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = set()
            if grid[i][j]== 1:
                dfs(grid,i,j,i,j,path,visited)
                if path:
                    paths.add(frozenset(path))
    return len(paths)

def dfs(grid,i,j,r,c, path,visited):
    if i<0 or i>=len(grid) or j<0 or j >= len(grid[0]) or grid[i][j]==0 or (i,j) in visited:
        return 
        
    visited.add((i,j))
    path.add((i-r, j-c))
    dfs(grid,i-1,j,r,c,path,visited)
    dfs(grid,i+1,j,r,c,path,visited)
    dfs(grid,i,j-1,r,c,path,visited)
    dfs(grid,i,j+1,r,c,path,visited)