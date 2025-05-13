# Invert Binary Tree - LeetCode

## Problem Statement

Given the root of a binary tree, invert the tree and return its root.

### Example 1:

* **Input**: root = \[4,2,7,1,3,6,9]
* **Output**: \[4,7,2,9,6,3,1]

### Example 2:

* **Input**: root = \[2,1,3]
* **Output**: \[2,3,1]

### Example 3:

* **Input**: root = \[]
* **Output**: \[]

### Constraints

* The number of nodes in the tree is in the range \[0, 100].
* Node values range from -100 to 100.

---

## What is a Binary Tree?

A **binary tree** is a hierarchical data structure in which each node has at most two children: a left child and a right child. These trees are commonly used in various applications such as expression parsing, search algorithms, and decision trees.

The **Invert Binary Tree** problem requires swapping the left and right subtrees of every node in the tree recursively or iteratively.

---

## Solution 1: Depth-First Search (DFS) - Recursive Approach

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # base case: if the tree is empty, return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root  # return the root after inversion
```

### Explanation

* We check if the current node is `None`. If so, return `None`.
* Swap the left and right children of the current node.
* Recursively call the `invertTree` function for both left and right subtrees.

### Time and Space Complexity

* **Time Complexity**: O(n) — each node is visited exactly once.
* **Space Complexity**: O(h) — where h is the height of the tree (due to recursion stack).

  * Worst case (skewed tree): O(n)
  * Best case (balanced tree): O(log n)

---

## Solution 2: Breadth-First Search (BFS) - Iterative Approach

```python
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])  # initialize queue with root node
        while queue:
            node = queue.popleft()  # remove the front node

            # Swap the children
            node.left, node.right = node.right, node.left

            # Add children to queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
```

### Explanation

* This solution uses a queue to traverse the tree level by level (BFS).
* For each node, it swaps the children and enqueues the children if they exist.

### Time and Space Complexity

* **Time Complexity**: O(n) — all nodes are visited once.
* **Space Complexity**: O(n) — in the worst case, the queue holds all nodes at the deepest level.

---

## Comparison of DFS vs BFS

| Feature               | DFS (Recursive)              | BFS (Iterative)                |
| --------------------- | ---------------------------- | ------------------------------ |
| Approach              | Top-down (Depth-first)       | Level-by-level (Breadth-first) |
| Space Usage           | O(h)                         | O(n)                           |
| Uses                  | Recursion stack              | Queue                          |
| Ease of Understanding | More intuitive for recursion | Better for iterative control   |

### Most Optimal Solution

* Both solutions have **O(n)** time complexity.
* The **DFS recursive** solution is usually considered more elegant and concise.
* If recursion depth is not a problem (i.e., for balanced trees or small depth), DFS is optimal in terms of readability and slightly better space efficiency in average cases.

---

## Conclusion

The Invert Binary Tree problem is a classic example of binary tree manipulation and recursion. Both DFS and BFS approaches solve the problem efficiently with O(n) time complexity.
