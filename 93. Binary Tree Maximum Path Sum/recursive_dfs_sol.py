# Binary Tree Maximum Path Sum
# Recursive Depth-First Search (DFS) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    
# Time Complexity: O(n) where n is the number of nodes in the tree. This is because in recursive DFS, we visit each node once.
# Space Complexity: O(n) where n is the number of nodes in the tree. This is because in recursive DFS, we need to store the maximum path sum at each node.
# This recursive DFS solution is efficient and works well for trees of all sizes.


# Test Cases
# Test Case 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().maxPathSum(root)) # 6

# Test Case 2:
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().maxPathSum(root)) # 42
