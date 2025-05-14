# Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# Recursive Depth-First Search (DFS) Solution:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(n), where n is the number of nodes in the tree. In the worst case, the stack can hold all nodes if the tree is completely unbalanced.
# The solution uses an iterative depth-first search (DFS) approach with a stack to traverse the binary tree. The stack is initialized with the root node and its depth (1). For each node, if it is not None, we update the maximum depth (res) and push its left and right children onto the stack with their respective depths (depth + 1). The process continues until the stack is empty, at which point we return the maximum depth found.
# This iterative approach avoids the potential issues of recursion depth limits in Python, especially for large trees. It is efficient and works well for large trees, as it only traverses each node once and uses a stack to keep track of the nodes and their depths.

# Test Cases:
# Helper function to create a binary tree from a list of values
def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test cases
test_cases = [
    ([3, 9, 20, None, None, 15, 7], 3),  # Example 1
    ([1, None, 2], 2)]                   # Example 2


for values, expected_depth in test_cases:
    root = create_tree(values)
    solution = Solution()
    depth = solution.maxDepth(root)
    assert depth == expected_depth, f"Expected {expected_depth}, but got {depth} for input {values}"
    print(f"Test case {values} passed with depth {depth}.")