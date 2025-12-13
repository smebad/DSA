# Flip Equivalent Binary Trees - LeetCode

## Problem Explanation

The **Flip Equivalent Binary Trees** problem asks whether two binary trees can be made identical by performing any number of *flip operations*. A flip operation means choosing any node and swapping its left and right child subtrees.

Two trees are considered *flip equivalent* if, after applying zero or more such flips to one or both trees, their structures and node values become exactly the same.

### Key Points

* A flip can be performed at **any node**.
* Node values in each tree are **unique**.
* The trees may be empty.

The task is to determine whether two given binary trees are flip equivalent.

---

## Code Explanation

```python
class Solution:
    def flipEquiv(self, root1, root2):
        # If either tree is empty, both must be empty to be equivalent
        if not root1 or not root2:
            return not root1 and not root2

        # If the current node values are different, trees cannot be equivalent
        if root1.val != root2.val:
            return False

        # Case 1: Children match without flipping
        no_flip = (
            self.flipEquiv(root1.left, root2.left) and
            self.flipEquiv(root1.right, root2.right)
        )

        # Case 2: Children match after flipping
        flip = (
            self.flipEquiv(root1.left, root2.right) and
            self.flipEquiv(root1.right, root2.left)
        )

        # Trees are equivalent if either case works
        return no_flip or flip
```

---

## Approach and Logic

### Core Idea

At every node, there are **two valid ways** to compare subtrees:

1. Compare left with left and right with right (no flip).
2. Compare left with right and right with left (flip).

If either comparison succeeds, the trees can still be flip equivalent at that node.

### Step-by-Step Logic

1. **Base Case (Empty Trees)**

   * If both nodes are `None`, they are equivalent.
   * If only one is `None`, they are not equivalent.

2. **Value Check**

   * If the values of the current nodes differ, no sequence of flips can fix that.

3. **Recursive Comparison**

   * Check both non-flip and flip possibilities.
   * Use recursion to repeat the same logic for child subtrees.

4. **Final Decision**

   * If either configuration returns `True`, the trees are flip equivalent.

---

## Why This Solution Works

* Every flip operation only swaps left and right children.
* By checking both swapped and non-swapped cases at each node, we cover all possible flip combinations.
* The recursion naturally explores all valid configurations.

This ensures correctness without explicitly performing flips.

---

## Time and Space Complexity

### Time Complexity

* **O(n)**

Each node in both trees is visited once. Although two recursive calls are made at each step, they do not create extra work beyond visiting all nodes.

### Space Complexity

* **O(h)**

Where `h` is the height of the tree.

* Best case (balanced tree): `O(log n)`
* Worst case (skewed tree): `O(n)`

The space is used by the recursion call stack.

---

## Optimality Explanation

This depth-first search solution is optimal because:

* It avoids rebuilding or modifying the trees.
* It checks equivalence directly during traversal.
* No extra data structures are used.

Any correct solution must compare all nodes at least once, so **O(n)** time is the best possible complexity.

---

## Test Cases
```python
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)

    solution = Solution()
    print(solution.flipEquiv(root1, root2))  # Output: True

    # Test Case 2
    print(solution.flipEquiv(None, None))  # Output: True

    # Test Case 3
    print(solution.flipEquiv(None, TreeNode(1)))  # Output: False
```