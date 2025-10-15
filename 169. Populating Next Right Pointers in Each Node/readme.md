# Populating Next Right Pointers in Each Node - LeetCode

## Problem statement

You are given a **perfect binary tree**, meaning all interior nodes have exactly two children, and all leaves are on the same level. Each node has a `next` pointer that should point to its immediate right neighbor in the same level. If there is no right neighbor, the pointer should be set to `NULL`.

Initially, all `next` pointers are `NULL`.

**Definition:**

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
};
```

### Examples

**Example 1**

```
Input:  root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
```

Explanation: The tree is perfect, so every node's `next` pointer is set to its right neighbor. The `#` symbol represents the end of each level.

**Example 2**

```
Input: root = []
Output: []
```

### Constraints

* Number of nodes: `[0, 2^12 - 1]`
* Node values: `[-1000, 1000]`

### Follow-up

* You may only use **constant extra space**.
* Recursive solutions are acceptable because implicit stack space does not count as extra space.

---

## Intuition

The goal is to connect every node’s `next` pointer to its right neighbor in the same level. Since the tree is **perfect**, we can always connect:

* `left.next = right`
* `right.next = next.left` (if `next` exists)

We can solve this using **Depth-First Search (DFS)** recursion or **Breadth-First Search (BFS)** iteration.

---

### Depth-First Search (Recursive Solution)

```python
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
        # Base case: if tree is empty, return None
        if not root:
            return root

        # If the current node has a left child, connect its children
        if root.left:
            # Connect left child to right child
            root.left.next = root.right

            # If root has a next, connect right child to next's left child
            if root.next:
                root.right.next = root.next.left

            # Recursively connect left and right subtrees
            self.connect(root.left)
            self.connect(root.right)

        # Return the root node after all connections
        return root
```

### Breadth-First Search (Iterative Solution)

```python
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
        # Start from the root level
        cur, nxt = root, root.left if root else None

        # Loop through all levels
        while cur and nxt:
            # Connect left -> right for the current node
            cur.left.next = cur.right

            # Connect right -> next.left if a next node exists
            if cur.next:
                cur.right.next = cur.next.left

            # Move to the next node in the current level
            cur = cur.next

            # If we reach the end of the current level, go to the next level
            if not cur:
                cur = nxt
                nxt = cur.left

        return root
```

---

## Step-by-step Explanation of Approaches

### 1. Recursive (DFS) Approach

1. Start from the root node.
2. If a node has children, connect:

   * `left.next = right`
   * If `node.next` exists, then `right.next = node.next.left`.
3. Recursively perform these steps for the left and right subtrees.

This approach leverages the recursive call stack to traverse the tree in a pre-order manner. Because the tree is **perfect**, the left and right children always exist for each internal node.

### 2. Iterative (BFS) Approach

1. Use two pointers, `cur` (current node) and `nxt` (the first node of the next level).
2. While `cur` and `nxt` exist:

   * Connect `cur.left.next = cur.right`.
   * If `cur.next` exists, connect `cur.right.next = cur.next.left`.
   * Move `cur` to `cur.next` (next node in the same level).
   * When the end of a level is reached (`cur == None`), move to the next level (`cur = nxt`).

This version iterates through the tree using only pointers and avoids recursion entirely.

---

## Key Differences Between Solutions

| Feature              | Recursive (DFS)                    | Iterative (BFS)                              |
| -------------------- | ---------------------------------- | -------------------------------------------- |
| **Approach Type**    | Top-down recursion                 | Level-order traversal using pointers         |
| **Space Complexity** | O(log n) (recursion stack)         | O(1) (constant extra space)                  |
| **Readability**      | Easier to understand conceptually  | Slightly more complex pointer handling       |
| **Performance**      | Similar O(n)                       | Similar O(n) but uses less memory            |
| **Use Case**         | Great for clarity or smaller trees | Best for large trees and strict space limits |

---

## Time and Space Complexity Analysis

### Time Complexity

Both solutions visit each node once.

* **Time Complexity:** `O(n)` for both DFS and BFS, where `n` is the number of nodes in the tree.

### Space Complexity

* **Recursive DFS:** `O(log n)` for recursion stack (height of a perfect binary tree is `log n`).
* **Iterative BFS:** `O(1)` constant space, because we only use a few pointers (`cur`, `nxt`).

### Optimal Solution

The **iterative BFS** version is the most optimal one:

* Same `O(n)` time as DFS.
* But only **constant** `O(1)` extra space.
* Avoids recursion stack usage and is suitable for large trees.

---

## Example Visualization

For the tree:

```
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

After populating `next` pointers:

```
        1 -> NULL
      /   \
     2 -> 3 -> NULL
    / \   / \
   4->5->6->7 -> NULL
```

---

## Test Cases

```python
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

# Test Case 1:
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
solution = Solution()
result1 = solution.connect(root1)
print(print_tree_with_next_pointers(result1))  # Output: [1->#,2->3->#,4->5->6->7->#]

# Test Case 2:
root2 = None
solution = Solution()
result2 = solution.connect(root2)
print(print_tree_with_next_pointers(result2))  # Output: []
```