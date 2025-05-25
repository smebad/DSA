# Validate Binary Search Tree - LeetCode

## Problem Description

Given the `root` of a binary tree, determine if it is a **valid binary search tree (BST)**.

A valid BST is defined as:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.

### Example 1:

Input: `root = [2,1,3]`
Output: `true`

### Example 2:

Input: `root = [5,1,4,null,null,3,6]`
Output: `false`
Explanation: The root node's value is 5 but its right child's value is 4, violating the BST property.

### Constraints:

* The number of nodes in the tree is in the range `[1, 10^4]`.
* `-2^31 <= Node.val <= 2^31 - 1`

---

## DFS Solution Explanation

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            # Check if current node's value is within the valid range
            if not (left < node.val < right):
                return False

            # Recursively validate left subtree and right subtree
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # Initialize the range with negative and positive infinity
        return valid(root, float("-inf"), float("inf"))
```

### Logic

This is a **Depth-First Search (DFS)** recursive approach where we pass down the valid range for each node based on its ancestors:

* For the left child: the upper bound becomes the current node's value.
* For the right child: the lower bound becomes the current node's value.
* If any node violates this range, we return `False`.

---

## BFS Solution Explanation

```python
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False

            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
```

### Logic

This is a **Breadth-First Search (BFS)** approach using a queue:

* Each node is dequeued along with its valid value range.
* If it violates the BST range, return `False`.
* Enqueue children with updated bounds accordingly.

---

## Differences Between DFS and BFS Approaches

| Aspect         | DFS                                  | BFS                                 |
| -------------- | ------------------------------------ | ----------------------------------- |
| Traversal      | Depth-first (recursion)              | Level-order (queue)                 |
| Space Usage    | O(h), h = height of tree             | O(n) in worst case                  |
| Implementation | Simpler recursive logic              | Uses explicit queue                 |
| Intuition      | Natural for tree validation problems | More general-purpose tree traversal |

---

## Time and Space Complexity

### Time Complexity (Both DFS and BFS):

* **O(n)**: Every node is visited exactly once.

### Space Complexity:

* **DFS**:

  * Best: O(log n) in balanced tree (recursion stack).
  * Worst: O(n) in skewed tree.
* **BFS**:

  * Always O(n) in worst-case scenario due to the queue holding many nodes at the same level.

---

## Optimal Solution

The **DFS recursive approach** is typically the most optimal in terms of space and readability:

* It uses only as much memory as needed for the height of the tree.
* It is easier to implement and reason about.
* Less overhead than maintaining a queue structure.

Choose the DFS method unless you have a specific reason to perform level-order traversal or require an iterative solution.

---

## Sample Test Cases

```python
# Test case 1:
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(Solution().isValidBST(root1))  # Output: True

# Test case 2:
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(Solution().isValidBST(root2))  # Output: False

# Test case 3:
root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(20)
print(Solution().isValidBST(root3))  # Output: False
```

---

## Summary

To validate a Binary Search Tree, recursively (DFS) or iteratively (BFS) check each node to ensure it fits within its expected value bounds, derived from its ancestors. The DFS method is optimal in both clarity and space for most practical cases.
