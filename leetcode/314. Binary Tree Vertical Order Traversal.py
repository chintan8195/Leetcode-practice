"""
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

[9][3,15][20][7]
"""
import collections
class Node:
    def __init__(self, val = 0,left = None,right= None):
        self.val = val
        self.left = left
        self.right = right
    
def vertical_traversal(self, root):
    cols = collections.defaultdict(list)
    q = [(root,0)]
    for node,i in q:
        if node:
            cols[i].append(node.val)
            q += (node.left,i+1) , (node.right,i-1)
    return [cols[i] for i in sorted(cols)]