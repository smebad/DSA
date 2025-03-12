# tree min value
# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.


# Breadth First Solution (Iterative):
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None
from collections import deque

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



# Time Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(n)


# Test Cases:
# Test Case 1
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
print(tree_min_value(a)) # -> -2

# Test Case 2
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

print(tree_min_value(a)) # -> 3

# Test Case 3
a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
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
# -3   -4   -13
#     /       \
#    -2       -2

print(tree_min_value(a)) # -> -13

# Test Case 4
a = Node(42)

#        42

print(tree_min_value(a)) # -> 42
