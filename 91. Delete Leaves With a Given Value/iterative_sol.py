# Delete Leaves With a Given Value
# Iterative (post-order) Solution:
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        visit = set()
        parents = {root: None}

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if node.val == target:
                    p = parents[node]
                    if not p:
                        return None
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif node not in visit:
                visit.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node

        return root
    
# Time Complexity: O(n) where n is the number of nodes in the tree. This is because we are visiting each node once. In the worst case, the tree is skewed, and we have to visit all nodes for each node.
# Space Complexity: O(n) where n is the number of nodes in the tree. This is because we are using a stack to store the nodes in the tree. In the worst case, the tree is skewed, and we have to store all nodes for each node.
# This iterative solution is optimal in terms of time and space complexity.

# Test Cases
# Test Case 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
target = 2
sol = Solution()
print(sol.removeLeafNodes(root, target))

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
target = 3
sol = Solution()
print(sol.removeLeafNodes(root, target))
