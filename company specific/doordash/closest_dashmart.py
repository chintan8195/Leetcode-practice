""" 

Find Closest DashMart
A DashMart is a warehouse run by DoorDash that houses items found in convenience stores, grocery stores, and restaurants. 
We have a city with open roads, blocked-off roads, and DashMarts.

City planners want you to identify how far a location is from its closest DashMart.

You can only travel over open roads (up, down, left, right). Locations are given in [row, col] format.

Example 1:

Given a grid where:

'O' represents an open road that you can travel over in any direction (up, down, left, or right).
'X' represents a blocked road that you cannot travel through.
'D' represents a DashMart.
The grid is provided as a 2D array, and a list of locations is provided where each location is a pair [row, col].

[
  ['X', 'O', 'O', 'D', 'O', 'O', 'X', 'O', 'X'], #0
  ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'], #1
  ['O', 'O', 'O', 'D', 'X', 'X', 'O', 'X', 'O'], #2
  ['O', 'O', 'D', 'O', 'D', 'O', 'O', 'O', 'X'], #3
  ['O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'], #4
  ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'X'], #5
]

List of pairs `[row, col]` for locations:
[
  [200, 200],
  [1, 4],
  [0, 3],
  [5, 8],
  [1, 8],
  [5, 5],
]
Your task is to return the distance for each location from the closest DashMart.

Provided:

city: char[][]
locations: int[][]
Return:

answer: int[]
"""

def closest_dashmart(grid):
    open_road = '0'
    dash_mart = 'D'
    directions = [[-1,0], [0,-1], [1,0], [0,1]]
    rows = len(grid)
    cols = len(grid[0])

    if rows == 0:
        return

    visited = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == dash_mart:
                visited.append([row, col])

    while len(visited) > 0:
        row, col = visited.pop(0)
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] != open_road:
                continue
            visited.append([new_row, new_col])
            grid[new_row][new_col] = grid[row][col] + 1
