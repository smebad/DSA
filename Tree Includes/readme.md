# Tree Includes

## Problem Statement
Write a function, `tree_includes`, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

## Solutions
This problem can be solved using two different approaches:
1. **Iterative solution using Breadth-First Search (BFS)**
2. **Recursive solution using Depth-First Search (DFS)**

---

## Iterative Solution (Breadth-First Search - BFS)
### Explanation
The BFS approach explores the tree level by level using a queue. It starts from the root node and moves to its children, then their children, and so on. If we find the target value at any node, we return `True`. Otherwise, if we traverse the entire tree without finding the target, we return `False`.

### Code:
```python
from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_includes(root, target):
  if not root:
    return False
  
  queue = deque([ root ])
  
  while queue:
    node = queue.popleft()
    
    if node.val == target:
      return True
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return False
```

### Time Complexity
- **O(n)**, where `n` is the number of nodes in the tree, since we visit each node once.
- **Space Complexity: O(n)**, as we may store up to `n` nodes in the queue in the worst case.

---

## Recursive Solution (Depth-First Search - DFS)
### Explanation
The DFS approach explores the tree by going as deep as possible along each branch before backtracking. We check if the current node matches the target. If not, we recursively search the left and right subtrees.

### Code:
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_includes(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)
```

### Time Complexity
- **O(n)**, since we may need to visit every node in the worst case.
- **Space Complexity: O(n)** in the worst case due to recursive function calls.

---

## Summary
| Approach | Time Complexity | Space Complexity |
|----------|---------------|-----------------|
| **BFS (Iterative)** | O(n) | O(n) |
| **DFS (Recursive)** | O(n) | O(n) |

Both solutions work efficiently for searching values in a binary tree, and the choice between BFS and DFS depends on the specific problem constraints and tree structure.