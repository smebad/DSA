# House Robber III - LeetCode

## Problem Statement

The thief has discovered a neighborhood structured as a **binary tree**, where each node represents a house with some amount of money. There's only one rule: **you cannot rob two directly-linked houses** (i.e., a parent and its child).

Given the root of the binary tree, determine the **maximum amount of money** the thief can rob without alerting the police.

### Example 1:

```
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Rob houses 3 + 3 + 1 = 7
```

### Example 2:

```
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Rob houses 4 + 5 = 9
```

## Constraints

* The number of nodes is in the range \[1, 10^4]
* 0 <= Node.val <= 10^4

---

## Recursive Solution (Brute Force)

### Python Code with Comments

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # If the node is None, there's nothing to rob

        # Rob current node, so skip its direct children
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)

        # Alternatively, don't rob current node, and rob its children
        res = max(res, self.rob(root.left) + self.rob(root.right))

        return res  # Return the best of the two options
```

### Approach and Explanation

* For each node, we have two choices:

  1. **Rob it**: We add its value and skip its immediate children.
  2. **Skip it**: We rob its children instead.
* The function recursively evaluates both scenarios and returns the maximum profit.
* This is a brute-force recursive method where each decision leads to more recursive calls.

### Time and Space Complexity

* **Time Complexity:** O(2^n), where n is the number of nodes. Every node may lead to two recursive branches (rob or not).
* **Space Complexity:** O(n), which is the depth of the recursion stack in the worst case (a skewed tree).

## Summary

* This problem asks us to maximize the loot from a binary tree under the constraint that we cannot rob directly connected houses.
* The provided solution explores both possibilities for each node—robbing it or skipping it—and recursively selects the better one.
* While the logic is sound and clear, this brute-force solution is inefficient for large trees due to repeated calculations.
