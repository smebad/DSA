# Grumpy Bookstore Owner - LeetCode

## Problem Explanation

The **Grumpy Bookstore Owner** problem describes a situation where a bookstore owner has customers entering every minute. However, the owner can be grumpy during certain minutes, which makes customers entering during that time unsatisfied. The owner can use a special technique to stay calm (not grumpy) for a continuous block of `minutes`. The goal is to maximize the total number of satisfied customers throughout the day by choosing the best time window to use the technique.

### Example:

```
Input:
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

Output: 16
```

Explanation:

* Normally satisfied customers (non-grumpy minutes): `1 + 1 + 1 + 7 = 10`
* If the owner uses the technique in the last 3 minutes, they satisfy an additional `6` customers (from `1 + 7 + 5`).
* Total satisfied = 10 + 6 = **16**

---

## Brute Force Solution

```python
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res, n = 0, len(customers)
        
        # Step 1: Add all customers that are already satisfied (when owner is not grumpy)
        for i in range(n):
            if not grumpy[i]:
                res += customers[i]
        
        satisfied = res  # baseline satisfaction

        # Step 2: Try every possible window of size 'minutes'
        for i in range(n - minutes + 1):
            cur = 0
            # Add all grumpy customers in this window
            for j in range(i, i + minutes):
                if grumpy[j]:
                    cur += customers[j]
            res = max(res, satisfied + cur)  # choose the max satisfaction

        return res
```

### Explanation:

* Count all already satisfied customers (when `grumpy[i] == 0`).
* For every possible window of size `minutes`, add all customers who would be satisfied if the owner stayed calm during that period.
* Track the maximum total satisfaction achieved.

### Time Complexity:

* **O(n * m)**, where `n` = number of customers, and `m` = `minutes`.

  * The nested loop (outer for window start, inner for window range) makes it quadratic.
* **Space Complexity:** O(1), since no extra data structures are used.

This solution works correctly but becomes slow for large inputs.

---

## Optimized Sliding Window Solution

```python
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        window = max_window = 0
        satisfied = 0

        for r in range(len(customers)):
            # If grumpy, add to current window gain potential
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]  # Already satisfied customers

            # Maintain window size of 'minutes'
            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]  # remove the leftmost customer from window
                l += 1

            max_window = max(window, max_window)

        return satisfied + max_window
```

### Explanation (Step-by-Step):

1. **Baseline Satisfaction:** Add customers from minutes when owner is already not grumpy.
2. **Window Sum:** For each window of size `minutes`, calculate how many extra customers could be satisfied if the owner stayed calm.
3. **Sliding Window:** Instead of recalculating from scratch, adjust the window by removing the left element and adding the next one.
4. **Track Maximum:** Keep the maximum possible number of satisfied customers.

### Time Complexity:

* **O(n)** — We iterate through the list once, maintaining a sliding window efficiently.

### Space Complexity:

* **O(1)** — Only a few integer variables are used.

### Why Sliding Window is Optimal:

* Instead of recalculating the same sums repeatedly, the sliding window reuses previous results, updating in constant time per step.
* It reduces time complexity from **O(n * m)** to **O(n)**, which is much faster for large inputs.

---

## Summary of Both Approaches

| Approach       | Time Complexity | Space Complexity | Efficiency         | Technique                   |
| -------------- | --------------- | ---------------- | ------------------ | --------------------------- |
| Brute Force    | O(n * m)        | O(1)             | Slower for large n | Nested Loops                |
| Sliding Window | O(n)            | O(1)             | Optimal            | Efficient Window Adjustment |

The **Sliding Window Solution** is the most optimal because it calculates the maximum potential satisfaction in linear time without redundant calculations.