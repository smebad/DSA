# Kth Smallest Element in a Binary Search Tree (BST) - LeetCode

## Problem Statement

Given the `root` of a Binary Search Tree (BST) and an integer `k`, return the **kth smallest** value (1-indexed) among all the values of the nodes in the tree.

---

## What is "Kth Smallest Element in BST"?

A Binary Search Tree (BST) is a binary tree where, for each node:

* All values in the left subtree are **less than** the node's value.
* All values in the right subtree are **greater than** the node's value.

The in-order traversal of a BST yields values in **ascending order**. Therefore, the **kth smallest** element can be found by performing an in-order traversal and counting the visited nodes.

### Example 1:

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2:

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

---

## Iterative DFS Solution (Optimal)

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        # Iterative in-order traversal
        while stack or curr:
            # Traverse to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit the node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            # Move to the right subtree
            curr = curr.right
```

### How It Works:

* We perform an in-order traversal (Left -> Node -> Right) using a stack.
* We decrement `k` each time we visit a node.
* When `k == 0`, the current node is the kth smallest.

---

## Brute Force Solution

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        # Collect all node values using DFS
        def dfs(node):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        arr.sort()  # Sort the values to get ascending order
        return arr[k - 1]  # Return kth smallest (1-indexed)
```

### How It Works:

* Traverse the entire tree and store all node values in a list.
* Sort the list.
* Return the `k-1` indexed value from the sorted list.

---

## Solution Comparison and Analysis

| Approach      | Time Complexity | Space Complexity | Explanation                                                                             |
| ------------- | --------------- | ---------------- | --------------------------------------------------------------------------------------- |
| Iterative DFS | O(H + k)        | O(H)             | Most optimal. Traverses only up to kth node in in-order. `H` is height of the tree.     |
| Brute Force   | O(n log n)      | O(n)             | Simple but inefficient. Stores and sorts all node values. `n` is total number of nodes. |

### Most Optimal Solution: Iterative In-Order DFS

* **Why Optimal?**

  * BST in-order traversal gives sorted values.
  * We only visit `k` nodes in sorted order, which is efficient for large trees.
* **Space Efficiency:**

  * Uses a stack of size `O(H)` where `H` is the height of the tree.
  * In the worst case (skewed tree), H = n; in balanced trees, H = log(n).

---

## Constraints

* Number of nodes `n` in the tree: `1 <= k <= n <= 10^4`
* Node values: `0 <= Node.val <= 10^4`

---

## Summary

* Use **Iterative In-Order Traversal** for the most efficient solution.
* Brute force is easier to implement but not suitable for large datasets due to sorting.
* Understanding how in-order traversal works with BSTs is key to solving this problem efficiently.

---