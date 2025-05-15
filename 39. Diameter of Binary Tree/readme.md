# Diameter of Binary Tree - LeetCode

## Problem Description

Given the `root` of a binary tree, return the **length of the diameter** of the tree.

The **diameter** of a binary tree is the length of the **longest path between any two nodes** in a tree. This path **may or may not pass through the root**. The length of a path is the number of **edges** between the two nodes.

### Examples

#### Example 1:

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: Longest path is [4,2,1,3] or [5,2,1,3].
```

#### Example 2:

```
Input: root = [1,2]
Output: 1
```

## Constraints

* The number of nodes in the tree is in the range \[1, 10^4]
* -100 <= Node.val <= 100

---

## Solution: Depth-First Search (DFS) Recursive Approach

### Code

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This variable will store the final diameter result
        res = 0

        # Depth-first search function to calculate height and update diameter
        def dfs(root):
            nonlocal res  # allow access to the 'res' variable from the outer function

            if not root:
                return 0  # base case: null node contributes 0 to height

            # Recursively find the height of the left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the diameter if the path through this node is longer
            res = max(res, left + right)

            # Return the height of the tree rooted at this node
            return 1 + max(left, right)

        dfs(root)  # start DFS from the root
        return res
```

### Explanation

* We perform a depth-first search to compute the height of each subtree.
* While returning from each call, we compute the potential diameter at that node as the sum of the left and right subtree heights.
* The global `res` variable keeps track of the maximum diameter found so far.
* This solution efficiently traverses each node only once.

---

## Time and Space Complexity

### Time Complexity

* **O(n)** — where `n` is the number of nodes in the tree. Each node is visited exactly once.

### Space Complexity

* **O(h)** — where `h` is the height of the tree. This is the space used by the recursion stack.

  * **Best Case (Balanced Tree)**: O(log n)
  * **Worst Case (Skewed Tree)**: O(n)
---

## Test Cases

```python
# Helper function to create a binary tree from a list
def create_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 3),  # Longest path: 4-2-1-3 or 5-2-1-3
    ([1, 2], 1),           # Only one edge between 1 and 2
    ([1], 0),              # Single node has diameter 0
    ([1, None, 2], 1),     # Right-skewed tree
    ([1, 2, None], 1),     # Left-skewed tree
]

for nodes, expected_diameter in test_cases:
    root = create_tree(nodes)
    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)
    assert diameter == expected_diameter, f"Test failed for {nodes}: expected {expected_diameter}, got {diameter}"
    print(f"Test passed for {nodes}: diameter is {diameter}")
```
