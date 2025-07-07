# Binary Tree Inorder Traversal
# Depth-First Search (DFS) Solution:
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res
    
# Time Complexity: O(n) where n is the number of nodes in the binary tree. This is because we visit each node exactly once.
# Space Complexity: O(n) for the recursion stack in the worst case (when the tree is skewed), and O(n) for the result list in the best case (when all nodes are present). In a balanced tree, the space complexity for the recursion stack would be O(log n).
# This solution is efficient and meets the problem's constraints.


# Test Cases
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(Solution().inorderTraversal(root1)) # [1, 3, 2]

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(6)
print(Solution().inorderTraversal(root2)) # [4, 2, 5, 1, 6, 3]

# Test Case 3:
root3 = None
print(Solution().inorderTraversal(root3)) # []
