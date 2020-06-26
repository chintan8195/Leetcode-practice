# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
# 1 <= numCourses <= 10^5
# 
# [1,2],[2,3],[3,4],[4,1]
# 1->2->3->4

'''
1->2
2->3
3->4
4->1

'''
import collections
def course_schedule(numCourses, prerequisites):
    if not prerequisites:
        return True
    def dfs(node):
        if visited[node]==1:
            return False
        visited[node] = 1
        for other in hm[node]:
            if visited[other] != 2 and not dfs(other):
                return False
        visited[node] = 2
        return True

    hm = collections.defaultdict(list)
    for i,j in prerequisites:
        hm[j].append(i)
        hm[i]

    visited = [0]*numCourses
    for node in hm:
        if not visited[node]:
            if not dfs(node):
                return False
    return True

print(course_schedule(4,[[1,2],[2,3],[3,4],[4,1]]))