# Max Root to Leaf Path Sum

## Problem Statement
The **Max Root to Leaf Path Sum** problem involves finding the maximum sum of any root-to-leaf path in a binary tree. A root-to-leaf path is a sequence of nodes starting from the root and ending at a leaf (a node with no children). The goal is to compute the maximum possible sum obtained by traversing any such path.

You may assume that the input tree is non-empty.

## Solution Explanation
To solve this problem, we use a **recursive Depth-First Search (DFS) approach**.

### **Recursive Depth-First Search Solution**
1. **Base Case**: If the current node is `None`, return negative infinity (`float("-inf")`) to ensure it is not considered in the maximum path sum.
2. **Leaf Node Case**: If the node has no children (i.e., it's a leaf), return its value since it represents a complete root-to-leaf path.
3. **Recursive Case**: Compute the maximum path sum for both left and right subtrees. The result for the current node is its value plus the maximum of the two subtree sums.

### **Python Implementation**
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def max_path_sum(root):
  if root is None:
    return float("-inf")

  if root.left is None and root.right is None:
    return root.val

  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
```

### **Time Complexity Analysis**
- **Time Complexity: O(n)**
  - Since we visit each node once, the time complexity is **O(n)**, where **n** is the number of nodes in the tree.
- **Space Complexity: O(n)**
  - In the worst case (a skewed tree), the recursive call stack can go up to **O(n)** depth.

## Test Cases
### **Test Case 1**
```python
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

print(max_path_sum(a)) # -> 18
```

### **Test Case 2**
```python
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \      
# 20   15
#      / \
#     1   3

print(max_path_sum(a)) # -> 59
```

### **Test Case 3**
```python
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2

print(max_path_sum(a)) # -> -8
```

### **Test Case 4**
```python
a = Node(42)

#        42

print(max_path_sum(a)) # -> 42
```