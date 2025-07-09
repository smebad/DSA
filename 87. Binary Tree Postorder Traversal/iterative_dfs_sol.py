# Binary Tree Postorder Traversal
# Iterative First Search (DFS) Solution:
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)

        return res
    
# Time Complexity: O(n) where n is the number of nodes in the tree. This is because we visit each node once.
# Space Complexity: O(n) where n is the number of nodes in the tree. This is because we use a stack to store the nodes.
# This iterative dfs solution uses a stack to traverse the tree in a depth-first manner and it is efficient for large trees.

# Test Cases
# Test Case 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().postorderTraversal(root)) # [2,3,1]

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().postorderTraversal(root)) # [4,5,2,6,7,3,1]

# Test Case 3:
root = None

print(Solution().postorderTraversal(root)) # []

# Test Case 4:
root = TreeNode(1)

print(Solution().postorderTraversal(root)) # [1]
