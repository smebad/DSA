# Minimum Distance Between BST Nodes - LeetCode

## Problem Statement

The problem "Minimum Distance Between BST Nodes" requires finding the minimum difference between the values of any two distinct nodes in a Binary Search Tree (BST).

* **Input:** A BST represented by its root node.
* **Output:** An integer representing the minimum absolute difference between any two node values in the BST.

### Example 1

```
Input: root = [4,2,6,1,3]
Output: 1
```

Explanation: The minimum difference is between nodes 2 and 3 or nodes 1 and 2.

### Example 2

```
Input: root = [1,0,48,null,null,12,49]
Output: 1
```

Explanation: The minimum difference is between nodes 48 and 49 or nodes 0 and 1.

### Constraints

* The number of nodes in the tree is in the range [2, 100].
* 0 <= Node.val <= 10^5

## Solution Explanation

The provided code uses an **inorder traversal** of the BST to solve the problem efficiently.

### Code with Comments

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")  # prev stores the previous node in inorder, res stores minimum difference

        def dfs(node):
            nonlocal prev, res
            if not node:
                return

            # Traverse left subtree
            dfs(node.left)

            # Compute difference with previous node if it exists
            if prev:
                res = min(res, node.val - prev.val)

            # Update previous node
            prev = node

            # Traverse right subtree
            dfs(node.right)

        dfs(root)
        return res
```

### Approach and Logic

1. **Inorder Traversal:** In a BST, inorder traversal gives nodes in ascending order. Therefore, the minimum difference must occur between consecutive nodes in this order.
2. **Track Previous Node:** Keep track of the previously visited node (`prev`) and calculate the difference with the current node.
3. **Update Minimum:** Update the minimum difference (`res`) whenever a smaller difference is found.
4. **Return Result:** After traversing all nodes, return the minimum difference.

**Why it works:**

* Since the BST is ordered, consecutive values in inorder traversal are the closest numerically.
* Comparing only consecutive nodes ensures we find the smallest possible difference.

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the number of nodes. Each node is visited once.
* **Space Complexity:** O(h), where h is the height of the tree due to recursion stack. In the worst case (skewed tree), h = n.

**Optimality:**

* This is optimal because we visit each node only once and compute the difference during traversal without extra passes.

## Test Cases

```python
if __name__ == "__main__":
    sol = Solution()

    # Helper function to insert nodes in BST
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Test Case 1
    root1 = None
    for val in [4, 2, 6, 1, 3]:
        root1 = insert_into_bst(root1, val)
    print(sol.minDiffInBST(root1))  # Output: 1

    # Test Case 2
    root2 = None
    for val in [1, 0, 48, 12, 49]:
        root2 = insert_into_bst(root2, val)
    print(sol.minDiffInBST(root2))  # Output: 1

```
