# Palindrome Linked List - LeetCode

## Problem Explanation

A **Palindrome Linked List** is a linked list whose sequence of values reads the same forward and backward. For example:

* `[1, 2, 2, 1]` is a palindrome because reversing it gives the same sequence.
* `[1, 2]` is not a palindrome because reversing it gives `[2, 1]`, which is different.

**Problem Statement:**
Given the head of a singly linked list, return `true` if it is a palindrome and `false` otherwise.

### Example 1:

```
Input: head = [1,2,2,1]
Output: true
```

### Example 2:

```
Input: head = [1,2]
Output: false
```

**Constraints:**

* The number of nodes in the list is in the range \[1, 10^5].
* Each node value is between 0 and 9.

**Follow-up:** Can this be solved in O(n) time and O(1) space?

---

## Solutions

### 1. Convert To Array Solution

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        # Step 1: Copy linked list values into an array
        while cur:
            arr.append(cur.val)
            cur = cur.next

        # Step 2: Use two pointers to check if array is a palindrome
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:  # If mismatch found, not palindrome
                return False
            l, r = l + 1, r - 1

        return True
```

**Explanation:**

* We traverse the list once to store all values in an array.
* Then, using two pointers (one from start, one from end), we compare values.
* If all pairs match, the list is a palindrome.

**Complexity:**

* Time: **O(n)** (two traversals: building the array and checking).
* Space: **O(n)** (extra array storage).

---

### 2. Fast and Slow Pointers Solution

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # Step 1: Find the middle using fast and slow pointers
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Step 3: Compare first half and reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:  # If mismatch, not palindrome
                return False
            left = left.next
            right = right.next

        return True
```

**Explanation:**

* Use **fast and slow pointers** to find the middle of the list.

  * `fast` moves two steps, `slow` moves one step.
  * When `fast` reaches the end, `slow` is at the middle.
* Reverse the second half of the list.
* Compare the first half with the reversed second half.
* If all nodes match, it is a palindrome.

**Complexity:**

* Time: **O(n)** (finding middle, reversing, and comparing).
* Space: **O(1)** (reverses the list in-place without extra space).

---

## Comparison of Approaches

1. **Convert To Array:**

   * Easy to understand and implement.
   * Requires extra space proportional to the size of the list.
   * Not optimal for memory usage.

2. **Fast and Slow Pointers:**

   * More advanced but efficient.
   * Does not require extra space.
   * Achieves the follow-up requirement of **O(n) time and O(1) space**.

---

## Optimal Solution

The **fast and slow pointers approach** is the most optimal:

* **O(n) time** because the list is traversed a constant number of times.
* **O(1) space** because it modifies the list in place instead of using extra arrays.
* Best choice for large linked lists where memory efficiency matters.
