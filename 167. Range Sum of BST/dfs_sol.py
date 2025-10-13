# Range Sum of BST
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.


# Depth-First Search (DFS) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        res = root.val if low <= root.val <= high else 0
        res += self.rangeSumBST(root.left, low, high)
        res += self.rangeSumBST(root.right, low, high)
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the binary search tree. In the worst case, we may need to visit all nodes.
# Space Complexity: O(n), which is the space used by the recursion stack in the worst case (when the tree is skewed). In a balanced tree, the space complexity would be O(h), where h is the height of the tree.
# This DFS solution is straightforward and works well within the given constraints.


# Test Cases:
# Test Case 1:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

low = 7
high = 15

sol = Solution()
print(sol.rangeSumBST(root, low, high))  # Expected output: 32

# Test Case 2:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(6)

low = 6
high = 10

sol = Solution()
print(sol.rangeSumBST(root, low, high))  # Expected output: 23