# Binary Tree Maximum Path Sum - LeetCode

## Problem Statement

In a binary tree, a **path** is a sequence of nodes where each pair of adjacent nodes is connected by an edge. A node may appear **only once** in a path, and the path does **not necessarily need to pass through the root**.

The **path sum** is the sum of all node values in the path. Given the root of a binary tree, the task is to return the **maximum path sum** among all possible paths in the tree.

### Example 1:

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

### Example 2:

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

### Constraints

* The number of nodes is in the range \[1, 3 \* 10^4].
* -1000 <= Node.val <= 1000

---

## Recursive Depth-First Search (DFS) Solution

### Python Code with Comments

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]  # Store the global max path sum

        def dfs(root):
            if not root:
                return 0  # No value to contribute if the node is None

            # Recursively calculate max path sum for left and right
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Only consider positive contributions
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update the result if the current path is better
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the best single path sum extending from this node
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
```

---

## Explanation of the Approach

* We use **post-order DFS** to explore all subtrees.
* At each node:

  * Compute the max path sum from the left and right children.
  * Ignore negative path sums since they would reduce the total.
  * Update the global result if the path through the current node (including both children) gives a higher sum.
  * Return the max sum of one side + current node to allow path continuation to the parent.
* This way, the algorithm always considers paths that start and end at any two nodes in the tree.

### Example Walkthrough

For the input tree:

```
       -10
      /    \
     9     20
          /  \
         15   7
```

* The path with the maximum sum is 15 -> 20 -> 7 = 42.

---

## Time and Space Complexity

* **Time Complexity:** O(n), where n is the number of nodes in the binary tree. Every node is visited exactly once.
* **Space Complexity:** O(n), due to the recursion stack in the worst-case (when the tree is skewed).

---

## Summary

* This problem asks for the highest sum among all paths in a binary tree.
* The recursive DFS approach calculates the best path sum for every subtree and updates a global result.
* Negative paths are discarded to maximize the result.
* The solution is optimal in both time and space complexity for this problem.
* Understanding how to use recursion to return values up the tree and track global state is essential for solving tree-based problems efficiently.