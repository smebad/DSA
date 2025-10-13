# Range Sum of BST - LeetCode

## Problem - What is "Range Sum of BST"?

Given the root of a binary **search** tree (BST) and two integers `low` and `high`, return the sum of values of all nodes with a value in the inclusive range `[low, high]`.

Because the input is a **BST**, for any node:

* all values in the left subtree are less than the node's value,
* all values in the right subtree are greater than the node's value.

The goal: traverse the tree and add up only those node values that fall between `low` and `high` (inclusive).

---

## Code with comments

Below is the exact DFS solution you provided, annotated with comments so you can remember the logic later.

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case: empty subtree contributes 0 to the sum
        if not root:
            return 0

        # If current node's value is inside [low, high], include it; otherwise add 0
        res = root.val if low <= root.val <= high else 0

        # Recurse into left and right subtrees and add their contributions
        # (this version does not prune using BST properties)
        res += self.rangeSumBST(root.left, low, high)
        res += self.rangeSumBST(root.right, low, high)

        return res
```

Notes on the annotated lines:

* `if not root: return 0` — standard base case for recursion.
* `res = root.val if low <= root.val <= high else 0` — counts current node only if it falls in range.
* The two recursive calls add sums from left and right subtrees.

---

## Approaches, logic, and differences (explained simply)

### DFS solution and its Time & Space Complexity

**Idea:** visit every node, check if it's in the range and add it.

* Logic: unconditional recursion into both left and right children for every node.
* Pros: extremely simple to write and reason about.
* Cons: visits all nodes even when many nodes are outside the range — not taking advantage of BST ordering.

* **Time complexity:** O(n) in the worst case — it visits every node.
* **Space complexity:** O(h) due to recursion stack, where `h` is the tree height. Worst case O(n) for skewed trees, O(log n) for balanced trees.

---

## Test cases

```python
# Test Case 1:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

sol = Solution()
print(sol.rangeSumBST(root, 7, 15))  # 32

# Test Case 2:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(6)
print(sol.rangeSumBST(root, 6, 10))  # 23
```