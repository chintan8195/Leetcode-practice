#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict()
        for i in range(numCourses):
            adj_list[i] = []
        for course, pre in prerequisites:
            adj_list[course].append(pre)
            
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.add(course)
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            adj_list[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        
# @lc code=end

