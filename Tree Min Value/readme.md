# Tree Min Value

## Problem Statement
Write a function, `tree_min_value`, that takes in the root of a binary tree containing number values. The function should return the minimum value within the tree.

**Assumption:** The input tree is non-empty.

---
## Solutions
### 1. Depth First Search (Recursive)
#### Explanation
- This approach uses recursion to traverse the tree.
- It recursively finds the smallest value in the left and right subtrees and compares them with the current node value.
- The base case returns `float("inf")` for `None` nodes.

#### Code
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_min_value(root):
  if root is None:
    return float("inf")
  smallest_left_value = tree_min_value(root.left)
  smallest_right_value = tree_min_value(root.right)
  return min(root.val, smallest_left_value, smallest_right_value)
```

#### Time Complexity
- **Time:** O(n) – Every node is visited once.
- **Space:** O(n) – In the worst case (skewed tree), the recursive stack could store up to `n` calls.

---
### 2. Depth First Search (Iterative)
#### Explanation
- This approach uses a stack to perform an iterative depth-first traversal.
- It keeps track of the smallest value encountered while traversing.

#### Code
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None
     
def tree_min_value(root):
  stack = [ root ]
  smallest = float("inf")
  while stack:
    current = stack.pop()
    if current.val < smallest:
      smallest = current.val

    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)

  return smallest
```

#### Time Complexity
- **Time:** O(n) – Every node is visited once.
- **Space:** O(n) – In the worst case, the stack could hold up to `n` nodes.

---
### 3. Breadth First Search (Iterative)
#### Explanation
- This approach uses a queue to perform a level-order (BFS) traversal.
- It keeps track of the smallest value encountered while visiting each node.

#### Code
```python
from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_min_value(root):
  queue = deque([ root ])
  smallest = float("inf")
  while queue:
    current = queue.popleft()
    if current.val < smallest:
      smallest = current.val

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return smallest
```

#### Time Complexity
- **Time:** O(n) – Every node is visited once.
- **Space:** O(n) – In the worst case, the queue could store up to `n` nodes.

---
## Summary
| Solution | Approach | Time Complexity | Space Complexity |
|----------|----------|----------------|-----------------|
| **DFS (Recursive)** | Recursion | O(n) | O(n) |
| **DFS (Iterative)** | Stack-based traversal | O(n) | O(n) |
| **BFS (Iterative)** | Queue-based traversal | O(n) | O(n) |

Each approach efficiently finds the minimum value in a binary tree, and the choice depends on the problem constraints and memory limitations.

