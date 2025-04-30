# Remove Nth Node From End of List - LeetCode

## Problem Statement
Given the `head` of a singly linked list, remove the `n`th node from the end of the list and return its head.

### Example 1
**Input:** head = [1,2,3,4,5], n = 2  
**Output:** [1,2,3,5]

### Example 2
**Input:** head = [1], n = 1  
**Output:** []

### Example 3
**Input:** head = [1,2], n = 1  
**Output:** [1]

---

## Brute Force Solution

### Approach
1. Traverse the entire linked list and store each node in a list.
2. Find the index of the node to remove by calculating `len(nodes) - n`.
3. If the index is 0, return `head.next` (removing the first node).
4. Otherwise, update the previous node's `next` pointer to skip the target node.

### Code with Comments
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head

        # Store all nodes in a list
        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - n

        # If removing the head node
        if removeIndex == 0:
            return head.next

        # Re link previous node to skip the removed node
        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head
```

### Time and Space Complexity
- **Time Complexity:** O(N), where N is the number of nodes in the list.
- **Space Complexity:** O(N), due to storing all nodes in a list.

### Notes
- Simple and beginner-friendly.
- Not optimal due to extra space usage.

---

## Optimal Solution: Two Pointers

### Approach
1. Create a dummy node that points to the head (to simplify edge cases).
2. Use two pointers: `right` moves `n` steps ahead of `left`.
3. Move both pointers until `right` reaches the end of the list.
4. Remove the `n`th node from the end by updating `left.next`.

### Code with Comments
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Skip the nth node from the end
        left.next = left.next.next
        return dummy.next
```

### Time and Space Complexity
- **Time Complexity:** O(N), where N is the number of nodes in the list.
- **Space Complexity:** O(1), using constant extra space.

### Notes
- This is the **most optimal** solution.
- Efficient for large linked lists.
- Handles edge cases cleanly using a dummy node.

---

## Conclusion
- **Brute Force** is easier to understand but not space-efficient.
- **Two Pointers** is the optimal method, balancing both time and space complexity.
- Choosing the right method depends on the need for performance and simplicity.