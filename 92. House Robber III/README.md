# House Robber III - LeetCode

## Problem Statement

The thief has discovered a new neighborhood where the houses are arranged in the form of a **binary tree**. Each house has a certain amount of money. However, if the thief robs two **directly connected houses** (a parent and one of its children), an alarm will be triggered.

Given the `root` of the binary tree, return the **maximum amount of money** the thief can rob **without alerting the police**.

### Example 1:

```
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Rob 3 (root), 3 (left.right), and 1 (right.right)
```

### Example 2:

```
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Rob 4 (left), and 5 (right)
```

### Constraints

* The number of nodes is in the range \[1, 10^4].
* 0 <= Node.val <= 10^4

---

## Recursive Solution (Brute Force)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # No money from an empty node

        res = root.val  # Rob current node

        # Add values from grandchildren if available
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)

        # Compare with skipping current node and robbing its children
        res = max(res, self.rob(root.left) + self.rob(root.right))
        return res
```

### Explanation of the Approach

* For each node, the algorithm decides:

  1. Rob the current house (skip its children).
  2. Skip the current house (consider the best outcome of robbing its children).
* It computes both cases and takes the maximum.
* This approach works well for small trees but becomes inefficient as the tree grows.

### Time and Space Complexity

* **Time Complexity:** O(2^n), where n is the number of nodes. The algorithm explores every combination (rob or skip) recursively.
* **Space Complexity:** O(n), for the maximum depth of the recursion stack in a skewed tree.

---

## Dynamic Programming Solution (Optimized)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [0, 0]  # [max_if_robbed, max_if_skipped]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # Rob current node: cannot rob its children
            withRoot = root.val + leftPair[1] + rightPair[1]
            # Skip current node: take max of robbing or not robbing children
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]

        return max(dfs(root))
```

### Explanation of the Approach

* Each `dfs(node)` returns two values:

  * `withRoot`: maximum amount when robbing the current node
  * `withoutRoot`: maximum amount when skipping the current node
* At each node, we calculate both options based on its children’s values and propagate them up.
* No values are recomputed, making it highly efficient.

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the number of nodes. Every node is visited exactly once.
* **Space Complexity:** O(n), for recursion stack in the worst case (skewed tree).

---

## Comparison Between Recursive and DP Solutions

| Aspect           | Recursive (Brute Force) | Dynamic Programming (Optimized) |
| ---------------- | ----------------------- | ------------------------------- |
| Time Complexity  | O(2^n)                  | O(n)                            |
| Space Complexity | O(n)                    | O(n)                            |
| Recomputations   | Yes                     | No                              |
| Suitable for     | Small trees             | Large trees                     |
| Optimal          | No                      | Yes                             |

### Why the DP Solution Is Optimal

* It eliminates redundant calculations by storing results for subproblems.
* By returning both rob and skip values at each node, it makes decisions efficiently at every level.
* It ensures every node contributes to the overall maximum only once.

---

## Summary

* House Robber III is an extension of the classic House Robber problem to binary trees.
* The brute force recursive method considers all possible rob/skip combinations, leading to exponential time.
* The dynamic programming solution improves this drastically by avoiding redundant calculations.
* The DP approach is optimal and should be preferred for solving this problem efficiently.
