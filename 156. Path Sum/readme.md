# Path Sum - LeetCode

## Problem Explanation

The **Path Sum** problem asks us to determine if there exists a **root-to-leaf path** in a given binary tree such that the sum of the node values along this path equals a given integer `targetSum`.

* A **leaf** is a node that has no left or right children.
* The task is to check all possible root-to-leaf paths and see if any of them add up exactly to `targetSum`.

### Example 1

Input: `root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22`
Output: `true`
Explanation: One valid path is `5 -> 4 -> 11 -> 2`, which sums to 22.

### Example 2

Input: `root = [1,2,3], targetSum = 5`
Output: `false`
Explanation: Possible paths are `1 -> 2` (sum = 3) and `1 -> 3` (sum = 4). Neither equals 5.

### Example 3

Input: `root = [], targetSum = 0`
Output: `false`
Explanation: The tree is empty, so no paths exist.

---

## Code with Comments

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:  # If we reach a null node, no path exists here
                return False

            curSum += node.val  # Add the current node value to the path sum

            # If we are at a leaf, check if the path sum equals targetSum
            if not node.left and not node.right:
                return curSum == targetSum

            # Recursively check left and right subtrees
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        # Start DFS from root with initial sum = 0
        return dfs(root, 0)
```

---

## Approach and Logic

The solution uses **Depth-First Search (DFS)** recursion:

1. Start at the root and keep a running sum (`curSum`).
2. At each node, add the node's value to the running sum.
3. If the node is a **leaf**, check if the running sum equals `targetSum`.
4. If not at a leaf, recursively explore the left and right children.
5. Return `True` if **any root-to-leaf path** matches the target, otherwise return `False`.

### Why DFS works well here

DFS ensures that we follow each possible root-to-leaf path completely before moving to the next one. Since the problem is specifically about root-to-leaf paths, DFS is a natural fit.

---

## Complexity Analysis

* **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree. We may need to visit every node once.
* **Space Complexity:**

  * Worst case: `O(n)` if the tree is skewed (like a linked list).
  * Average case: `O(h)` where `h` is the height of the tree, due to recursion stack.

### Optimality

The DFS recursive approach is optimal because:

* Every node must be checked at least once, so `O(n)` time is unavoidable.
* The recursion stack space is proportional to tree height, which is the best we can do without altering the traversal method.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.left = TreeNode(1)
targetSum1 = 22
print(sol.hasPathSum(root1, targetSum1))  # Output: True

# Test Case 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
targetSum2 = 5
print(sol.hasPathSum(root2, targetSum2))  # Output: False

# Test Case 3
root3 = None
targetSum3 = 0
print(sol.hasPathSum(root3, targetSum3))  # Output: False
```

---

## Summary

* The problem checks whether a root-to-leaf path adds up to a given sum.
* A recursive DFS solution is straightforward and efficient.
* Time complexity is `O(n)`, and space complexity is `O(h)`.
* This approach is optimal since we must check each node at least once.