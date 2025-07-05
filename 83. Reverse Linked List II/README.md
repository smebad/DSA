# Reverse Linked List II

## Problem Description

"Reverse Linked List II" is a classic linked list problem in which you're given a singly linked list and two integer positions `left` and `right` such that `left <= right`. The task is to reverse the nodes of the list from position `left` to position `right`, and return the modified list.

For example:

* Input: `head = [1,2,3,4,5], left = 2, right = 4`
* Output: `[1,4,3,2,5]`

The goal is to perform the reversal in **one pass** through the list.

---

## Code Explanation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge case handling
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head

        # Move leftPrev and cur to the proper starting point in the list
        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Reverse the sublist from left to right
        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next     # Temporarily store the next node
            cur.next = prev        # Reverse the current node's pointer
            prev, cur = cur, tmpNext  # Move prev and cur forward

        # Reconnect the reversed sublist back to the main list
        leftPrev.next.next = cur  # Connect end of reversed sublist to the remainder
        leftPrev.next = prev      # Connect start of reversed sublist to the beginning

        return dummy.next  # Return the updated list, skipping dummy node
```

---

## Approach and Logic

* We use a dummy node to handle edge cases cleanly, especially when `left = 1`.
* We first traverse the list to reach the node just before the `left` position (`leftPrev`) and the node at the `left` position (`cur`).
* Then, we reverse the `right - left + 1` nodes starting from `cur` using a standard linked list reversal loop.
* Finally, we reconnect the reversed segment with the rest of the list:

  * `leftPrev.next` points to the new head of the reversed sublist.
  * The old `left` node, now at the end of the reversed sublist, connects to the `right+1` node.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * We traverse the list once to reach the left position and reverse part of it.
  * Since we only make a single pass through the relevant nodes, the complexity is linear.
* **Space Complexity:** `O(1)`

  * We use only a constant number of pointers (`dummy`, `cur`, `prev`, `tmpNext`, `leftPrev`).
  * No additional memory is used apart from these variables.

### Optimality

This solution is optimal:

* Performs in **one pass**, satisfying the follow-up requirement.
* Uses **constant space**.
* Cleanly handles edge cases using a dummy node, reducing code complexity.

---

## Test Cases

### Test Case 1

```python
# Input: [1, 2, 3, 4, 5], left = 2, right = 4
# Output: [1, 4, 3, 2, 5]
```

**Explanation:** Sublist \[2, 3, 4] is reversed to \[4, 3, 2].

### Test Case 2

```python
# Input: [5], left = 1, right = 1
# Output: [5]
```

**Explanation:** Only one element, no change needed.

