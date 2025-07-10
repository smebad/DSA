# Insert into a Binary Search Tree
# Recursive Solution:
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root
    
# Time Complexity: O(h) where h is the height of the tree. In the worst case, the tree is skewed, and we have to visit all nodes for each node.
# Space Complexity: O(h) where h is the height of the tree. This is the space used by the recursion stack.
# This recursive solution is optimal in terms of time and space complexity.

# Test Cases
# Test Case 1:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

val = 5

sol = Solution()
print(sol.insertIntoBST(root, val))

# Test Case 2:
root = TreeNode(40)
root.left = TreeNode(20)
root.right = TreeNode(60)
root.left.left = TreeNode(10)
root.left.right = TreeNode(30)
root.right.left = TreeNode(50)
root.right.right = TreeNode(70)

val = 25

sol = Solution()
print(sol.insertIntoBST(root, val))

