# Maximum Depth of Binary Tree - LeetCode

## Problem Statement

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

### Example 1:

**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `3`

### Example 2:

**Input:** `root = [1,null,2]`
**Output:** `2`

---

### Constraints:

* The number of nodes in the tree is in the range `[0, 10^4]`
* `-100 <= Node.val <= 100`

---

## What is Maximum Depth of a Binary Tree?

The **maximum depth** of a binary tree is the length of the longest path from the root to any leaf. Each node along that path counts as one depth level.

---

## Solution 1: Recursive DFS (Depth-First Search)

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Recursively find the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The maximum depth is the greater of the two plus one (for the current node)
        return 1 + max(left_depth, right_depth)
```

### Explanation:

* **Base Case:** If the node is `None`, the depth is 0.
* **Recursive Step:** Call `maxDepth()` on left and right children.
* Return `1 + max(left_depth, right_depth)`.

### Time Complexity: `O(n)`

* We visit every node exactly once.

### Space Complexity: `O(h)`

* `h` is the height of the tree.
* Worst case (unbalanced tree): `O(n)`
* Best case (balanced tree): `O(log n)`

---

## Solution 2: Iterative DFS Using Stack

```python
class IterativeDFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Stack stores pairs of (node, depth)
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                # Update result if current depth is greater
                res = max(res, depth)
                # Add left and right children to the stack with incremented depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
```

### Explanation:

* Use a stack to keep track of nodes and their depth.
* At each step, pop from the stack and update the maximum depth.
* Push left and right children with incremented depth.

### Time Complexity: `O(n)`

* We visit every node once.

### Space Complexity: `O(n)`

* Stack could hold all nodes in worst case.

---

## Solution 3: Iterative BFS Using Queue

```python
from collections import deque

class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        # Initialize the queue with the root node if it exists
        if root:
            q.append(root)

        level = 0
        # Process each level in the queue
        while q:
            # Process all nodes at the current level
            for i in range(len(q)):
                node = q.popleft()
                # Enqueue children for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Increment level after processing all nodes at current depth
            level += 1
        return level
```

### Explanation:

* Use a queue (`deque`) to process nodes level by level.
* Increment `level` after processing each level.
* The final `level` value is the max depth.

### Time Complexity: `O(n)`

* Each node is visited once.

### Space Complexity: `O(n)`

* In worst case, all nodes at one level are in the queue.

---

## Comparing Solutions:

| Solution      | Approach    | Time Complexity | Space Complexity | Pros                                    | Cons                          |
| ------------- | ----------- | --------------- | ---------------- | --------------------------------------- | ----------------------------- |
| Recursive DFS | Top-down    | `O(n)`          | `O(h)`           | Simple, elegant, easy to implement      | Stack overflow for deep trees |
| Iterative DFS | Stack-based | `O(n)`          | `O(n)`           | No recursion depth issues               | Stack grows with tree depth   |
| Iterative BFS | Level-order | `O(n)`          | `O(n)`           | Best for measuring depth level by level | Slightly more complex to code |

---

## Most Optimal Approach:

**All three approaches have `O(n)` time complexity.**

* However, for **very deep or unbalanced trees**, iterative methods (either DFS or BFS) are more optimal in practice due to avoiding recursion limits.
* **BFS** is particularly intuitive for depth problems as it processes nodes level by level.

---

## Test Case Utility Function:

```python
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
```

---

## Example Test Cases:

```python
test_cases = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2)
]

for values, expected_depth in test_cases:
    root = create_tree(values)
    solution = Solution()
    depth = solution.maxDepth(root)
    assert depth == expected_depth, f"Expected {expected_depth}, but got {depth} for input {values}"
    print(f"Test case {values} passed with depth {depth}.")
```