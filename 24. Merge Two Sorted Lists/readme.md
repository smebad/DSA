# Merge Two Sorted Lists - LeetCode

## Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`. The task is to merge these two linked lists into a single sorted linked list. The merged list should be made by splicing together the nodes of the first two lists.

You must return the head of the new merged linked list.

### Examples

**Example 1:**
- Input: `list1 = [1,2,4]`, `list2 = [1,3,4]`
- Output: `[1,1,2,3,4,4]`

**Example 2:**
- Input: `list1 = []`, `list2 = []`
- Output: `[]`

**Example 3:**
- Input: `list1 = []`, `list2 = [0]`
- Output: `[0]`

## Constraints
- The number of nodes in both lists is in the range [0, 50].
- −100 <= Node.val <= 100
- Both `list1` and `list2` are sorted in non-decreasing order.

## Understanding the Problem

In this problem, we are given two singly linked lists that are sorted. We need to merge them into a new sorted linked list. The key point is to reuse the given nodes, not create new ones. This problem tests our understanding of linked list manipulation and recursive/iterative approaches in Data Structures and Algorithms (DSA).

## Recursive Solution Explanation

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

### Step by Step Code Explanation
- Check if `list1` is `None`. If it is, return `list2` because merging an empty list with a list results in the non-empty list.
- Similarly, check if `list2` is `None`. If it is, return `list1`.
- Compare the current nodes of `list1` and `list2`.
- If `list1.val <= list2.val`, recursively merge the rest of `list1` (i.e., `list1.next`) with `list2` and set it as the `next` of `list1`. Then return `list1`.
- Otherwise, recursively merge `list1` with the rest of `list2` (i.e., `list2.next`) and set it as the `next` of `list2`. Then return `list2`.

### Logic Summary
- Always attach the smaller node to the merged list and move ahead in that list.
- Recursively build the merged list node by node.

### Time and Space Complexity
- **Time Complexity:** `O(n + m)` where `n` and `m` are the lengths of `list1` and `list2`.
- **Space Complexity:** `O(n + m)` due to the recursion stack.

## Iterative Solution Explanation

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
```

### Step by Step Code Explanation
- Create a dummy node to simplify edge cases.
- `node` initially points to the dummy node.
- Loop through both lists while neither is `None`.
- Compare `list1.val` and `list2.val`, attach the smaller node to `node.next`, and move the respective pointer (`list1` or `list2`) ahead.
- Move the `node` pointer forward.
- After the loop, attach the remaining part of `list1` or `list2` (only one will be non-empty).
- Finally, return `dummy.next` which is the head of the merged list.

### Logic Summary
- Use a dummy node to simplify list merging.
- Keep connecting the smaller node at each step.
- No recursion, just iteration.

### Time and Space Complexity
- **Time Complexity:** `O(n + m)` where `n` and `m` are the lengths of `list1` and `list2`.
- **Space Complexity:** `O(1)` because only a few pointers are used and no recursion stack is needed.

## Which Solution is More Optimal?
- The **iterative solution** is more optimal in terms of **space complexity** (`O(1)` vs `O(n+m)` for recursion).
- Both solutions have the same **time complexity** (`O(n+m)`).
- The recursive solution is more elegant and shorter but can cause a stack overflow for very large inputs.

## Conclusion
- It is better to prefer the iterative solution if space is critical.
- If simplicity and clarity are preferred (and input size is manageable), recursion is a very clean approach.

