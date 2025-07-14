# House Robber III
# Recursion Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
        
        res = max(res, self.rob(root.left) + self.rob(root.right))
        return res
    
# Time Complexity: O(2^n) where n is the number of nodes in the binary tree. This is because the function is called recursively for each node in the tree, and there are 2 choices for each node (rob it or not rob it).
# Space Complexity: O(n) where n is the number of nodes in the binary tree. This is because the function uses a stack to store the nodes in the tree.
# This recursion solution is not optimal for large trees, as it has a time complexity of O(2^n) but it is efficient for small trees like the one in the example.

# Test Cases
# Test Case 1:
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

print(Solution().rob(root)) # 7

# Test Case 2:
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

print(Solution().rob(root)) # 9
