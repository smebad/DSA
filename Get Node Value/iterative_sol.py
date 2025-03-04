# get node value
# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# iterative solution

class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if count == index:
      return current.val
    
    current = current.next
    count += 1
    
  return None

# Time Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(1)


# Test Cases
# Test Case 1
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'

# Test Case 2
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 3)) # 'd'

# Test Case 3
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 7)) # None

# Test Case 4
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

print(get_node_value(node1, 0)) # 'banana'


# Test Case 5
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

print(get_node_value(node1, 1)) # 'mango'




