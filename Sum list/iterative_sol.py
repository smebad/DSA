# sum list
# iterative solution
# Define the Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(head):
  total_sum = 0

  current = head
  while current is not None:
    total_sum += current.val
    current = current.next



  return total_sum

# n = number of nodes
# Time: O(n)
# Space: O(1)


# test cases
# Test Case 1
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19

# Test Case 2
x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

print(sum_list(x)) # 42

# Test Case 3
z = Node(100)

# 100

print(sum_list(z)) # 100

# Test Case 4
print(sum_list(None)) # 0

