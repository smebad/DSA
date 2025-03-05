# Reverse List

## Problem Statement
The **reverse_list** function takes in the head of a singly linked list as an argument. The function reverses the order of the nodes **in-place** and returns the new head of the reversed linked list.

## Solutions Used
Two solutions are implemented to solve this problem:

### 1. Iterative Solution
In this approach:
- We use two pointers: `prev` (initially `None`) and `current` (starting from `head`).
- We traverse the list while updating the `next` pointer of each node to point to the previous node.
- The loop continues until we reach the end of the list.
- Finally, we return `prev`, which becomes the new head of the reversed list.

#### **Time Complexity**:
- **O(n)**: We traverse the list once, processing each node in constant time.
- **Space Complexity**: **O(1)**: No extra space is used apart from pointers.

#### **Code**:
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev
```

---

### 2. Recursive Solution
In this approach:
- We recursively traverse to the end of the linked list.
- Once we reach the last node, we start updating the `next` pointers to reverse the links.
- The recursive function keeps track of the previous node as it unwinds back to the original head.
- Finally, we return the last node as the new head of the reversed list.

#### **Time Complexity**:
- **O(n)**: We visit each node once.
- **Space Complexity**: **O(n)**: Each recursive call adds a new stack frame, leading to a linear space requirement.

#### **Code**:
```python
class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def reverse_list(head, prev=None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
```

## Differences in Time Complexity
| Solution    | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| Iterative  | O(n)            | O(1)             |
| Recursive  | O(n)            | O(n)             |

## Conclusion
- The **iterative approach** is more efficient in terms of space and should be preferred for large linked lists.
- The **recursive approach** provides a cleaner and more elegant solution but uses extra memory due to recursion.

Both methods effectively reverse the linked list, and the choice depends on the specific constraints of the problem.

