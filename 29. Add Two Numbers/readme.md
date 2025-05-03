# Add Two Numbers - LeetCode

## Problem Statement

You are given two non empty linked lists representing two non negative integers. The digits are stored in **reverse order**, and each of their nodes contains a **single digit**. Add the two numbers and return the **sum as a linked list**.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

### Example 1

**Input:**
l1 = \[2,4,3], l2 = \[5,6,4]
**Output:** \[7,0,8]
**Explanation:** 342 + 465 = 807

### Example 2

**Input:** l1 = \[0], l2 = \[0]
**Output:** \[0]

### Example 3

**Input:** l1 = \[9,9,9,9,9,9,9], l2 = \[9,9,9,9]
**Output:** \[8,9,9,9,0,0,0,1]

---

## Code Explanation (Iterative Approach)

```python
from typing import Optional

# Definition for singly linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # A dummy node to simplify handling the head of the result list
        cur = dummy         # Pointer to track the current node in the result list
        carry = 0           # Carry to handle sum > 9

        # Traverse both lists until both are exhausted and no carry remains
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0  # Get value from l1, or 0 if l1 is exhausted
            v2 = l2.val if l2 else 0  # Get value from l2, or 0 if l2 is exhausted

            val = v1 + v2 + carry     # Sum of two digits and carry
            carry = val // 10         # Update carry
            val = val % 10            # Get current digit

            cur.next = ListNode(val)  # Add this digit as a node to the result list
            cur = cur.next            # Move to the next node

            # Move input pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return the next node of dummy, which is the actual head
```

---

## Time and Space Complexity

### Time Complexity: **O(m + n)**

* `m` is the length of the first linked list.
* `n` is the length of the second linked list.
* We traverse each node of both lists exactly once.

### Space Complexity: **O(1)** (excluding output)

* No extra space is used apart from the result list.
* If we **include the output linked list**, space is **O(max(m, n))**.

---

## Why This Is Optimal

This solution is optimal because:

* It uses a single pass through both lists.
* It avoids recursion (which can have stack overflow risks).
* The logic handles lists of different lengths naturally.
* The dummy node simplifies list construction.

---

## Test Cases

```python
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test case 1
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: [7, 0, 8]

# Test case 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = Solution().addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: [0]

# Test case 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = Solution().addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
```
