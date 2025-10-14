# Swap Nodes in Pairs - LeetCode

## Problem statement

Given a singly-linked list, swap every two adjacent nodes and return the head of the modified list. You are **not allowed** to change the node values — you must change the node pointers themselves.

**Examples**

* Input: `1 -> 2 -> 3 -> 4`
  Output: `2 -> 1 -> 4 -> 3`
* Input: `[]`
  Output: `[]`
* Input: `1`
  Output: `1`
* Input: `1 -> 2 -> 3`
  Output: `2 -> 1 -> 3`

**Constraints**

* Number of nodes in the list is in `[0, 100]`.
* `0 <= Node.val <= 100`.

---

## Intuition

We need to swap nodes pairwise without touching their `val` fields. For each adjacent pair `(a, b)` we want to end up with `(b, a)` and ensure the rest of the list remains connected correctly. Two common approaches are:

1. **Recursive**: Swap the first pair, then recursively swap the remainder of the list and fix pointers.
2. **Iterative**: Walk the list pair-by-pair and rearrange pointers using a dummy node as an anchor. This avoids recursion overhead and uses constant extra space.

---

## Code with inline comments

Below are the two solutions you provided with inline comments added to help you remember what's happening.

### Recursive solution (with comments)

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if 0 or 1 node remains, no swap possible
        if not head or not head.next:
            return head

        # 'cur' is the first node of the current pair
        cur = head
        # 'nxt' is the second node of the current pair
        nxt = head.next

        # Recursively swap the pairs after the current pair
        # nxt.next will eventually point to 'cur' (after swap),
        # and cur.next should point to the head of the swapped remainder
        cur.next = self.swapPairs(nxt.next)

        # Make the second node point to the first => swap the two
        nxt.next = cur

        # 'nxt' is the new head of this swapped pair
        return nxt
```

### Iterative solution (with comments)

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that points to head to simplify edge cases
        # (for example when the head itself will change after the first swap)
        dummy = ListNode(0, head)
        # 'prev' is the node before the current pair; initially points to dummy
        prev, curr = dummy, head

        # Iterate while we have at least two nodes to swap
        while curr and curr.next:
            # nxtPair: the node after the current pair (start of next iteration)
            nxtPair = curr.next.next
            # second: second node in the current pair
            second = curr.next

            # Reverse the current pair: second -> curr
            second.next = curr
            # Connect the first node in the pair to the next sublist
            curr.next = nxtPair
            # Connect the previous part of the list to the new head of the pair
            prev.next = second

            # Move 'prev' and 'curr' forward for the next pair
            prev = curr
            curr = nxtPair

        # dummy.next is the real head after swaps
        return dummy.next
```

---

## Explanation of approaches & their differences (simple terms)

### Recursive approach — how it works

* Think of the linked list as: `[a, b] + rest` where `rest` is the remainder of the list starting at the third node.
* Swap `a` and `b` by making `b.next = a`.
* Set `a.next` to the result of recursively swapping `rest`.
* The function returns `b`, which becomes the new head of the swapped piece.

This approach is concise and mirrors the problem statement at the code level: swap the first pair, then do the rest.

### Iterative approach — how it works

* Use a dummy node so we always have a node (`prev`) pointing to the node before the current pair — this simplifies pointer updates, especially at the list head.
* For each pair `(a, b)`:

  * Keep a reference to the node after the pair (to continue iterating later).
  * Make `b.next = a`, `a.next = node_after_pair`, and `prev.next = b`.
  * Advance `prev` to `a` (because `a` is now the second node in the swapped pair) and `curr` to the next pair start.

This version manually manages pointers and runs inside a loop without recursion.

### Key differences (in plain language)

* **Readability vs. control**: The recursive solution is shorter and often easier to reason about conceptually. The iterative solution uses more pointer assignments but gives explicit control and avoids recursion.
* **Space usage**: Recursive uses extra stack space proportional to the number of recursive calls (O(n) worst-case). Iterative uses constant extra space (O(1)).
* **Practical constraints**: For long lists recursion may hit recursion depth limits or use unnecessary stack memory; iterative avoids both concerns.

---

## Time & Space Complexity

* **Time Complexity (both solutions)**: `O(n)`, where `n` is the number of nodes. Every node is visited and the pointers are updated a constant number of times.

* **Space Complexity**:

  * **Recursive**: `O(n)` in the worst case due to recursion call stack (actually `O(n/2)` calls for pairs, but this simplifies to `O(n)`).
  * **Iterative**: `O(1)` extra space — uses only a few pointers (`dummy`, `prev`, `curr`, `second`, `nxtPair`).

**Most optimal**: The iterative solution is the most optimal in terms of space because it uses constant extra memory. The time for both is the same (`O(n)`), so since iterative achieves `O(1)` space it is the preferred solution in practice. The iterative solution also avoids potential recursion limits and call overhead.

---

## Test cases

```python
solution = Solution()

# Test Case 1:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = solution.swapPairs(head)
print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)  # Output: 2 1 4 3

# Test Case 2:
head = None
result = solution.swapPairs(head)
print(result)  # Output: None

# Test Case 3:
head = ListNode(1)
result = solution.swapPairs(head)
print(result.val)  # Output: 1

# Test Case 4:
head = ListNode(1, ListNode(2, ListNode(3)))
result = solution.swapPairs(head)
print(result.val, result.next.val, result.next.next.val)  # Output: 2 1 3
```