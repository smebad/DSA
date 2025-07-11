# Delete Node in a BST
# Recursive solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root
    
# Time Complexity: O(h) where h is the height of the tree. In the worst case, the tree is skewed, and we have to visit all nodes for each node.
# Space Complexity: O(h) where h is the height of the tree. This is the space used by the recursion stack.
# This recursive solution is optimal in terms of time and space complexity.


# Test Cases
# Test Case 1:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
key = 3
print(Solution().deleteNode(root, key))  # Output: [5,4,6,2,null,null,7]

# Test Case 2:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
key = 0
print(Solution().deleteNode(root, key))  # Output: [5,3,6,2,4,null,7]

# Test Case 3:
root = None
key = 0
print(Solution().deleteNode(root, key))  # Output: []
