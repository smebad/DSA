# Populating Next Right Pointers in Each Node
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000
 

# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.


# Depth-First Search solution:
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(log n) due to the recursion stack in a balanced binary tree. In the worst case, the height of the tree is log n.
# This depth-first search approach efficiently connects the next pointers in a perfect binary tree.


# Test Cases:
def print_tree_with_next_pointers(root: 'Optional[Node]'):
    if not root:
        return "[]"
    
    result = []
    level_start = root
    while level_start:
        current = level_start
        level_nodes = []
        while current:
            level_nodes.append(str(current.val))
            current = current.next
        result.append("->".join(level_nodes) + "->#")
        level_start = level_start.left
    return "[" + ",".join(result) + "]"

# Test case 1:
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
solution = Solution()
result1 = solution.connect(root1)
print(print_tree_with_next_pointers(result1))  # Output: [1,#,2,3,#,4,5,6,7,#]

# Test case 2:
root2 = None
solution = Solution()
result2 = solution.connect(root2)
print(print_tree_with_next_pointers(result2))  # Output: []