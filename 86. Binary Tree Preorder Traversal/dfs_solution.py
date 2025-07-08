# Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?


# Depth-First Search (DFS) Solution:
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
    
# Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once. In the worst case, the tree is a linked list, so the time complexity is O(n).
# Space Complexity: O(n), where n is the number of nodes in the tree. In the worst case, the tree is a linked list, so the space complexity is O(n).
# This depth-first search (DFS) solution uses recursion to traverse the tree in preorder (root, left, right) and collects the values in a list. The base case is when the node is None, at which point the function returns without doing anything. The function appends the current node's value to the result list and then recursively calls itself for the left and right children of the current node.


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
