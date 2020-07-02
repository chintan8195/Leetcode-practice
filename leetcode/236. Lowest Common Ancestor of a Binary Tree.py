'''
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''
class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def lca(root, p ,q):
    if not root:
        return None
    if root == p or root == q:
        return 
    left = lca(root.left,p,q)
    right = lca(root.right,p,q)
    if left and right:
        return root
    if not left:
        return right
    if not right:
        return left

    