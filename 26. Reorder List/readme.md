# Reorder Linked List - LeetCode

## Problem Statement
You are given the head of a singly linked list. The list can be represented as:

```
L0 → L1 → ... → Ln - 1 → Ln
```

Reorder the list to be in the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → ...
```

You may not modify the values in the list's nodes. Only the nodes themselves may be changed.

## Examples

**Example 1:**
- Input: `head = [1,2,3,4]`
- Output: `1 -> 4 -> 2 -> 3 -> None`

**Example 2:**
- Input: `head = [1,2,3,4,5]`
- Output: `1 -> 5 -> 2 -> 4 -> 3 -> None`

## Brute Force Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Store all nodes in a list for index access
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # Reorder the list using two pointers from front and back
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]  # Link front node to back node
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]  # Link back node to next front node
            j -= 1

        # End the list
        nodes[i].next = None
```

### Time and Space Complexity
- **Time Complexity:** O(n) for traversing the list and rearranging it.
- **Space Complexity:** O(n) due to storing nodes in a list.

This method is easier to understand but not optimal in terms of space usage.

## Optimal Reverse and Merge Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Use slow and fast pointers to find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second = slow.next
        prev = slow.next = None  # Disconnect the first half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second  # Link node from first half to one from reversed second half
            second.next = tmp1   # Connect node from second half to next node from first half
            first, second = tmp1, tmp2
```

### Time and Space Complexity
- **Time Complexity:** O(n)
  - One pass to find the middle
  - One pass to reverse second half
  - One pass to merge two halves
- **Space Complexity:** O(1)
  - No extra data structures used; rearrangement is done inplace

This approach is optimal for both time and space and is the preferred solution for interviews and production-level problems.

## Summary
- **Brute Force:** Easy to implement, uses extra memory.
- **Reverse and Merge (Optimal):** Efficient in both time and space, uses pointer manipulation effectively.

This problem is a good example of how linked list manipulation can benefit from two pointer techniques and inplace operations.

