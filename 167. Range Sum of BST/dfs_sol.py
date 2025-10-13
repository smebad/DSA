# Range Sum of BST
# Depth-First Search (DFS) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        res = root.val if low <= root.val <= high else 0
        res += self.rangeSumBST(root.left, low, high)
        res += self.rangeSumBST(root.right, low, high)
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the binary search tree. In the worst case, we may need to visit all nodes.
# Space Complexity: O(n), which is the space used by the recursion stack in the worst case (when the tree is skewed). In a balanced tree, the space complexity would be O(h), where h is the height of the tree.
# This DFS solution is straightforward and works well within the given constraints.


# Test Cases:
# Test Case 1:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

low = 7
high = 15

sol = Solution()
print(sol.rangeSumBST(root, low, high))  # Expected output: 32

# Test Case 2:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(6)

low = 6
high = 10

sol = Solution()
print(sol.rangeSumBST(root, low, high))  # Expected output: 23
