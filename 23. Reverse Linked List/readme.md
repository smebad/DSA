# Reverse Linked List - LeetCode

## Problem Description

Given the `head` of a singly linked list, the task is to reverse the list and return the reversed list.

### Example 1
**Input:** head = [1,2,3,4,5]  
**Output:** [5,4,3,2,1]

### Example 2
**Input:** head = [1,2]  
**Output:** [2,1]

### Example 3
**Input:** head = []  
**Output:** []

### Constraints
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

### Follow-up
The problem asks if the reversal can be implemented both iteratively and recursively. Both solutions are provided below.


## Understanding Reverse Linked List

A **linked list** is a linear data structure where each element points to the next. Reversing a linked list means making the last node become the head and reversing all the pointers' directions.

In other words, the first node points to `null`, the second node points to the first, the third to the second, and so on, until the entire list is reversed.


## Recursive Solution Explanation

### Code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
```

### Step-by-Step Breakdown
1. **Base case:**
   - If the `head` is `None`, it means the list is empty. Return `None`.

2. **Recursive case:**
   - Assume `head.next` exists. Recursively call `reverseList(head.next)`, which will reverse the rest of the list.
   - After reversing the smaller list, make `head.next.next = head`, meaning the next node now points back to the current head.

3. **Breaking the link:**
   - Set `head.next = None` to break the original forward link.

4. **Return new head:**
   - Return the new head of the reversed list.

### Logic
- The recursive function reaches the end of the list and starts connecting each node backward.
- This creates a reversal effect as the recursion unwinds.

### Time Complexity
- **O(n)** where `n` is the number of nodes. Each node is visited exactly once.

### Space Complexity
- **O(n)** due to the recursion stack. Each recursive call adds a new frame to the call stack.


## Iterative Solution Explanation

### Code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next  # Save next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev one step forward
            curr = temp       # Move curr one step forward
        return prev
```

### Step-by-Step Breakdown
1. Initialize two pointers:
   - `prev` as `None` (end of the new reversed list).
   - `curr` as `head` (current node).

2. Traverse through the list:
   - Save `curr.next` into `temp`.
   - Set `curr.next` to `prev` to reverse the link.
   - Move `prev` to `curr`.
   - Move `curr` to `temp` (original next node).

3. When traversal is complete, `prev` will point to the new head.

### Logic
- Iteratively reverse the pointers without using any extra memory.
- This approach modifies the list in-place.

### Time Complexity
- **O(n)** where `n` is the number of nodes.

### Space Complexity
- **O(1)** because it only uses a fixed number of variables regardless of list size.


## Summary

| Approach     | Time Complexity | Space Complexity | Description |
|--------------|------------------|------------------|-------------|
| Recursive    | O(n)             | O(n)             | Simple but uses call stack |
| Iterative    | O(n)             | O(1)             | Most optimal solution |

- The iterative approach is **more optimal** because it uses **constant space**.
- The recursive approach is more elegant but can lead to a **stack overflow** for very large lists.


## Test Cases Used

```python
# Helper functions to create and convert linked list

def create_linked_list(arr):
    head = None
    for val in reversed(arr):
        head = ListNode(val, head)
    return head

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Test Case 1
head = create_linked_list([1,2,3,4,5])
sol = Solution()
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))  # Output: [5,4,3,2,1]

# Test Case 2
head = create_linked_list([1,2])
sol = Solution()
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))  # Output: [2,1]

# Test Case 3
head = create_linked_list([])
sol = Solution()
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))  # Output: []
```

