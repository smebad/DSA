# Breadth-First Values (Binary Tree Traversal)

## Overview
This repository contains a Python implementation of breadth-first traversal for a binary tree. The function `breadth_first_values` takes the root of a binary tree as input and returns a list of all values in breadth-first order.

## What is Breadth-First Traversal?
Breadth-first traversal (also called **level-order traversal**) explores all nodes of a binary tree **level by level** from left to right before moving to the next level. This approach ensures that nodes closer to the root are visited first.

### Example:
Given the following binary tree:
```
     a
    / \
   b   c
  / \   \
 d   e   f
```
A breadth-first traversal would return:
```
['a', 'b', 'c', 'd', 'e', 'f']
```

## Implementation
The `breadth_first_values` function is implemented using a **queue (FIFO structure)** to process each node level by level.

### Solution (Iterative Approach using a Queue)
```python
from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def breadth_first_values(root):
  if not root:
    return []
  
  queue = deque([ root ])
  values = []
  
  while queue:
    node = queue.popleft()
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values
```

### Explanation:
1. **Queue Initialization:** Start with a queue containing the root node.
2. **Processing Nodes:** Pop a node from the queue, add its value to the result list.
3. **Adding Children:** If the node has left or right children, enqueue them.
4. **Continue Until Empty:** Repeat until the queue is empty.

## Time and Space Complexity
- **Time Complexity:** `O(n)` because we visit each node once.
- **Space Complexity:** `O(n)` in the worst case, where all nodes are stored in the queue (e.g., a full binary tree).

## Test Cases
### Example 1:
```python
# Constructing the binary tree
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(breadth_first_values(a))  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
```

### Edge Cases:
- **Single Node Tree:**
  ```python
  a = Node('a')
  print(breadth_first_values(a))  # Output: ['a']
  ```
- **Empty Tree:**
  ```python
  print(breadth_first_values(None))  # Output: []
  ```

## Summary
- **Breadth-first traversal** visits nodes level by level.
- The **queue-based approach** ensures `O(n)` time complexity.
- Efficient for processing trees in a **structured order** (e.g., shortest path problems).