# Take Gifts From the Richest Pile - LeetCode

## Problem Explanation

The problem **Take Gifts From the Richest Pile** gives us an array `gifts`, where each element represents the number of gifts in a pile. Over the course of `k` seconds, we repeatedly perform the following steps:

1. Choose the pile with the maximum number of gifts.
2. Reduce the pile to the floor of the square root of its current number of gifts.
3. Repeat the process `k` times.

After completing `k` operations, we must return the total number of gifts remaining across all piles.

### Example 1:

```
Input: gifts = [25,64,9,4,100], k = 4
Output: 29
```

**Explanation:**

* Choose 100 → becomes 10.
* Choose 64 → becomes 8.
* Choose 25 → becomes 5.
* Choose 10 → becomes 3.
  Final piles = [5,8,9,4,3]. Sum = 29.

### Example 2:

```
Input: gifts = [1,1,1,1], k = 4
Output: 4
```

**Explanation:**

* All piles are 1, square root of 1 is still 1, so nothing changes.
  Total = 4.

---

## Code with Comments

```python
import heapq
from math import floor, sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert all elements to negative because Python's heapq is a min-heap by default.
        # Negating values allows us to simulate a max-heap.
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        
        # Build the heap from the list.
        heapq.heapify(gifts)

        # Perform k operations
        for _ in range(k):
            # Extract the current maximum (by popping the smallest negative value)
            n = -heapq.heappop(gifts)
            # Push the square root of this number (negated again for max-heap behavior)
            heapq.heappush(gifts, -floor(sqrt(n)))

        # Sum the values (negating them back to positive)
        return -sum(gifts)
```

---

## Solution Explanation

The approach uses a **max-heap** (simulated via a min-heap with negated values) to always pick the largest pile efficiently.

### Step-by-step logic:

1. Convert all values to negatives so that Python's `heapq` can be used as a max-heap.
2. Build a heap of size `n` (number of piles).
3. For `k` iterations:

   * Remove the largest pile (top of the heap).
   * Replace it with the floor of its square root.
4. At the end, compute the sum of all remaining piles and return it.

---

## Complexity Analysis

* **Time Complexity:**

  * Building the heap takes **O(n)**.
  * Each of the `k` operations involves a pop and push on the heap, each costing **O(log n)**.
  * Total = **O(n + k log n)**.

* **Space Complexity:**

  * We use a heap of size `n`, so **O(n)**.

### Why is this optimal?

* We must repeatedly extract the maximum pile. Without a heap, finding the maximum each time would take **O(n)** per operation, leading to **O(nk)** in total.
* The heap allows us to always access the maximum in **O(log n)** time, making the process much more efficient for large inputs.

Thus, the heap-based solution is the most optimal approach for this problem.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
gifts = [25,64,9,4,100]
k = 4
print(sol.pickGifts(gifts, k))  # Output: 29

# Test Case 2
gifts = [1,1,1,1]
k = 4
print(sol.pickGifts(gifts, k))  # Output: 4
```