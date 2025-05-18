# Depth First Search
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# Depth First Search Solution:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        

# Time Complexity: O(n) where n is the number of nodes in the tree. This is because we need to visit each root node once.
# Space Complexity: O(h) where h is the height of the tree. This is because we need to keep track of the nodes in the stack during the recursive calls.
# The maximum height of a binary tree is O(n) in the case of a skewed tree, and O(log n) in the case of a balanced tree.
# This depth first search solution is efficient and works well for both balanced and unbalanced trees.


# Test Cases:

# Test Case 1:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(Solution().isSameTree(root1, root2)) # True

# Test Case 2:
root3 = TreeNode(1)
root3.left = TreeNode(2)

root4 = TreeNode(1)
root4.right = TreeNode(2)

print(Solution().isSameTree(root3, root4)) # False

# Test Case 3:
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(1)

root6 = TreeNode(1)
root6.left = TreeNode(1)
root6.right = TreeNode(2)

print(Solution().isSameTree(root5, root6)) # False