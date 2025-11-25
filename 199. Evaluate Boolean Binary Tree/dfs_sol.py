# Evaluate Boolean Binary Tree
# Depth-First Search (DFS) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val == 1

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(n), where n is the height of the tree due to the recursion stack. In the worst case, the tree can be skewed, leading to a height of n.
# This dfs solution efficiently evaluates the boolean binary tree by recursively evaluating each node based on its value and the evaluations of its children.


# Test Cases
if __name__ == "__main__":
    sol = Solution()
 
    # Test Case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(1)
    print(sol.evaluateTree(root1))  # Output: True

    # Test Case 2
    root2 = TreeNode(0)
    print(sol.evaluateTree(root2))  # Output: False
