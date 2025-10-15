# Populating Next Right Pointers in Each Node
# Breadth-First Search solution:
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
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left

        return root
    
# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(1), since we are using only a constant amount of extra space.
# This breadth-first search approach efficiently connects the next pointers in a perfect binary tree.


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
