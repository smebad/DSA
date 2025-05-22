# Binary Tree Right Side View - LeetCode

## Problem Statement

Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

### Example 1:

**Input:** `root = [1,2,3,null,5,null,4]`
**Output:** `[1,3,4]`

### Example 2:

**Input:** `root = [1,2,3,4,null,null,null,5]`
**Output:** `[1,3,4,5]`

### Example 3:

**Input:** `root = [1,null,3]`
**Output:** `[1,3]`

### Example 4:

**Input:** `root = []`
**Output:** `[]`

### Constraints:

* The number of nodes in the tree is in the range \[0, 100].
* -100 <= Node.val <= 100

---

## What is Binary Tree Right Side View?

The "Right Side View" of a binary tree shows only the nodes visible when looking at the tree from the right-hand side. At each level of the tree, only the rightmost node is visible and should be included in the output.

---

## BFS Solution (Breadth-First Search)

```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])  # Initialize a queue with the root node

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node  # The last node at each level will be the rightmost
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)  # Add the rightmost node's value to result
        return res
```

### BFS Approach Explanation:

* This solution uses a queue to perform level order traversal (breadth-first search).
* At each level, it tracks the rightmost node and adds it to the result.
* It appends children (left then right) to the queue for processing in the next level.

### Time and Space Complexity:

* **Time Complexity:** O(n), where n is the number of nodes in the tree. Every node is visited once.
* **Space Complexity:** O(n), due to the queue holding nodes at each level.

---

## DFS Solution (Depth-First Search)

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)  # First node encountered at this depth

            # Traverse right first to ensure rightmost node is recorded first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
```

### DFS Approach Explanation:

* This solution uses recursion to traverse the tree in a depth-first manner.
* It prioritizes right children so the first node encountered at each depth is the rightmost.
* Nodes are added to the result only if no value has been recorded for that depth.

### Time and Space Complexity:

* **Time Complexity:** O(n), where n is the number of nodes in the tree.
* **Space Complexity:** O(h), where h is the height of the tree due to recursion call stack. Worst case is O(n) for a skewed tree.

---

## Differences Between BFS and DFS Solutions

| Feature        | BFS                            | DFS                             |
| -------------- | ------------------------------ | ------------------------------- |
| Traversal      | Level by level                 | Depth-first (right first)       |
| Implementation | Uses a queue                   | Uses recursion                  |
| Order control  | Last node in level = rightmost | First node at depth = rightmost |
| Space usage    | Can grow with width of tree    | Can grow with height of tree    |

---

## Most Optimal Solution

Both BFS and DFS approaches have the same time complexity of O(n), but the **DFS solution is often considered more optimal in practice** for this problem because:

* It avoids using an explicit queue (uses call stack instead).
* Traverses the right subtree first, making it naturally aligned with the problem requirement.

However, BFS may be easier for beginners to understand as it directly mirrors the concept of processing nodes level by level.

---

## Summary to remember

* The goal is to collect the rightmost node at every level of a binary tree.
* Two main methods are BFS and DFS.
* Both are efficient with O(n) time complexity.
* DFS is elegant and concise for right-side view because it prioritizes the right child during traversal.
* Choose the approach that matches your comfort level and use case.
