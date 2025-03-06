# zipper lists
# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.


# Iterative Solution

class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1
    
  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2
    
  return head_1



# Time Complexity:
# n = length of list 1
# m = length of list 2
# Time: O(min(n, m))
# Space: O(1)


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

