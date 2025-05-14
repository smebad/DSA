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
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space Complexity: O(n), where n is the number of nodes in the tree. In the worst case, the queue can hold all nodes if the tree is completely unbalanced.
# The solution uses an iterative breadth-first search (BFS) approach with a queue to traverse the binary tree. The queue is initialized with the root node. For each level of the tree, we process all nodes at that level, adding their children to the queue for the next level. The process continues until the queue is empty, at which point we return the maximum depth found.
# What is queue or deque? A deque (double-ended queue) is a data structure that allows you to add and remove elements from both ends efficiently. In Python, the collections module provides a deque class that is optimized for fast appends and pops from both ends. It is often used in scenarios where you need to maintain a queue or stack-like behavior, such as in breadth-first search (BFS) algorithms.
# The solution is efficient and works well for large trees, as it only traverses each node once and uses a queue to keep track of the nodes at each level.
# Comparing all the solutions, the iterative BFS approach is generally more space-efficient than the recursive DFS approach, especially for large trees. The iterative BFS approach avoids the potential issues of recursion depth limits in Python, making it a safer choice for deep trees. However, both approaches have their own advantages and can be chosen based on the specific requirements of the problem.

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