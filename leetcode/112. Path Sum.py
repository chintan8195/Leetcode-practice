def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
    if not root:
        return False
    sum_=sum_-root.val
    if not root.left and not root.right:  # if reach a leaf
        return sum_ == 0
    res_left = self.hasPathSum(root.left,sum_)
    res_right = self.hasPathSum(root.right,sum_)
    return res_left or res_right