# Minimum Distance Between BST Nodes
# Inorder Traversal Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            nonlocal prev, res
            if not node:
                return

            dfs(node.left)
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)
        return res

# Time Complexity: O(n), where n is the number of nodes in the BST. We visit each node exactly once during the inorder traversal.
# Space Complexity: O(n) due to the recursion stack in the worst case (unbalanced tree). In the average case (balanced tree), the space complexity is O(h), where h is the height of the tree.
# This solution efficiently finds the minimum difference between values of any two different nodes in a BST using inorder traversal, which processes nodes in ascending order.


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Helper function
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Test Case 1
    root1 = None
    for val in [4, 2, 6, 1, 3]:
        root1 = insert_into_bst(root1, val)
    print(sol.minDiffInBST(root1))  # Output: 1

    # Test Case 2
    root2 = None
    for val in [1, 0, 48, 12, 49]:
        root2 = insert_into_bst(root2, val)
    print(sol.minDiffInBST(root2))  # Output: 1
