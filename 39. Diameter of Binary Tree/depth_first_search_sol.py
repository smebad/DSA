# Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100


# Depth-First Search (DFS) Solution:
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
    

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case, the tree is completely unbalanced and h = n, leading to O(n) space. In the best case, the tree is balanced and h = log(n), leading to O(log(n)) space.
# The solution uses a recursive depth-first search (DFS) approach to traverse the binary tree.
# Recursion is a common technique used in tree traversal, where the function calls itself on the left and right subtrees of the current node.
# However this solution does not use any additional data structures like stacks or queues, which are often used in iterative approaches to tree traversal.


# Test Cases:
# Helper function to create a binary tree
def create_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 3),  # Example 1
    ([1, 2], 1),           # Example 2
    ([1], 0),              # Single node
    ([1, None, 2], 1),     # Right skewed tree
    ([1, 2, None], 1),     # Left skewed tree
]

for nodes, expected_diameter in test_cases:
    root = create_tree(nodes)
    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)
    assert diameter == expected_diameter, f"Test failed for {nodes}: expected {expected_diameter}, got {diameter}"
    print(f"Test passed for {nodes}: diameter is {diameter}")