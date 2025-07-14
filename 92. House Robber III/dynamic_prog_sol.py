# House Robber III
# Dynamic Programming Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [0, 0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]

        return max(dfs(root))
    
# Time Complexity: O(n) where n is the number of nodes in the binary tree. This is because dynamic programming requires us to visit each node once.
# Space Complexity: O(n) where n is the number of nodes in the binary tree. This is because dynamic programming requires us to store the maximum amount of money we can rob at each node.
# This dynamic programming solution is efficient and works well for trees of all sizes.

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
