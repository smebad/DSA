# Intersection of Two Linked Lists - LeetCode

## Problem Explanation

The **Intersection of Two Linked Lists** problem asks us to determine the node at which two singly linked lists intersect. If the two linked lists do not intersect, we must return `null`.

An intersection means that at some node, both lists share the same reference in memory (not just the same value). That is, the nodes after the intersection are common between the two lists.

### Example

**Input:**

```
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
Intersection at node with value 8
```

**Output:**

```
Intersected at '8'
```

If no intersection exists, return `None`.

---

## Brute Force Solution

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        while headA:
            cur = headB
            while cur:
                if headA == cur:  # If both nodes refer to the same memory location
                    return headA   # Intersection found
                cur = cur.next
            headA = headA.next
        return None
```

### Explanation of the Code

* We start by traversing each node in **List A**.
* For each node in **List A**, we compare it with every node in **List B**.
* If we find a node that is the same by reference (`headA == cur`), that means both lists intersect at that node.
* If we finish checking all pairs and find no intersection, we return `None`.

### Time and Space Complexity

* **Time Complexity:** `O(m * n)` — For each of the `m` nodes in List A, we traverse up to `n` nodes in List B.
* **Space Complexity:** `O(1)` — We only use pointers without extra storage.

### Summary

This method is easy to understand but inefficient for large lists, as it performs nested iterations.

---

## Optimal Two-Pointer Solution

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        l1, l2 = headA, headB
        while l1 != l2:
            # If a pointer reaches the end of a list, switch it to the head of the other list
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1  # Either the intersection node or None
```

### Explanation of the Code

* We initialize two pointers, `l1` and `l2`, pointing to the heads of `List A` and `List B`.
* Both pointers move one step at a time through their respective lists.
* When one pointer reaches the end of its list, it switches to the head of the other list.
* This ensures that both pointers travel the same total distance (`m + n`), synchronizing their traversal.
* If there is an intersection, both pointers will meet at the intersection node.
* If there is no intersection, both will become `None` at the same time.

### Example Walkthrough

```
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
```

1. `l1` traverses A, `l2` traverses B.
2. When `l1` finishes A, it jumps to head of B.
3. When `l2` finishes B, it jumps to head of A.
4. After traveling equal combined distances, both meet at node 8 (the intersection).

### Time and Space Complexity

* **Time Complexity:** `O(m + n)` — Each list is traversed at most twice.
* **Space Complexity:** `O(1)` — Only two pointers are used.

### Why It Is Optimal

This approach ensures minimal time and space usage:

* It avoids nested loops.
* It guarantees synchronization of traversal paths.
* It is optimal for problems involving linked lists where we need to align paths of different lengths.

---

## Comparison of Solutions

| Approach     | Time Complexity | Space Complexity | Explanation                                             |
| ------------ | --------------- | ---------------- | ------------------------------------------------------- |
| Brute Force  | O(m * n)        | O(1)             | Checks all possible node pairs, slow for large inputs   |
| Two Pointers | O(m + n)        | O(1)             | Efficiently synchronizes traversal without extra memory |

The **two-pointer approach** is the optimal and recommended solution because it achieves linear time with constant space.