# reverse list
# recursive solution

class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)


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
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a)) # f -> e -> d -> c -> b -> a

# Test Case 2
x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(reverse_list(x)) # y -> x

# Test Case 3
p = Node("p")

# p

print(reverse_list(p)) # p

