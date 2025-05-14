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
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case, the tree is completely unbalanced and h = n, leading to O(n) space. In the best case, the tree is balanced and h = log(n), leading to O(log(n)) space.
# The solution uses a recursive depth-first search (DFS) approach to traverse the binary tree.
# The base case is when the root is None, in which case the maximum depth is 0.
# For each non-null node, the function recursively calculates the maximum depth of the left and right subtrees and returns 1 plus the maximum of those two depths.
# The function is called on the root node, and the result is returned.
# However, the solution does not handle the case where the input tree is empty (i.e., root is None) explicitly. In such cases, it will return 0 as expected since the base case checks for None.
# The solution is efficient and works well for large trees, as it only traverses each node once and uses a simple recursive approach.


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