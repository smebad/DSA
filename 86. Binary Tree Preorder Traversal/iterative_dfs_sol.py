# Binary Tree Preorder Traversal
# Iteratvie Depth-First Search (DFS) Solution:
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return
            
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res
    
# Time Complexity: O(n) where n is the number of nodes in the tree, as we visit each node exactly once. This is because in a preorder traversal, we visit the root node first, then recursively visit the left subtree, followed by the right subtree.
# Space Complexity: O(h) where h is the height of the tree, due to the recursion stack. In the worst case, the height of the tree can be n (if the tree is skewed), leading to O(n) space complexity. In a balanced tree, the height would be O(log n), leading to O(log n) space complexity.
# This iterative solution is efficient and handles the preorder traversal without using an explicit stack, relying on the recursion stack instead.


# Test Cases
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
solution = Solution()
print(solution.preorderTraversal(root1))  # Output: [1, 2,

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
root2.left.left.left = TreeNode(8)
root2.left.left.right = TreeNode(9)
root2.left.right.left = TreeNode(10)
root2.left.right.right = TreeNode(11)
root2.right.left.left = TreeNode(12)
root2.right.left.right = TreeNode(13)
root2.right.right.left = TreeNode(14)
root2.right.right.right = TreeNode(15)
solution = Solution()
print(solution.preorderTraversal(root2))  # Output: [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]

# Test Case 3:
root3 = None
solution = Solution()
print(solution.preorderTraversal(root3))  # Output: []

# Test Case 4:
root4 = TreeNode(1)
solution = Solution()
print(solution.preorderTraversal(root4))  # Output: [1]
