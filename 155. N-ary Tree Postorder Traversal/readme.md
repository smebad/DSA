# N-ary Tree Postorder Traversal - LeetCode

## Problem Explanation

The problem "N-ary Tree Postorder Traversal" asks us to perform a **postorder traversal** of an **N-ary tree**. In an N-ary tree, each node can have multiple children (not just two as in a binary tree).

**Postorder traversal** means:

1. Traverse all children of the node first.
2. Visit the current node last.

So for each node, we visit its children in order, and then record the node's own value.

### Example

* Input: `root = [1,null,3,2,4,null,5,6]`
* Output: `[5,6,3,2,4,1]`

Explanation:

* Start at the root (1). First, traverse its children `3,2,4`.
* For node `3`, traverse its children `5,6` before visiting `3`.
* Then traverse `2`, then `4`.
* Finally, visit root `1`.

---

## Code with Comments

```python
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
      self.val = val
      self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []  # This will store the final traversal result

        def dfs(node):
            if not node:
                return  # Base case: if node is None, do nothing

            # Recursively visit all children first
            for child in node.children:
                dfs(child)

            # After visiting children, add the node value
            res.append(node.val)

        dfs(root)  # Start DFS from the root
        return res
```

---

## Approach and Logic

### Recursive DFS Approach

1. Use a recursive **Depth-First Search (DFS)** function.
2. For each node:

   * Traverse all its children first (recursively).
   * Append the node's value after processing its children.
3. Return the result list containing the traversal order.

### Why this works

* Postorder requires children before the parent. DFS naturally fits this requirement.
* By visiting all children first and then appending the parent, the correct order is achieved.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * Each node is visited exactly once, where `n` is the number of nodes.

* **Space Complexity:**

  * Worst case: `O(n)` if the tree is very skewed (like a linked list).
  * Average case: `O(h)` where `h` is the height of the tree due to recursion stack.

### Optimal Solution

The recursive DFS solution is optimal:

* Traverses each node once in `O(n)`.
* Uses only the recursion stack, so extra memory overhead is minimal.

---

## Test Cases

```python
# Helper function to create an n-ary tree from a list of values
def create_nary_tree(values):
    if not values:
        return None

    root = Node(values[0], [])
    queue = [root]
    i = 2  # Start after root and first null

    while i < len(values):
        current = queue.pop(0)
        while i < len(values) and values[i] is not None:
            child = Node(values[i], [])
            current.children.append(child)
            queue.append(child)
            i += 1
        i += 1  # Skip null separator

    return root

solution = Solution()

# Test Case 1
root1 = create_nary_tree([1, None, 3, 2, 4, None, 5, 6])
print(solution.postorder(root1))  # Output: [5, 6, 3, 2, 4, 1]

# Test Case 2
root2 = create_nary_tree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
print(solution.postorder(root2))  # Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
```