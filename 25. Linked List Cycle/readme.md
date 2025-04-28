# Linked List Cycle - LeetCode

## Problem Explanation

The **Linked List Cycle** problem asks us to determine if a linked list contains a cycle.

A cycle occurs when a node's `next` pointer points back to a previous node instead of `None`, creating an infinite loop. Internally, an index `pos` is used to indicate the node where the tail connects back to, but it is not passed as a parameter to the function.

We must return:
- `True` if there is a cycle
- `False` if there is no cycle

---

## Example

- **Input:** head = [3, 2, 0, -4], pos = 1
- **Output:** true

Explanation: The tail connects to the node at index 1 (0-indexed).

- **Input:** head = [1, 2], pos = 0
- **Output:** true

- **Input:** head = [1], pos = -1
- **Output:** false

---

## Constraints
- Number of nodes is in the range \[0, 10⁴\].
- Node values are in the range \[-10⁵, 10⁵\].
- `pos` is either -1 or a valid index in the linked list.

---

# Solutions

## Hash Set Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()   # To keep track of visited nodes
        cur = head

        while cur:
            if cur in seen:
                return True  # Cycle detected
            seen.add(cur)
            cur = cur.next

        return False  # No cycle detected
```

### Step by Step Explanation
- We initialize an empty set `seen` to store visited nodes.
- We traverse the linked list node by node:
  - If a node has already been visited (present in `seen`), it means there is a cycle.
  - If the node is new, add it to the set.
  - Move to the next node.
- If we reach the end (`cur` becomes `None`), there is no cycle.

### Time and Space Complexity
- **Time Complexity:** \( O(n) \), where \( n \) is the number of nodes in the linked list. We visit each node once.
- **Space Complexity:** \( O(n) \), because we store each node in the hash set.

### When to Use
- This approach is simple and easy to implement.
- It is effective for small to medium-sized linked lists.
- Not optimal for memory usage in very large lists.

---

## Fast and Slow Pointers Solution (Floyd's Tortoise and Hare Algorithm)

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next       # Move slow pointer by 1
            fast = fast.next.next  # Move fast pointer by 2

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle detected
```

### Step by Step Explanation
- Initialize two pointers, `slow` and `fast`, both starting at the head.
- Move `slow` one step and `fast` two steps at a time.
- If there is no cycle, `fast` or `fast.next` will become `None`.
- If there is a cycle, `slow` and `fast` will eventually meet at some point inside the cycle.

### Time and Space Complexity
- **Time Complexity:** \( O(n) \), where \( n \) is the number of nodes.
- **Space Complexity:** \( O(1) \), as only two pointers are used.

### Why This is the Most Optimal Solution
- Uses constant memory \( O(1) \) making it suitable for large linked lists.
- Traverses each node at most a constant number of times.
- Slightly more complex to understand than the hash set method but extremely efficient.

### What is Floyd's Tortoise and Hare Algorithm?
- It is a pointer algorithm where one pointer moves twice as fast as the other.
- If a cycle exists, the faster pointer "laps" the slower pointer, causing them to meet.
- If no cycle exists, the faster pointer reaches the end of the list.

---

# Test Cases

Helper function to create a linked list with a cycle:

```python
def create_cycle_list(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    cur = head
    cycle_node = None

    for i in range(1, len(values)):
        cur.next = ListNode(values[i])
        cur = cur.next
        if i == pos:
            cycle_node = cur

    if cycle_node:
        cur.next = cycle_node  # Create a cycle

    return head
```

**Test Case 1: Cycle exists**
```python
head1 = create_cycle_list([3, 2, 0, -4], 1)
solution1 = Solution()
print(solution1.hasCycle(head1))  # Output: True
```

**Test Case 2: Cycle exists**
```python
head2 = create_cycle_list([1, 2], 0)
solution2 = Solution()
print(solution2.hasCycle(head2))  # Output: True
```

**Test Case 3: No cycle**
```python
head3 = create_cycle_list([1], -1)
solution3 = Solution()
print(solution3.hasCycle(head3))  # Output: False
```

---

# Conclusion

- The **hash set solution** is intuitive and simple but uses extra space.
- The **fast and slow pointers solution** (Floyd's Algorithm) is the most optimal, requiring only constant space.
- Understanding both methods is important as it allows selecting the best approach depending on the situation and constraints.

Both solutions provide \( O(n) \) time complexity, but for large scale applications, the fast and slow pointer approach is preferred due to its \( O(1) \) space efficiency.