# Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?


# Iterative Depth-First Search (DFS) Solution:
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the binary tree. Each node is processed once. This is because we traverse each node exactly once, either by visiting it or by pushing it onto the stack.
# Space Complexity: O(n) iteratively, where n is the number of nodes in the binary tree. This is because we use a stack to store the nodes that we have not yet visited.
# This iterative solution uses a stack to simulate the recursive call stack used in the recursive solution. It allows us to traverse the tree in an inorder manner without using recursion.


# Test Cases
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(Solution().inorderTraversal(root1)) # [1, 3, 2]

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(6)
print(Solution().inorderTraversal(root2)) # [4, 2, 5, 1, 6, 3]

# Test Case 3:
root3 = None
print(Solution().inorderTraversal(root3)) # []
