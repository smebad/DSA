# Balanced Binary Tree - LeetCode

## Problem Statement

Given a binary tree, determine if it is height-balanced.

A **balanced binary tree** is defined as a binary tree in which the depth of the two subtrees of *every* node never differs by more than one.

---

## Problem Example

### Example 1:

**Input:** `[3,9,20,null,null,15,7]`
**Output:** `true`

### Example 2:

**Input:** `[1,2,2,3,3,null,null,4,4]`
**Output:** `false`

### Example 3:

**Input:** `[]`
**Output:** `true`

---

## Constraints

* The number of nodes in the tree is in the range `[0, 5000]`
* `-10^4 <= Node.val <= 10^4`

---

## Brute Force Solution

This solution checks if the binary tree is height-balanced by recursively calculating the height of each subtree.

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # Get the height of left and right subtrees
        left = self.height(root.left)
        right = self.height(root.right)

        # If the absolute difference is greater than 1, it's unbalanced
        if abs(left - right) > 1:
            return False

        # Check recursively if left and right subtrees are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        # Base case: height of empty tree is 0
        if not root:
            return 0

        # Height = 1 + max height of left or right subtree
        return 1 + max(self.height(root.left), self.height(root.right))
```

### Time Complexity:

* **O(n²)** in the worst case (when the tree is skewed)
* For every node, you compute the height of its left and right subtrees.

### Space Complexity:

* **O(h)** for the recursion stack (where `h` is the height of the tree)

---

## Optimal One-Pass DFS Solution

This optimized approach checks for balance and computes height in a single DFS traversal.

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Base case: An empty tree is balanced with height 0
            if not root:
                return [True, 0]

            # Recursively check left and right subtrees
            left, right = dfs(root.left), dfs(root.right)

            # A node is balanced if both children are balanced and height difference is <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Height of current node is 1 + max height of left or right subtree
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
```

### Time Complexity:

* **O(n)** where `n` is the number of nodes — every node is visited exactly once.

### Space Complexity:

* **O(h)** where `h` is the height of the tree due to recursion stack.

---

## Optimal vs Brute Force

| Approach     | Time Complexity | Space Complexity | Remarks                             |
| ------------ | --------------- | ---------------- | ----------------------------------- |
| Brute Force  | O(n²)           | O(h)             | Recalculates heights multiple times |
| One-Pass DFS | O(n)            | O(h)             | Efficient — calculates once         |

**The one-pass DFS solution is the most optimal** because it avoids redundant height calculations by checking balance and height in one traversal.

---

## Test Cases

```python
# Test Case 1:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().isBalanced(root)) # True

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(Solution().isBalanced(root)) # False

# Test Case 3:
root = None
print(Solution().isBalanced(root)) # True
```