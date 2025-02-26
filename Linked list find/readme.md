# Linked List Find

## Overview
The `linked_list_find` function determines whether a target value exists in a given singly linked list. The function returns `True` if the value is found and `False` otherwise.

We implemented two solutions:
1. **Iterative Approach**
2. **Recursive Approach**

## What is Linked List Find?
A linked list is a data structure where elements (nodes) are connected sequentially through pointers. Searching for a value in a linked list involves traversing through nodes to check if the target value exists.

## Iterative Solution
### Approach
- Start at the `head` of the linked list.
- Traverse each node while checking if its value matches the `target`.
- If found, return `True`; otherwise, continue traversing.
- If the end of the list is reached without finding the target, return `False`.

### Implementation
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False
```

### Time and Space Complexity
- **Time Complexity**: `O(n)` (where `n` is the number of nodes, as each node is visited once).
- **Space Complexity**: `O(1)` (since only a constant amount of extra space is used).

## Recursive Solution
### Approach
- Base case: If `head` is `None`, return `False` (end of the list).
- If `head.val` matches the `target`, return `True`.
- Otherwise, recursively check the next node.

### Implementation
```python
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
```

### Time and Space Complexity
- **Time Complexity**: `O(n)` (since each node is checked once).
- **Space Complexity**: `O(n)` (due to recursive call stack usage).

## Why Use Two Solutions?
- The **iterative solution** is more space-efficient (`O(1)`) as it does not require extra stack space.
- The **recursive solution** is simpler and more readable but uses `O(n)` space due to function call stack overhead.

## Conclusion
The iterative approach is preferable for large linked lists due to its `O(1)` space complexity. However, the recursive approach is more concise and can be easier to understand for small datasets.

Both implementations efficiently determine if a given value exists within a linked list.