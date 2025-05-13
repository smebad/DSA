# Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Depth First Search (DFS) Solution:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack.
# Recursion is used to traverse the tree, and the maximum depth of the recursion stack will be equal to the height of the tree.
# This DFS solution is efficient and works well for trees of all sizes.
# The time complexity is linear because we visit each node exactly once.


# Test Cases:

# Test Case 1:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(Solution().invertTree(root)) # [4,7,2,9,6,3,1]

# Test Case 2:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().invertTree(root)) # [2,3,1]

# Test Case 3:
root = None
print(Solution().invertTree(root)) # []