# Middle of the Linked List - LeetCode

## Problem Explanation

The **"Middle of the Linked List"** problem asks us to find the middle node in a singly linked list. If the list has an odd number of nodes, we return the single middle node. If it has an even number of nodes, we return the **second** of the two middle nodes.

### Example 1

**Input:** head = [1,2,3,4,5]
**Output:** [3,4,5]
**Explanation:** The middle node is node 3.

### Example 2

**Input:** head = [1,2,3,4,5,6]
**Output:** [4,5,6]
**Explanation:** There are two middle nodes (3 and 4), so we return the second one.

### Constraints

* The number of nodes in the list is in the range [1, 100].
* 1 <= Node.val <= 100

---

## Convert to Array Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        
        # Traverse the linked list and store all nodes in an array
        while cur:
            arr.append(cur)
            cur = cur.next
            
        # Return the middle node using the array index
        return arr[len(arr) // 2]
```

### Explanation

1. We initialize an empty array `arr` to store the nodes.
2. We iterate through the linked list and append each node to `arr`.
3. After traversal, the middle node is at index `len(arr) // 2`.
4. We return this node, which represents the middle of the list.

### Complexity Analysis

* **Time Complexity:** O(n), where *n* is the number of nodes, since we traverse the list once.
* **Space Complexity:** O(n), as we store all nodes in an array.

This solution is simple and easy to understand, but it is **not optimal** due to extra memory usage.

---

## Fast and Slow Pointer Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Move 'fast' twice as quickly as 'slow'
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When 'fast' reaches the end, 'slow' is at the middle
        return slow
```

### Explanation

1. We use two pointers — `slow` and `fast` — both starting at the head.
2. In each iteration:

   * `slow` moves one step forward.
   * `fast` moves two steps forward.
3. When `fast` reaches the end of the list, `slow` will be at the middle node.
4. We return `slow` as the middle node.

### Complexity Analysis

* **Time Complexity:** O(n), since both pointers traverse the list once.
* **Space Complexity:** O(1), as no extra data structures are used.

---

## Comparison of Approaches

| Approach              | Time Complexity | Space Complexity | Description                               |
| --------------------- | --------------- | ---------------- | ----------------------------------------- |
| Convert to Array      | O(n)            | O(n)             | Easy to understand but uses extra memory. |
| Fast and Slow Pointer | O(n)            | O(1)             | Optimal solution with no extra space.     |

### Why the Fast and Slow Pointer Approach is Optimal

The two-pointer method efficiently finds the middle node in a **single traversal** and without using any additional space. It is the **most optimal** solution for this problem because it meets both time and space efficiency goals.

---

## Test Cases

```python
# Test Case 1:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = Solution().middleNode(head)
print(result.val)  # Output: 3

# Test Case 2:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
result = Solution().middleNode(head)
print(result.val)  # Output: 4
```