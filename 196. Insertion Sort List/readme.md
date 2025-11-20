# Insertion Sort List - LeetCode

## 1. What is the "Insertion Sort List" Problem?

The Insertion Sort List problem is a linked list adaptation of the classic insertion sort algorithm. You are given the head of a **singly linked list**, and your task is to **sort the list in ascending order** using insertion sort.

### How insertion sort works

Insertion sort builds a sorted portion of the list step by step. On each iteration:

1. Take the next unsorted node.
2. Walk through the sorted part of the list until the correct position is found.
3. Insert the node into the sorted portion.

For arrays, this requires shifting elements.
For linked lists, we instead **rearrange pointers**, making it efficient because no shifting is needed.

---

## 2. Explanation of the Code

Below is your original solution rewritten with comments to help you remember each step.

```python
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node helps simplify edge cases (like inserting at the head)
        dummy = ListNode(0, head)
        
        # prev represents the last node in the sorted portion
        # cur is the node to be inserted into the sorted portion
        prev, cur = head, head.next

        while cur:
            # Case 1: cur is already in correct order (greater than or equal to previous)
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue

            # Case 2: cur is smaller and must be repositioned
            # Start from the dummy to find insertion position
            tmp = dummy
            
            # Move forward until finding the correct spot
            while cur.val > tmp.next.val:
                tmp = tmp.next

            # Remove cur from its current position
            prev.next = cur.next

            # Insert cur after tmp
            cur.next = tmp.next
            tmp.next = cur

            # Move cur to the next unsorted node
            cur = prev.next

        return dummy.next
```

---

## 3. Detailed Explanation of the Approach and Logic

### Main idea

The sorted list grows gradually while the unsorted part shrinks. The idea is:

* Keep track of two regions: sorted and unsorted.
* Each iteration takes the `cur` node from the unsorted region.
* If `cur` is greater than or equal to `prev`, it is already in the correct position.
* Otherwise, search from the beginning to insert it at the right spot.

### Why use a dummy node?

Without the dummy, it becomes complicated to insert before the head.
A dummy node adds a simple fixed starting point.

### How the pointers move

* `prev`: last node of the sorted section
* `cur`: first node of the unsorted section
* `tmp`: used to search where `cur` belongs in the sorted section

### Step-by-step logic

1. Start with `dummy -> head`.
2. Compare `cur` with `prev`:

   * If already sorted, move ahead.
   * If not, find correct position.
3. Insert `cur` into sorted portion.
4. Continue until the list ends.

### Why this is optimal for linked lists

Insertion sort on linked lists avoids shifting elements, which is expensive for arrays.
Here, pointer rearrangements make insertion efficient.

---

## 4. Time and Space Complexity

### Time Complexity: **O(n²)**

Worst case occurs when the list is in reverse order.
For each of the n nodes, you may need to scan through the sorted portion, which grows up to n.

### Space Complexity: **O(1)**

Only pointers (dummy, prev, cur, tmp) are used.
No extra data structures or new nodes are created.

---

## Why this solution is optimal

For linked lists:

* Insertion sort is more efficient than many other comparison-based sorts because nodes can be re-linked quickly.
* Although the worst-case time is O(n²), the algorithm is optimal when:

  * The list is nearly sorted.
  * You want a stable, in-place sorting method.
  * You want minimal extra memory usage.

### Most optimal scenario

If the list is **almost sorted**, each insertion is O(1), giving nearly **O(n)** performance overall.
This is one of the best-case scenarios possible for linked list sorting without using extra memory or more advanced algorithms like merge sort.

---

## 5. Test Cases
```python
def print_list(head: Optional[ListNode]):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Test Case 1:
head1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head1 = Solution().insertionSortList(head1)
print_list(sorted_head1)  # Output: [1, 2, 3, 4]

# Test Case 2:
head2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
sorted_head2 = Solution().insertionSortList(head2)
print_list(sorted_head2)  # Output: [-1, 0, 3, 4, 5]
```