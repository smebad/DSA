# Leaf-Similar Trees
# Depth First Search (DFS) solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2
    
# Time complexity: O(m + n), where m and n are the number of nodes in the two trees. We need to traverse both trees to collect their leaf sequences.
# Space complexity: O(h1 + h2), where h1 and h2 are the heights of the two trees. This space is used by the recursion stack during the DFS traversal.
# This depth first search (DFS) approach collects the leaf value sequences of both trees and compares them to determine if they are leaf-similar.


# Test Cases:
if __name__ == "__main__":
    # Test Case 1:
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    sol = Solution()
    print(sol.leafSimilar(root1, root2))  # Output: True

    # Test Case 2:
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)

    root4 = TreeNode(1)
    root4.left = TreeNode(3)
    root4.right = TreeNode(2)

    print(sol.leafSimilar(root3, root4))  # Output: False
