# Koko Eating Bananas - LeetCode

## Problem Description

Koko loves to eat bananas. There are `n` piles of bananas, where the `i-th` pile has `piles[i]` bananas. The guards who monitor her will return in `h` hours. Koko can choose an integer speed `k`, representing how many bananas she eats per hour. Each hour, she eats `k` bananas from any single pile. If the pile has fewer than `k` bananas, she eats all of them and spends the rest of that hour idle.

Koko wants to eat slowly but also finish eating all the bananas before the guards return. The goal is to return the **minimum integer speed `k`** such that she can eat all the bananas within `h` hours.

### Example 1

**Input**: `piles = [3,6,7,11], h = 8`
**Output**: `4`

### Example 2

**Input**: `piles = [30,11,23,4,20], h = 5`
**Output**: `30`

### Example 3

**Input**: `piles = [30,11,23,4,20], h = 6`
**Output**: `23`

### Constraints

* `1 <= piles.length <= 10^4`
* `piles.length <= h <= 10^9`
* `1 <= piles[i] <= 10^9`

---

## Brute Force Solution

```python
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1  # Start with the minimum possible speed
        while True:
            totalTime = 0
            for pile in piles:
                # Ceiling division using (pile + speed - 1) // speed
                totalTime += (pile + speed - 1) // speed
            if totalTime <= h:
                return speed  # Found the minimum speed that works
            speed += 1  # Try a faster speed
```

### Explanation:

* Try every speed from 1 up to a large number.
* For each speed, compute how many hours Koko would need.
* Use ceiling division to calculate how many hours a pile takes.
* If total hours needed is less than or equal to `h`, return that speed.

### Time & Space Complexity:

* **Time Complexity**: O(n \* m) where `n = len(piles)` and `m = max(piles)` (worst-case speed check).
* **Space Complexity**: O(1), only a few variables are used.

---

## Optimized Binary Search Solution

```python
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # Range of possible speeds
        res = r  # Initialize result with the upper bound

        while l <= r:
            k = (l + r) // 2  # Mid-point speed
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)  # Time to eat each pile
            if totalTime <= h:
                res = k  # This speed works, try to find a smaller one
                r = k - 1
            else:
                l = k + 1  # Speed too slow, try faster
        return res
```

### Explanation:

* Use binary search to minimize the value of `k`.
* For each `k`, simulate how long it takes to eat all the piles.
* If the time is within `h`, store `k` as a potential result and try smaller speeds.
* Otherwise, increase the speed.

### Time & Space Complexity:

* **Time Complexity**: O(n \* log m), where `n = len(piles)` and `m = max(piles)`.
* **Space Complexity**: O(1)

### Why Binary Search is Optimal:

The brute-force approach has linear complexity in the worst case with respect to `max(piles)`, which could be up to 10^9. Binary search reduces the number of iterations from `O(m)` to `O(log m)`, drastically improving performance, especially when piles are large.

---

## Summary

* The problem is a good example of applying binary search on the answer.
* The brute-force solution works but is not feasible for large inputs.
* The optimal solution uses binary search, leveraging the monotonic nature of the time taken with respect to the speed.

---

## Test Cases

```python
# Test Case 1
piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))  # Expected Output: 4

# Test Case 2
piles = [30,11,23,4,20]
h = 5
print(Solution().minEatingSpeed(piles, h))  # Expected Output: 30

# Test Case 3
piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))  # Expected Output: 23
```
