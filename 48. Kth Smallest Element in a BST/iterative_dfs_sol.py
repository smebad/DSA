# Kth Smallest Element in a BST
# Iterative DFS Solution:

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


# Time COmplexity: O(n), where n is the number of nodes in the tree. In the worst case, we may need to traverse all nodes.
# Space Complexity: O(n), where n is the height of the tree. In the worst case, the stack can grow to the height of the tree, which is O(n) for a skewed tree.
# Note: This solution uses an iterative depth-first search (DFS) approach to traverse the binary search tree in an in-order manner, which ensures that we visit nodes in ascending order of their values.


# Test Cases:
# Test Case 1:
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(2)
k1 = 1
print(Solution().kthSmallest(root1, k1))  # Output: 1

# Test Case 2:  
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)
k2 = 3
print(Solution().kthSmallest(root2, k2))  # Output: 3
