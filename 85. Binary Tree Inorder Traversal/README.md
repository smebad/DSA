# Binary Tree Inorder Traversal - LeetCode

## Problem Description

Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal is a method where for each node:

1. Traverse the left subtree
2. Visit the node
3. Traverse the right subtree

This problem tests your understanding of tree traversal, recursion, and stack-based iteration.

### Examples:

* **Input:** `[1,null,2,3]`
  **Output:** `[1,3,2]`

* **Input:** `[1,2,3,4,5,null,8,null,null,6,7,9]`
  **Output:** `[4,2,6,5,7,1,3,9,8]`

* **Input:** `[]`
  **Output:** `[]`

* **Input:** `[1]`
  **Output:** `[1]`

### Constraints:

* The number of nodes in the tree is in the range \[0, 100].
* Node values range between -100 and 100.

---

## Recursive DFS Solution

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Traverse left subtree
            res.append(node.val)  # Visit the node
            inorder(node.right)  # Traverse right subtree
        
        inorder(root)
        return res
```

### Explanation:

* This uses recursion to visit left subtree, node, and then right subtree.
* A helper function `inorder` does the recursive work.

### Time and Space Complexity:

* **Time Complexity:** O(n), where n is the number of nodes.
* **Space Complexity:** O(n) in worst case due to recursion stack (skewed tree), O(log n) for balanced.

---

## Iterative DFS Solution

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
```

### Explanation:

* This mimics recursion using a stack.
* It manually manages traversal through left children, then visits nodes and moves to right.

### Time and Space Complexity:

* **Time Complexity:** O(n)
* **Space Complexity:** O(n) due to the stack

---

## Comparison & Optimality

| Solution Type | Time Complexity | Space Complexity | Notes                                       |
| ------------- | --------------- | ---------------- | ------------------------------------------- |
| Recursive     | O(n)            | O(n)             | Simpler, less control over call stack       |
| Iterative     | O(n)            | O(n)             | More explicit, avoids recursion depth limit |

* Both are optimal in terms of time.
* Iterative method is often preferred in production where stack overflow is a concern.

---

## Test Cases

```python
# Test Case 1:
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(Solution().inorderTraversal(root1)) # [1, 3, 2]

# Test Case 2:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(6)
print(Solution().inorderTraversal(root2)) # [4, 2, 5, 1, 6, 3]

# Test Case 3:
root3 = None
print(Solution().inorderTraversal(root3)) # []
```