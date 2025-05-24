# Count Good Nodes in Binary Tree - LeetCode

## Problem Explanation

In a binary tree, a node **X** is called a "good node" if no node on the path from the **root** to **X** has a value **greater** than **X**. In other words, the node's value must be greater than or equal to all the node values encountered along the path from the root to that node.

### Examples:

**Example 1:**
Input: `root = [3,1,4,3,null,1,5]`
Output: `4`
Explanation: Nodes 3 (root), 4, 5, and the left 3 are good nodes.

**Example 2:**
Input: `root = [3,3,null,4,2]`
Output: `3`

**Example 3:**
Input: `root = [1]`
Output: `1`

## Code Explanation (with Comments)

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Helper function for Depth First Search (DFS)
        def dfs(node, maxVal):
            if not node:
                return 0

            # Count this node as good if its value is >= max value seen so far
            res = 1 if node.val >= maxVal else 0

            # Update max value for the path to child nodes
            maxVal = max(maxVal, node.val)

            # Recursively check left and right subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        # Initial call to DFS with root value as initial max
        return dfs(root, root.val)
```

## Solution Approaches

### 1. Depth-First Search (DFS)

This is a recursive approach where we pass down the maximum value seen so far as we traverse the tree. At each node, we check if it qualifies as a "good node" and update the count accordingly.

### 2. Breadth-First Search (BFS)

```python
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        # Start with root node and initial max value
        q.append((root, -float('inf')))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            # Add children to queue with updated max value
            if node.left:
                q.append((node.left, max(maxval, node.val)))
            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res
```

## Time and Space Complexities

### Depth-First Search (DFS)

* **Time Complexity:** `O(n)`, where `n` is the number of nodes. Each node is visited once.
* **Space Complexity:** `O(h)`, where `h` is the height of the tree (recursion stack). In worst-case skewed trees, this is `O(n)`, and in balanced trees it's `O(log n)`.

### Breadth-First Search (BFS)

* **Time Complexity:** `O(n)` — each node is visited exactly once.
* **Space Complexity:** `O(n)` in the worst case due to storing nodes in the queue.

## Most Optimal Solution

The **DFS solution** is typically considered more optimal **in terms of space** because:

* It avoids extra data structures like a queue.
* It leverages the call stack and uses less memory in balanced trees.
* Simpler and more elegant implementation for recursive traversal.

Thus, for memory-constrained environments or balanced binary trees, **DFS** is preferred over BFS.

## Summary

* The goal is to count how many nodes are "good" based on values along the root-to-node path.
* Both DFS and BFS can solve the problem efficiently.
* DFS has lower space overhead in balanced trees, making it the most optimal approach in practice.
