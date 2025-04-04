"""
You are given an n x n grid where grid[i][j] represents the number of obstacles in the cell (i, j). Every second, the number of obstacles in each cell decreases by 1, stopping at 0 (it does not go negative).

You are a dasher who can move in four directions (up, down, left, right). However, you can only enter a cell once its obstacle count reaches 0. Additionally, you can move across multiple cells in the same direction in one step, as long as all the traversed cells have an obstacle count of 0.

Your starting position is (0,0), and your goal is to reach the bottom-right corner (n-1, n-1) in the shortest possible time.

Constraints
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n^2
Each grid[i][j] value is unique.
Example
Input:

grid = [[0,1,2,3,4],
        [24,16,22,21,5],
        [12,13,14,15,23],
        [11,17,18,19,20],
        [10,9,8,7,6]]
Output:

16
Followup: What if the dasher can only move down or to the right?
"""