# Binary Tree Preorder Traversal - LeetCode

## Problem Description

The **Binary Tree Preorder Traversal** problem requires you to traverse a binary tree using the preorder method and return the values of nodes in that order.

**Preorder traversal** visits the nodes in the following order:

1. Visit the root node
2. Traverse the left subtree
3. Traverse the right subtree

---

## Problem Statement

Given the root of a binary tree, return the preorder traversal of its nodes' values.

### Constraints:

* The number of nodes in the tree is in the range \[0, 100].
* Node values are in the range \[-100, 100].

### Example 1:

**Input:** root = \[1, null, 2, 3]
**Output:** \[1, 2, 3]

### Example 2:

**Input:** root = \[1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
**Output:** \[1, 2, 4, 5, 6, 7, 3, 8, 9]

---

## Recursive Solution Explanation

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return
            res.append(node.val)  # Visit the root node
            preorder(node.left)  # Recursively traverse left subtree
            preorder(node.right)  # Recursively traverse right subtree

        preorder(root)
        return res
```

### Logic:

* Start at the root.
* Add the root's value to the result list.
* Recursively do the same for the left subtree, then the right subtree.

---

## Iterative Solution Explanation

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res, stack = [], [root]

        while stack:
            node = stack.pop()
            res.append(node.val)  # Visit the node
            if node.right:
                stack.append(node.right)  # Right child is pushed first
            if node.left:
                stack.append(node.left)   # So that left is processed first

        return res
```

### Logic:

* Use a stack to mimic recursion.
* Push right child before left child so left is processed first.
* Continue until the stack is empty.

---

## Differences Between Recursive and Iterative Approaches

| Aspect      | Recursive                | Iterative                         |
| ----------- | ------------------------ | --------------------------------- |
| Method      | Uses function call stack | Uses explicit stack               |
| Simplicity  | Easier to read and write | More control over traversal       |
| Stack Usage | Implicit via recursion   | Explicit via list/stack structure |

---

## Time and Space Complexities

### Recursive Solution:

* **Time Complexity:** O(n) — Every node is visited once.
* **Space Complexity:** O(h) — `h` is the tree height. Worst-case: O(n) (skewed), best-case: O(log n) (balanced).

### Iterative Solution:

* **Time Complexity:** O(n) — Every node is pushed and popped once.
* **Space Complexity:** O(n) — Stack may hold all nodes in worst case.

---

## Most Optimal Solution

Both solutions have the same time complexity, but the **iterative approach** is considered more robust because it avoids stack overflow issues in very deep trees and gives finer control over the traversal order.

---

## Sample Test Cases

```python
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(Solution().preorderTraversal(root1))  # Output: [1, 2, 3]

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)
print(Solution().preorderTraversal(root2))  # Output: [1, 2, 4, 5, 3, 6, 7]

# Test Case 3:
print(Solution().preorderTraversal(None))  # Output: []

# Test Case 4:
root4 = TreeNode(1)
print(Solution().preorderTraversal(root4))  # Output: [1]
```
