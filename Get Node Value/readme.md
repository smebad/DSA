# Get Node Value

## Problem Statement
The **get_node_value** function takes in the head of a singly linked list and an index. The function returns the value of the node at the specified index in the linked list. If there is no node at the given index, the function returns `None`.

## Solutions Used
Two solutions are implemented to solve this problem:

### 1. Iterative Solution
In this approach:
- We traverse the linked list using a loop while maintaining a count of nodes.
- If the count matches the given index, we return the value of that node.
- If we reach the end of the list without finding the index, we return `None`.

#### **Time Complexity**:
- **O(n)**: In the worst case, we iterate through all `n` nodes.
- **Space Complexity**: **O(1)**: We only use a few extra variables for tracking the index.

#### **Code**:
```python
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
```

---

### 2. Recursive Solution
In this approach:
- We use recursion to traverse the linked list.
- If the index is 0, we return the current node's value.
- Otherwise, we recursively call the function on the next node with the index decremented by 1.

#### **Time Complexity**:
- **O(n)**: The recursion may go through all `n` nodes in the worst case.
- **Space Complexity**: **O(n)**: Since each recursive call adds a new stack frame, the space complexity is linear.

#### **Code**:
```python
def get_node_value(head, index):
  if head is None: 
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index - 1)
```

## Differences in Time Complexity
| Solution    | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| Iterative  | O(n)            | O(1)             |
| Recursive  | O(n)            | O(n)             |

## Conclusion
- The **iterative approach** is more space-efficient and should be preferred for large inputs.
- The **recursive approach** has a cleaner implementation but consumes more memory due to recursive calls.

Both methods solve the problem efficiently, and the choice depends on the constraints of the system.

