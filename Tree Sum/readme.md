# Tree Sum

## Problem Statement
Write a function, `tree_sum`, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

## What is a Binary Tree?
A binary tree is a hierarchical data structure in which each node has at most two children: a left child and a right child. Each node contains a value, and the entire tree is defined by its root node.

## What is Tree Sum?
Tree sum is a problem where we traverse a binary tree and sum up all the values present in its nodes. This can be done using different traversal techniques such as depth-first search (DFS) and breadth-first search (BFS).

## Solutions
We have implemented two solutions to solve this problem:

### 1. Depth-First Search (DFS) Solution
In the DFS approach, we traverse the tree recursively and sum up the values. We visit the root first, then recursively process the left subtree, followed by the right subtree.

#### **Implementation:**
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_sum(root):
  if root is None:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)
```

#### **Time Complexity:**
- **Time Complexity:** O(n), where *n* is the number of nodes in the tree. Each node is visited once.
- **Space Complexity:** O(n) in the worst case (for a skewed tree, where the recursive call stack grows to *n*).

### 2. Breadth-First Search (BFS) Solution
In the BFS approach, we use a queue to process nodes level by level. We add the values of all nodes while traversing the tree in a breadth-first manner.

#### **Implementation:**
```python
from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_sum(root):
  if not root:
    return 0

  queue = deque([ root ])
  total_sum = 0
  while queue:
    node = queue.popleft()
    total_sum += node.val
    
    if node.left:
      queue.append(node.left)
    
    if node.right:
      queue.append(node.right)

  return total_sum
```

#### **Time Complexity:**
- **Time Complexity:** O(n), as each node is visited once.
- **Space Complexity:** O(n), as in the worst case, the queue will store all nodes at the largest level of the tree.

## Differences Between DFS and BFS Approaches
| Approach | Time Complexity | Space Complexity | When to Use |
|----------|---------------|----------------|--------------|
| **DFS (Recursive)** | O(n) | O(n) (worst case recursion depth) | When recursion is preferred and tree depth is manageable |
| **BFS (Iterative)** | O(n) | O(n) (queue size for largest level) | When you need level-order processing or avoid deep recursion |

## Example Test Cases
```python
# Test Case 1:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a)) # -> 21

# Test Case 2:
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum(a)) # -> 10

# Test Case 3:
print(tree_sum(None)) # -> 0
```

## Conclusion
Both DFS and BFS provide efficient ways to compute the sum of a binary tree. The DFS approach uses recursion and requires additional space in the call stack, while BFS uses an explicit queue but has the same time complexity. Choosing between them depends on the use case and the structure of the tree.