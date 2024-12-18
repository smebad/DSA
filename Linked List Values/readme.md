# Linked List Values

## Introduction
The **linked list values** problem involves extracting all the values from a linked list into a Python list. A linked list is a linear data structure where each element (node) points to the next, forming a chain-like structure. This README explains the problem, provides an overview of linked lists, and details both iterative and recursive solutions with their time and space complexities.

## What is a Linked List?
A linked list is a data structure consisting of nodes. Each node contains:
1. **Value (val):** The data stored in the node.
2. **Pointer (next):** A reference to the next node in the list (or `None` if it’s the last node).

### Types of Linked Lists:
- **Singly Linked List:** Each node points to the next node.
- **Doubly Linked List:** Each node points to both the next and previous nodes.

For this problem, we focus on **singly linked lists**.

### Example:
Consider the linked list:
`head -> a -> b -> c -> d -> None`

The function should return:
`["a", "b", "c", "d"]`

## Problem Statement
Write a function `linked_list_values` that takes the head of a linked list as input and returns a Python list containing all the values of the nodes in the linked list.

## Solutions

### Iterative Solution
The iterative approach traverses the linked list using a `while` loop and appends each node’s value to a result list.

#### Code:
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative Solution
def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values
```
### Time and Space Complexity:
* Time Complexity: O(n), where n is the number of nodes. Each node is visited once.
* Space Complexity: O(n), for the values list.

### Recursive Solution
The recursive approach uses a helper function to traverse the list. At each step, it adds the current node’s value to a result list.

#### Code:
```python
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
```
### Time and Space Complexity:
* Time Complexity: O(n), where n is the number of nodes. Each node is visited once.
* Space Complexity: O(n), due to the recursive call stack and the values list.

## Test Cases:

```python
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
```
---

## Conclusion
The `linked_list_values` problem demonstrates how to traverse a linked list and extract its values using two methods: iterative and recursive. Both solutions have the same time complexity (**O(n)**) but differ in their space complexity due to recursion.

Understanding these approaches is crucial for mastering linked list manipulation and problem-solving in data structures.
