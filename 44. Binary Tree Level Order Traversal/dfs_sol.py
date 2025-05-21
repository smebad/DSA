# Binary Tree Level Order Traversal
# Depth-First Search (DFS) solution:

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

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
    

# Time complexity: O(n), where n is the number of nodes in the tree this is because we visit each node once.
# Space complexity: O(n), where n is the number of nodes in the tree this is because we store all nodes in the result list.
# This dfs solution is more space efficient than the bfs solution in my opinion because it does not use a queue to store nodes at each level.
# However, this problem can be solved using both dfs and bfs approaches.


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
