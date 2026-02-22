# linked list find
# recursive Solution

class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)



# Time Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(n)


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

print(linked_list_find(a, "c")) # True

# Test Case 2
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "d")) # True


# Test Case 3
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "q")) # False


# Test Case 4
node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

print(linked_list_find(node1, "jason")) # True


# Test Case 5
node1 = Node(42)

# 42

print(linked_list_find(node1, 42)) # True


# Test Case 6
node1 = Node(42)

# 42

print(linked_list_find(node1, 100)) # False
