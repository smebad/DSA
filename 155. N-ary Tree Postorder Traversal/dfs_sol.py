# N-ary Tree Postorder Traversal
# Depth-First Search Solution:
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
      self.val = val
      self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)
            res.append(node.val)

        dfs(root)
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(n) in the worst case, which occurs when the tree is completely unbalanced (e.g., a linked list). In the average case, the space complexity is O(h), where h is the height of the tree, due to the recursion stack.
# This dfs solution effectively captures the postorder traversal of an n-ary tree by recursively visiting all children of a node before appending the node's value to the result list.


# Test Cases:
# Helper function to create an n-ary tree from a list of values
def create_nary_tree(values):
    if not values:
        return None

    root = Node(values[0], [])
    queue = [root]
    i = 2  # Start from the second element after the root and null

    while i < len(values):
        current = queue.pop(0)
        while i < len(values) and values[i] is not None:
            child = Node(values[i], [])
            current.children.append(child)
            queue.append(child)
            i += 1
        i += 1  # Skip the null separator

    return root

# Test case 1
root1 = create_nary_tree([1, None, 3, 2, 4, None, 5, 6])
solution = Solution()
result1 = solution.postorder(root1)
print(result1)  # Output: [5, 6, 3, 2, 4, 1]

# Test case 2
root2 = create_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
result2 = solution.postorder(root2)
print(result2)  # Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
