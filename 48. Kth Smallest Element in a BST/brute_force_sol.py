# Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


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
        arr = []

        def dfs(node):
            if not node:
                return
            
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        arr.sort()
        return arr[k - 1]


# Time COmplexity: O(n log n), where n is the number of nodes in the tree. The sorting step takes O(n log n) time. This is because we traverse all nodes to collect their values and then sort the list of values.
# Space Complexity: O(n), where n is the number of nodes in the tree. We store all node values in a list, which can grow to the size of the number of nodes in the tree.
# Note: This solution uses a brute force approach to collect all node values in a list, sorts the list, and then retrieves the kth smallest value. This is less efficient than the iterative DFS approach but is straightforward and easy to understand.
# However, it is not optimal for large trees due to the sorting step.


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
