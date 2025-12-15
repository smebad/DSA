# Merge In Between Linked Lists - LeetCode

## Problem Explanation

The **Merge In Between Linked Lists** problem gives you two singly linked lists, `list1` and `list2`, along with two integers `a` and `b`.

Your task is to:

1. Remove nodes from index `a` to index `b` (inclusive) in `list1`.
2. Insert the entire `list2` in the exact position where those nodes were removed.
3. Return the head of the modified `list1`.

The indexing is **0-based**, meaning the first node is at index `0`.

The key challenge is to reconnect pointers correctly without creating new nodes or breaking the linked list structure.

---

## Intuition Behind the Problem

A linked list is all about **references (next pointers)**. To solve this problem, we need to:

* Find the node **just before index `a`**.
* Find the node **just after index `b`**.
* Connect the end of `list2` to the remainder of `list1`.

Once these connections are correct, the merge is complete.

---

## Code With Comments

Below is your provided solution with comments added to help you remember the logic later:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = 0

        # Move curr to the node just before index 'a'
        while i < a - 1:
            curr = curr.next
            i += 1

        # Store the node before index 'a'
        head = curr

        # Move curr to the node just after index 'b'
        while i <= b:
            curr = curr.next
            i += 1

        # Connect node before 'a' to the head of list2
        head.next = list2

        # Move to the end of list2
        while list2.next:
            list2 = list2.next

        # Connect the end of list2 to the remaining part of list1
        list2.next = curr

        # Return the head of the modified list1
        return list1
```

---

## Step-by-Step Approach

1. Start from the head of `list1`.
2. Traverse until you reach the node just **before** index `a`.
3. Continue traversing until you pass index `b`.
4. Link the node before `a` to the head of `list2`.
5. Traverse `list2` to its last node.
6. Connect the last node of `list2` to the node after `b`.

This preserves the order and structure of both lists.

---

## Why This Approach Works

* No new nodes are created.
* Only pointers are updated.
* Both linked lists remain valid.
* The problem guarantees that `a` and `b` are valid indices, so no extra edge-case handling is required.

This makes the solution both clean and efficient.

---

## Time and Space Complexity

### Time Complexity

* Traversing `list1`: `O(N)`
* Traversing `list2`: `O(M)`

Total time complexity:

```
O(N + M)
```

Where:

* `N` is the length of `list1`
* `M` is the length of `list2`

### Space Complexity

```
O(1)
```

No extra data structures are used. The merge is done in place by modifying pointers.

---

## Most Optimal Solution and Why

This **two-pointer, in-place approach** is the most optimal solution because:

* It performs a single pass over each list.
* It does not use additional memory.
* It directly modifies existing nodes.

Any alternative solution that copies nodes or uses auxiliary data structures would increase space complexity unnecessarily.

---

## Test Cases
```python
def print_linked_list(head):
    curr = head
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(result)

# Test Case 1
list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
a = 3
b = 4
result = Solution().mergeInBetween(list1, a, b, list2)
print_linked_list(result)  # Expected Output: [10, 1, 13, 1000000, 1000001, 1000002, 5]

# Test Case 2
list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004)))))
a = 2
b = 5
result = Solution().mergeInBetween(list1, a, b, list2)
print_linked_list(result)  # Expected Output: [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
```