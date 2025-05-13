# Invert Binary Tree
# Breadth First Search (BFS) Solution:

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(n), where n is the number of nodes in the tree. In the worst case, we may have to store all nodes in the queue.
# This BFS solution is efficient and works well for trees of all sizes.
# Differece betwen DFS and BFS is that DFS uses recursion and a stack, while BFS uses a queue to traverse the tree level by level.
# However, both approaches have the same time complexity of O(n) since they both visit each node once.


# Test Cases:

# Test Case 1:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(Solution().invertTree(root)) # [4,7,2,9,6,3,1]

# Test Case 2:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().invertTree(root)) # [2,3,1]

# Test Case 3:
root = None
print(Solution().invertTree(root)) # []
