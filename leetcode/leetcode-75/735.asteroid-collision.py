#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()  # top explodes
                    continue
                elif stack[-1] == -a:
                    stack.pop()  # both explode
                break
            else:
                stack.append(a)

        return stack
        
# @lc code=end

