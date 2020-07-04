#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val=val
#         self.left=left
#         self.right = right


#BFS 
import collections 
class Solution:
    def findBottomLeftValue(self, root: TreeNode):
        q = collections.deque([root])
        result = root
        level = 0
        while q:
            count = len(q)
            for i in range(count):
                node= q.popleft()
                if not i:
                    result = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result.val

#DFS
class Solution:
    def findBottomLeftValue(self, root: TreeNode):
        self.ans = None
        self.max_level = -1
        self.dfs(root, 0)
        return self.ans
            
    def dfs(self, root, depth):
        if not root:
            return
        if depth > self.max_level:
            self.max_level = depth
            self.ans = root.val
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)