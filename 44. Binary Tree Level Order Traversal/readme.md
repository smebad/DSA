# Binary Tree Level Order Traversal - LeetCode

## Problem Description

Given the root of a binary tree, return the level order traversal of its nodes' values. That means we need to return the values level by level from left to right.

## What is Level Order Traversal?

Level Order Traversal means visiting each node of the binary tree level by level, from top to bottom and from left to right at each level. This traversal is typically implemented using Breadth-First Search (BFS), but it can also be achieved using Depth-First Search (DFS) by keeping track of the depth.

## Examples

### Example 1:

Input: root = \[3,9,20,null,null,15,7]
Output: \[\[3],\[9,20],\[15,7]]

### Example 2:

Input: root = \[1]
Output: \[\[1]]

### Example 3:

Input: root = \[]
Output: \[]

## Constraints

* Number of nodes: 0 <= n <= 2000
* Node value range: -1000 <= Node.val <= 1000

## Breadth-First Search (BFS) Solution

```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Final result list to hold level-wise values
        q = deque()  # Queue for BFS traversal
        q.append(root)

        while q:
            qLen = len(q)  # Number of nodes in the current level
            level = []  # List to hold values of current level
            for i in range(qLen):
                node = q.popleft()  # Remove the front node
                if node:
                    level.append(node.val)  # Add its value to the level list
                    q.append(node.left)  # Add left child to queue
                    q.append(node.right)  # Add right child to queue
            if level:
                res.append(level)  # Add current level to result

        return res
```

### Time Complexity: O(n)

Each node is visited exactly once.

### Space Complexity: O(n)

In the worst case (when the tree is a complete binary tree), the queue can hold up to n nodes.

## Depth-First Search (DFS) Solution

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Final result list

        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append([])  # Create a new level
            res[depth].append(node.val)  # Add value to current level
            dfs(node.left, depth + 1)  # Recurse left with increased depth
            dfs(node.right, depth + 1)  # Recurse right with increased depth

        dfs(root, 0)
        return res
```

### Time Complexity: O(n)

Each node is visited once.

### Space Complexity: O(h) for recursion stack + O(n) for result

Where h is the height of the tree.

## BFS vs DFS: Key Differences

| Feature              | BFS                                     | DFS                          |
| -------------------- | --------------------------------------- | ---------------------------- |
| Traversal Order      | Level-by-level                          | Top-down using recursion     |
| Extra Data Structure | Queue (deque)                           | Recursion (call stack)       |
| Space Usage          | Can grow large if many nodes at a level | Depends on tree height       |
| Use Cases            | Level-order or shortest path problems   | Pre/in/post order traversals |

## Optimal Solution

Both solutions have the same time complexity of O(n), but BFS is considered the most intuitive and direct approach for level order traversal because it inherently operates level-by-level. DFS is elegant and can be preferred in some recursive designs, but may risk stack overflow in very deep trees.

## Test Cases

```python
# Test Case 1:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))  # [[3], [9, 20], [15, 7]]

# Test Case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().levelOrder(root))  # [[1], [2, 3], [4, 5]]

# Test Case 3:
root = None
print(Solution().levelOrder(root))  # []
```
