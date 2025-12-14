# Convert BST to Greater Tree
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -104 <= Node.val <= 104
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.


# Depth First Search (DFS) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        def dfs(node):
            nonlocal curSum
            if not node:
                return

            dfs(node.right)
            tmp = node.val
            node.val += curSum
            curSum += tmp
            dfs(node.left)

        dfs(root)
        return root

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(h), where h is the height of the tree. This space is used by the recursion stack. In the worst case (unbalanced tree), h can be n, leading to O(n) space complexity. In a balanced tree, h would be log(n).
# This dfs is efficient for converting a BST to a Greater Tree by leveraging the properties of BSTs and performing a reverse in-order traversal.


# Test Cases
if __name__ == "__main__":
    # Helper function to print in-order traversal of the tree
    def print_inorder(node):
        if not node:
            return
        print_inorder(node.left)
        print(node.val, end=' ')
        print_inorder(node.right)

    # Test Case 1
    root1 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(2)
    root1.left.right.right = TreeNode(3)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    root1.right.right.right = TreeNode(8)

    solution = Solution()
    new_root1 = solution.convertBST(root1)
    print("In-order traversal of Greater Tree for Test Case 1:")
    print_inorder(new_root1)  # Expected output: 36 36 35 33 30 26 21 15 8
    print()

    # Test Case 2
    root2 = TreeNode(0)
    root2.right = TreeNode(1)

    new_root2 = solution.convertBST(root2)
    print("In-order traversal of Greater Tree for Test Case 2:")
    print_inorder(new_root2)  # Expected output: 1 1
    print()