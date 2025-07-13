# Delete Leaves With a Given Value
# Recursive (post-order) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root
    
# Time Complexity: O(n) where n is the number of nodes in the tree. This is because we are visiting each node once. In the worst case, the tree is skewed, and we have to visit all nodes for each node.
# Space Complexity: O(h), where h is the height of the tree. This is the space used by the recursion stack. In the worst case, the height of the tree can be n, leading to O(n) space complexity.
# This recursive solution is optimal in terms of time and space complexity.

# Test Cases
# Test Case 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
target = 2
sol = Solution()
print(sol.removeLeafNodes(root, target))

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
target = 3
sol = Solution()
print(sol.removeLeafNodes(root, target))
