# Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:

# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


# Depth-First Search Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum

            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)
    
# Time Complexity: O(n), where n is the number of nodes in the tree. In the worst case, we may need to visit all nodes.
# Space Complexity: O(n), recursion stack space in the worst case (for a skewed tree). In the average case, the space complexity is O(h), where h is the height of the tree.
# This solution efficiently checks for a root-to-leaf path with the given sum using depth-first search.


# Test Cases:
sol = Solution()

# Test Case 1:
root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.left = TreeNode(1)
targetSum1 = 22
print(sol.hasPathSum(root1, targetSum1))  # Output: True

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
targetSum2 = 5
print(sol.hasPathSum(root2, targetSum2))  # Output: False

# Test Case 3:
root3 = None
targetSum3 = 0
print(sol.hasPathSum(root3, targetSum3))  # Output: False