# Balanced Binary Tree
# Depth First Solution:

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    
# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once. This is because we are using a depth-first search (DFS) approach to traverse the tree. In the worst case, the tree is skewed, and we have to visit all nodes for each node.
# Space Complexity: O(h), where h is the height of the tree. This is the space used by the recursion stack. In the worst case, the height of the tree can be n, leading to O(n) space complexity.
# However this solution is more optimal than the brute force solution as it calculates the height of the tree in a single traversal, making it O(n) in time complexity.


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
