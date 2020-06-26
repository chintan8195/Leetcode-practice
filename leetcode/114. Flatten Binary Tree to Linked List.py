'''
For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

root->left->right -> preorder 
'''
class Node:
    def __init__(self, val=0,left=None,right=None):
        self.val= val
        self.left =left
        self.right = right


def convert_tree_to_ll(root):
    while root:
        if root.left:
           convert_tree_to_ll(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right
            tail.right = root.right
            root.right = root.left
            root.left = None
        root = root.right




