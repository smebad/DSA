# Validate Binary Search Tree
# Breadth-First Search Solution:

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
    

# Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
# Space Complexity: O(n) in the worst case, where n is the number of nodes in the tree. This is due to the queue used for BFS, which can hold all nodes in a skewed tree.
# This solution uses a breadth-first search (BFS) approach to validate the binary search tree properties by checking the value of each node against the allowed range defined by its ancestors. The left child must be less than the current node, and the right child must be greater than the current node, ensuring that all nodes in the left subtree are less than the current node and all nodes in the right subtree are greater.
# However, unlike the DFS approach, this BFS solution uses a queue to explore nodes level by level, maintaining the constraints of a binary search tree.
# Both solutions effectively check the validity of the binary search tree, but they differ in their traversal methods (DFS vs BFS).


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
