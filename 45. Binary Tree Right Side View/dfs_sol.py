# Binary Tree Right Side View
# Depth First Search (DFS) Solution:

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

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
    
# Time Complexity: O(n) where n is the number of nodes in the tree because we visit each node once.
# Space Complexity: O(n) where n is the maximum number of nodes at any level of the tree. In the worst case, this can be O(n) for a complete binary tree.
# This dfs solution is more space efficient than the bfs solution because it does not require a queue to store nodes at each level. Instead, it uses recursion to traverse the tree and build the result list.
# However both solutions have the same time complexity of O(n) since they both visit each node once.



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
