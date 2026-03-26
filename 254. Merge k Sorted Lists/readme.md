# Merge k Sorted Lists - LeetCode

## Problem Overview

The **Merge k Sorted Lists** problem is a classic linked list and divide-and-conquer problem from LeetCode.

You are given:

* An array called `lists` containing `k` linked lists.
* Each linked list is already sorted in ascending order.

Your task is to **merge all the linked lists into one sorted linked list** and return the head of the merged list.

---

## Why This Problem Is Important

This problem teaches several important data structure and algorithm concepts:

* Linked list manipulation
* Merging sorted lists
* Divide and conquer
* Optimizing multi-list merging

It is commonly asked in technical interviews because it tests both algorithmic thinking and data structure understanding.

---

## Example

Input:

lists = [[1,4,5],[1,3,4],[2,6]]

The linked lists are:

1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6

Merged result:

1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

---

## Code With Comments

```python
from typing import List, Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the list of linked lists is empty, return None
        if not lists or len(lists) == 0:
            return None

        # Continue merging until only one list remains
        while len(lists) > 1:

            mergedLists = []

            # Merge lists in pairs
            for i in range(0, len(lists), 2):

                l1 = lists[i]

                # If there is a second list available, take it
                # otherwise use None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge the two lists and store the result
                mergedLists.append(self.mergeList(l1, l2))

            # Replace old list array with merged results
            lists = mergedLists

        # Only one merged list remains
        return lists[0]


    def mergeList(self, l1, l2):
        # Dummy node helps simplify linked list construction
        dummy = ListNode()

        # Tail pointer tracks the end of merged list
        tail = dummy

        # Merge nodes while both lists still have elements
        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            # Move tail forward
            tail = tail.next

        # If one list still has remaining nodes, attach them
        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        # Return the head of merged list
        return dummy.next
```

---

## Explanation of the Approach

### Key Idea

Instead of merging all lists at once, we use a **divide and conquer strategy**.

This means:

* Merge lists in pairs
* Reduce the total number of lists each round
* Continue until only one list remains

This approach is similar to the way **merge sort** works.

---

## Step-by-Step Logic

### Step 1: Pair the Lists

If we have:

lists = [L1, L2, L3, L4]

We merge them as:

(L1 + L2) and (L3 + L4)

Now we have:

[M1, M2]

---

### Step 2: Merge Again

Now merge:

(M1 + M2)

Result:

Final merged list.

---

## How Two Lists Are Merged

The `mergeList` function works like the classic **Merge Two Sorted Lists** problem.

Steps:

1. Compare the heads of both lists
2. Attach the smaller node to the result
3. Move that list forward
4. Repeat until one list ends
5. Attach the remaining nodes

A dummy node is used to simplify pointer handling.

---

## Possible Approaches

### 1. Brute Force Approach

* Collect all values from all lists
* Sort them
* Rebuild a new linked list

Time Complexity:

O(N log N)

Where N is the total number of nodes.

Not optimal because sorting is expensive.

---

### 2. Sequential Merge

Merge lists one by one:

(((L1 + L2) + L3) + L4)

Time Complexity:

O(N * k)

Where k is the number of lists.

This becomes slow when k is large.

---

### 3. Divide and Conquer

Merge lists in pairs repeatedly.

This dramatically reduces work because lists are merged in balanced groups.

---

## Time and Space Complexity

### Time Complexity

Let:

N = total number of nodes

k = number of lists

Each level merges all nodes once.

Number of levels:

log k

Total time:

O(N log k)

---

### Space Complexity

Extra space used for the list array during merging:

O(k)

The output linked list itself is not counted.

---

## Why This Solution Is Optimal

This solution is optimal because:

* Every node must be processed at least once.
* Divide and conquer ensures balanced merging.
* The number of merge rounds is minimized.

This gives the optimal complexity:

O(N log k)

which is significantly better than sequential merging.