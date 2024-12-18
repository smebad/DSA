# Define the Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Recursive Solution
def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)

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
print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]

# Test Case 2
x = Node("x")
y = Node("y")

x.next = y

# x -> y
print(linked_list_values(x)) # -> [ 'x', 'y' ]

# Test Case 3
q = Node("q")

# q
print(linked_list_values(q)) # -> [ 'q' ]

# Test Case 4
print(linked_list_values(None)) # -> []

# Time Complexity:
# n = number of nodes
# Time: O(n)
# Space: O(n)
