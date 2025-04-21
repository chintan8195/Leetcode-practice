#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        left = 0
        
        for end in range(1, len(chars)+1): 
            if end<len(chars) and chars[end] == chars[end-1]:
                count += 1
            else:
                chars[left] = chars[end-1]
                left += 1
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left += 1
                count = 1
                
        return left
            
        
# @lc code=end

