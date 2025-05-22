# Binary Tree Right Side View
# Breadth First Search (BFS) Solution:

from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
    
# Time Complexity: O(n) where n is the number of nodes in the tree because we visit each node once.
# Space Complexity: O(n) where n is the maximum number of nodes at any level of the tree. In the worst case, this can be O(n) for a complete binary tree.
# This bfs solution is optimal for this problem as it traverses the tree level by level and captures the rightmost node at each level.



# Test case 1 (Matches Example 1)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(Solution().rightSideView(root))  # [1, 3, 4]

# Test case 2 (Matches Example 2)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

print(Solution().rightSideView(root))  # [1, 3, 4, 5]

# Test case 3 (Matches Example 3)
root = TreeNode(1)
root.right = TreeNode(3)

print(Solution().rightSideView(root))  # [1, 3]

# Test case 4 (Matches Example 4)
root = None

print(Solution().rightSideView(root))  # []
