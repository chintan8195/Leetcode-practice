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
    