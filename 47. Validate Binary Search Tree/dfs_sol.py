# Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Depth-First Search Solution:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
    

# Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
# Space Complexity: O(h) or O(n) in the worst case, where h is the height of the tree. This is due to the recursion stack. In a balanced tree, h is O(log n), but in a skewed tree, h can be O(n).
# This solution uses a depth-first search (DFS) approach to validate the binary search tree properties by checking the value of each node against the allowed range defined by its ancestors. The left child must be less than the current node, and the right child must be greater than the current node, recursively ensuring that all nodes in the left subtree are less than the current node and all nodes in the right subtree are greater.


# Test Cases:
# Test case 1:
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(Solution().isValidBST(root1))  # Output: True

# Test case 2:
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(Solution().isValidBST(root2))  # Output: False

# Test case 3:
root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(20)
print(Solution().isValidBST(root3))  # Output: False