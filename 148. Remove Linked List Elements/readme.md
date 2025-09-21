# Remove Linked List Elements - LeetCode

## Problem Explanation

The "Remove Linked List Elements" problem asks us to delete all nodes in a linked list whose values are equal to a given integer `val`. The function should return the new head of the modified linked list.

### Example 1

**Input:** head = \[1,2,6,3,4,5,6], val = 6
**Output:** \[1,2,3,4,5]

### Example 2

**Input:** head = \[], val = 1
**Output:** \[]

### Example 3

**Input:** head = \[7,7,7,7], val = 7
**Output:** \[]

### Constraints

* The number of nodes in the list is in the range \[0, 10⁴].
* 1 <= Node.val <= 50
* 0 <= val <= 50

---

## Recursive Solution

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        # Recursively process the rest of the list
        head.next = self.removeElements(head.next, val)
        # If current node's value equals val, skip it
        return head if head.val != val else head.next
```

### Explanation of Code

1. **Base Case:** If the list is empty (`head` is None), return None.
2. **Recursive Step:** Process the rest of the list first using recursion.
3. **Decision:** If the current node's value equals `val`, skip it by returning `head.next`. Otherwise, keep the current node.

### Complexity

* **Time Complexity:** O(n) – each node is visited once.
* **Space Complexity:** O(n) in the worst case due to recursion stack.

This approach is elegant and compact but may cause stack overflow for very large lists.

---

## Iterative Solution

```python
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)  # Dummy node before head
        prev, curr = dummy, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                # Skip the current node
                prev.next = nxt
            else:
                # Move prev forward only if current is not removed
                prev = curr
            curr = nxt

        return dummy.next
```

### Explanation of Code

1. **Dummy Node:** A dummy node is created to handle edge cases (like removing the head) smoothly.
2. **Pointers:** `prev` points to the last valid node, `curr` points to the node being inspected.
3. **Decision:** If `curr.val == val`, remove the node by linking `prev.next` to `curr.next`. Otherwise, move `prev` forward.
4. **Continue Traversal:** Move `curr` to the next node.

### Complexity

* **Time Complexity:** O(n) – each node is visited once.
* **Space Complexity:** O(1) – only a few pointers are used.

This iterative method is more memory-efficient and preferred for large linked lists.

---

## Comparison of Approaches

* **Recursive Approach:** Easier to write and understand, but uses extra space due to recursion. Risk of stack overflow on large inputs.
* **Iterative Approach:** Slightly more verbose but optimal in terms of memory. It efficiently handles large lists without recursion issues.

---

## Optimal Solution

The **iterative solution** is the most optimal because:

* It runs in **O(n)** time.
* It uses **O(1)** extra space.

* It avoids recursion depth limitations, making it more robust for large inputs.

---

## Test Cases

```python
# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val1 = 6  
expected1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result1 = Solution().removeElements(head1, val1)
print_linked_list(result1)  # Output: [1, 2, 3, 4, 5]

# Test Case 2
head2 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val2 = 7
expected2 = None
result2 = Solution().removeElements(head2, val2)
print_linked_list(result2)  # Output: []

# Test Case 3
head3 = None
val3 = 7
expected3 = None
result3 = Solution().removeElements(head3, val3)
print_linked_list(result3)  # Output: []
```
