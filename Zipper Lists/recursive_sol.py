# Zipper lists

# Recursive Solution

class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  next_1 = head_1.next
  next_2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1  


# Time Complexity:
# n = length of list 1
# m = length of list 2
# Time: O(min(n, m))
# Space: O(min(n, m))


# Test Cases

# Test Case 1
a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z

# Test Case 2
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

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z -> d -> e -> f

# Test Case 3
s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

print(zipper_lists(s, one))
# s -> 1 -> t -> 2 -> 3 -> 4

# Test Case 4
w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 

print(zipper_lists(w, one))
# w -> 1 -> 2 -> 3


# Test Case 5
one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 

w = Node("w")
# w

print(zipper_lists(one, w))
# 1 -> w -> 2 -> 3

