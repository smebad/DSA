# depth first values
# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.


# Iterative Solution
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None


def depth_first_values(root):
  if not root:
    return []
  
  stack = [root]
  values = []
  
  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values


# Time Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(n)


# Test Cases:
# Test Case 1:
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

# Test Case 2:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']


# Test Case 3:
a = Node('a')
#     a
print(depth_first_values(a)) 
#   -> ['a']

# Test Case 4:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

print(depth_first_values(a)) 
#   -> ['a', 'b', 'c', 'd', 'e']


# Test Case 5:
print(depth_first_values(None)) 
#   -> []
