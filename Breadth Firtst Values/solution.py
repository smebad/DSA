# breadth first values
# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

# Solution
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None


from collections import deque

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


# Time Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(n)


# Test Cases
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

print(breadth_first_values(a))
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

print(breadth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']


# Test Case 3:
a = Node('a')
#     a
print(breadth_first_values(a)) 
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

print(breadth_first_values(a)) 
#   -> ['a', 'b', 'c', 'd', 'e']


# Test Case 5:
print(breadth_first_values(None)) 
#   -> []
