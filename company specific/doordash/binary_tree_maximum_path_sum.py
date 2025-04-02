"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

"""

from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None, alive=None):
        self.val = val
        self.left = left
        self.right = right
        self.alive = alive

def max_path_sum(root: TreeNode) -> int:
    maxSum = 0
    def post_dfs(node):
        if not node:
            return 0
        nonlocal maxSum
        left = max(0, post_dfs(node.left))
        right = max(0, post_dfs(node.right))
        maxSum = max(maxSum, left + right + node.val)
        return max(left + node.val, right + node.val)
    post_dfs(root)
    return maxSum

case1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

print(max_path_sum(case1))


"""Follow up:

Say our treeNode has an extra field called color. 
There are some nodes that are colored 'blue' and some other ones that are colored 'red'.
We now want to find the max path sum of any paths that start at a 'red' node and end at a 'red' node.
Note that paths can include 'blue' nodes, but for us to consider the sum for our max it has to both start at a red node and end at a red node.

Please let me know of any ideas, i've tried modifying the dfs function to include a check for the color of nodes before finding the max, but that only worked for paths that have all red nodes in the path.

Given a binary tree, find the maximum path sum from any two "alive nodes" within the tree. We can assume a node is an alive node if and only if it is a leaf node, indicated by an asterisk below.

     5
    /  \
   2    0
  /    /  \
*25   *14  *15

47 = 25 + 2 + 5 + 15
"""


def max_path_sum_between_alive_leaves(root: TreeNode) -> int:
    max_sum = float(-inf)
    def post_dfs(node):
        if not node:
            return float(-inf)
        if not node.left and not node.right:
            return node.val if node.alive else float(-inf)
       
        nonlocal max_sum
        
        # Recurse on left and right children.
        left_sum = post_dfs(node.left)
        right_sum = post_dfs(node.right)     

        if left_sum is not float(-inf) and right_sum is not float(-inf):
            max_sum = max(max_sum, left_sum + node.val + right_sum)
        return node.val + max(left_sum, right_sum)

    post_dfs(root)
    return max_sum

def run_tests():
    # Test Case 1: Given Example
    # Construct the tree:
    #         5
    #        / \
    #       2   0
    #      /   / \
    #    *25  *14 *15
    leaf25 = TreeNode(25, alive=True)
    leaf14 = TreeNode(14, alive=True)
    leaf15 = TreeNode(15, alive=True)
    node2 = TreeNode(2, left=leaf25)
    node0 = TreeNode(0, left=leaf14, right=leaf15)
    root1 = TreeNode(5, left=node2, right=node0)
    # Expected path: 25 -> 2 -> 5 -> 15 = 47
    print("Test Case 1 Expected: 47, Got:", max_path_sum_between_alive_leaves(root1))
    
    # Test Case 2: Single Alive Leaf (should not update maxSum)
    # Tree:
    #      10
    #     /
    #   *20
    leaf20 = TreeNode(20, alive=True)
    root2 = TreeNode(10, left=leaf20)
    # Only one alive leaf, so no valid path between two alive nodes exists.
    print("Test Case 2 Expected: -inf, Got:", max_path_sum_between_alive_leaves(root2))
    
    # Test Case 3: Mixed alive and non-alive leaves
    # Construct tree:
    #          1
    #         / \
    #      *2    3
    #           / \
    #         *4   5 (not alive)
    leaf2 = TreeNode(2, alive=True)
    leaf4 = TreeNode(4, alive=True)
    leaf5 = TreeNode(5, alive=False)
    node3 = TreeNode(3, left=leaf4, right=leaf5)
    root3 = TreeNode(1, left=leaf2, right=node3)
    # Valid path is only between 2 and 4: 2 + 1 + 3  + 4 = 10.
    print("Test Case 3 Expected: 10, Got:", max_path_sum_between_alive_leaves(root3))
    
    # Test Case 4: Empty Tree
    root4 = None
    print("Test Case 4 Expected: -inf, Got:", max_path_sum_between_alive_leaves(root4))
    
    # Test Case 5: Only root
    root5 = TreeNode(1, None, None, True)
    print("Test Case 5 Expected: -inf, Got:", max_path_sum_between_alive_leaves(root5))

    root6 = TreeNode(1, None, None, False)
    print("Test Case 6 Expected: -inf, Got:", max_path_sum_between_alive_leaves(root6))

run_tests()

"""
Followup: What if any nodes in the tree can be alive instead of just the leaves?
"""
def max_path_sum_between_alive_nodes(root: TreeNode):
    maxSum = float("-inf")
    def dfs(node: TreeNode) -> int:
        nonlocal maxSum
        if not node:
            return float("-inf")
        left = dfs(node.left)
        right = dfs(node.right)
        
        if node.alive:
            # Candidate branch: current node itself is a valid endpoint.
            branch = node.val
            # If either child yields a valid branch, extend from this node.
            if left != float("-inf"):
                branch = max(branch, node.val + left)
            if right != float("-inf"):
                branch = max(branch, node.val + right)
            # If both children are valid, we can form a full path (left + node + right)
            if left != float("-inf") and right != float("-inf"):
                maxSum = max(maxSum, left + node.val + right)
            # Also update global with the branch value (this covers the case where
            # a single alive node or its branch is the only candidate)
            maxSum = max(maxSum, branch)
            return branch
        else:
            # Current node is not alive. It cannot serve as an endpoint.
            # We can only return a valid branch if both children exist to form a bridge.
            if left != float("-inf") and right != float("-inf"):
                maxSum = max(maxSum, left + node.val + right)
                return node.val + max(left, right)
            else:
                # Not enough to form a valid branch from this node.
                return float("-inf")

    dfs(root)
    return maxSum