# Subtree of Another Tree - LeetCode

## Problem Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the **same structure and node values** of `subRoot`, and `false` otherwise.

A **subtree** of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Examples

**Example 1:**

* Input:

  ```
  root = [3,4,5,1,2]
  subRoot = [4,1,2]
  ```
* Output: `true`

**Example 2:**

* Input:

  ```
  root = [3,4,5,1,2,null,null,null,null,0]
  subRoot = [4,1,2]
  ```
* Output: `false`

## Constraints

* The number of nodes in the `root` tree is in the range \[1, 2000].
* The number of nodes in the `subRoot` tree is in the range \[1, 1000].
* -10^4 <= node.val <= 10^4

---

## Python Code with Explanation

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: if subRoot is None, it is trivially a subtree
        if not subRoot:
            return True
        # If root is None but subRoot isn't, subRoot can't be a subtree
        if not root:
            return False

        # Check if the trees match at the current node
        if self.sameTree(root, subRoot):
            return True

        # Otherwise, check the left and right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both trees are empty
        if not root and not subRoot:
            return True
        # Both trees are non-empty and root values match
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        # Trees do not match
        return False
```

---

## Solution Explanation

### Approach: Depth-First Search (DFS)

* Traverse each node of the `root` tree.
* At each node, check if the subtree starting from that node is **identical** to `subRoot` using a helper function `sameTree`.
* `sameTree` recursively checks if both the structure and values of the trees are identical.
* If a match is found, return `True`. Otherwise, recursively check the left and right subtrees.

### Logic

* Every node in `root` is a potential starting point of a subtree.
* `sameTree` performs a recursive deep comparison between `root` and `subRoot`.
* If any such node's subtree matches exactly with `subRoot`, we return `True`.

---

## Time and Space Complexity

### Time Complexity:

* **O(m \* n)**

  * Let `m` be the number of nodes in `root` and `n` be the number in `subRoot`.
  * In the worst case, each node of `root` is compared with the entire `subRoot` using `sameTree`.
  * `sameTree` itself takes O(n) time in the worst case.

### Space Complexity:

* **O(m + n)** in the worst case due to recursive call stack usage.

  * The recursion depth can go as deep as the height of the trees in the worst scenario.

---

## Optimality of the Solution

* The DFS-based solution is optimal in simplicity and clarity.
* There exist advanced approaches like **tree hashing** or **tree serialization + string matching (e.g., KMP)**, which may reduce redundant checks.
* But for most cases within constraints (m <= 2000), the DFS approach is efficient and easy to implement.

---

## Summary

* This problem is about checking whether a smaller tree (`subRoot`) is embedded entirely inside another tree (`root`).
* The solution uses recursive DFS to traverse and compare trees node by node.
* The time and space complexities are acceptable for the given input constraints, and this problem enhances your understanding of tree traversal and comparison logic.

---

## Test Cases

```python
# Test Case 1
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(Solution().isSubtree(root, subRoot))  # True

# Test Case 2
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(0)  # extra node causes mismatch

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(Solution().isSubtree(root, subRoot))  # False
```
