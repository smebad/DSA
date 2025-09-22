# Remove Duplicates from Sorted List - LeetCode

## Problem Statement

The problem **Remove Duplicates from Sorted List** is a classic linked list problem. Given the head of a sorted linked list, the task is to remove all duplicate nodes so that each element appears only once. The list must remain sorted after duplicates are removed.

### Example 1

* **Input:** head = \[1,1,2]
* **Output:** \[1,2]

### Example 2

* **Input:** head = \[1,1,2,3,3]
* **Output:** \[1,2,3]

### Constraints

* The number of nodes in the list is in the range \[0, 300].
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.

---

## Recursive Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # Base case: empty list or single node
            return head

        # Recursively process the rest of the list
        head.next = self.deleteDuplicates(head.next)

        # If current node has the same value as the next, skip it
        return head if head.val != head.next.val else head.next
```

### Explanation of the Code

* If the list is empty or has only one node, return the head.
* Recursively call the function on `head.next` to process the rest of the list.
* Compare the current node's value with the next node:

  * If they are equal, skip the duplicate by returning `head.next`.
  * Otherwise, keep the current node and return `head`.

### Complexity Analysis

* **Time Complexity:** O(n), where n is the number of nodes. Each node is visited once.
* **Space Complexity:** O(n), because recursion uses stack space.

This approach is elegant but may cause stack overflow for very large lists.

---

## Iterative Solution

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            # Skip duplicate nodes
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
```

### Explanation of the Code

* Use a pointer `cur` to traverse the linked list.
* While traversing, check if the next node exists and has the same value as the current node.
* If so, skip the duplicate by updating `cur.next` to `cur.next.next`.
* Continue until the end of the list.

### Complexity Analysis

* **Time Complexity:** O(n), where n is the number of nodes.
* **Space Complexity:** O(1), since no extra space is used apart from variables.

This iterative solution is more space-efficient and avoids recursion overhead, making it the **optimal solution**.

---

## Differences Between Solutions

* **Recursive Solution:** Uses recursion and is easier to understand conceptually but consumes extra space due to the call stack.
* **Iterative Solution:** Uses a loop and a pointer. It is more space-efficient and better suited for large inputs.

---

## Conclusion

Both solutions work correctly for removing duplicates from a sorted linked list. However, the **iterative solution** is considered the optimal one due to its **O(1) space complexity** and simplicity in handling large lists without the risk of stack overflow.

---

## Test Cases

```python
# Test Cases:
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test Case 1:
head = ListNode(1, ListNode(1, ListNode(2)))
print_list(Solution().deleteDuplicates(head))  # Output: 1 -> 2 -> None

# Test Case 2:
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print_list(Solution().deleteDuplicates(head))  # Output: 1 -> 2 -> 3 -> None
```