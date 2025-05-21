# Binary Tree Level Order Traversal
# Breadth-first search (BFS) solution:

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
                
        return res
    

# Time complexity: O(n), where n is the number of nodes in the tree this is because we visit each node once.
# Space complexity: O(n), where n is the maximum number of nodes at any level in the tree. In the worst case, this can be O(n) if the tree is a complete binary tree.
# This bfs solution is efficient and works well for large trees. It uses a queue to keep track of the nodes at each level and processes them in a breadth-first manner also the solution is easy to understand and implement.


# Test Cases:
# Test Case 1:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root)) # [[3], [9, 20], [15, 7]]

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().levelOrder(root)) # [[1], [2, 3], [4, 5]]

# Test Case 3:
root = None

print(Solution().levelOrder(root)) # []
