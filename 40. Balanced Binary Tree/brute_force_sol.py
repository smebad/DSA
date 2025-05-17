# Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.

 

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# Brute Force Solution:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
    
# Time Complexity: O(n^2) in the worst case, where n is the number of nodes in the tree. This is because for each node, we are calculating the height of its left and right subtrees, which takes O(n) time. In the worst case, the tree is skewed, and we have to visit all nodes for each node.
# Space Complexity: O(h), where h is the height of the tree. This is the space used by the recursion stack. In the worst case, the height of the tree can be n, leading to O(n) space complexity.
# However, in a balanced tree, the height is log(n), leading to O(log n) space complexity.
# The brute force solution is not optimal for large trees, as it has a time complexity of O(n^2).


# Test Cases:

# Test Case 1:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().isBalanced(root)) # True

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)

print(Solution().isBalanced(root)) # False

# Test Case 3:
root = None
print(Solution().isBalanced(root)) # True