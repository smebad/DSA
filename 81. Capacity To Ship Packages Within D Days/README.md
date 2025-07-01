# Capacity To Ship Packages Within D Days - LeetCode

## Problem Description

Given a list of package weights placed on a conveyor belt and an integer `days`, the task is to determine the minimum capacity a ship must have to ship all the packages within exactly `days` days. The packages must be shipped in the given order, and the ship cannot carry more weight than its capacity on a single day.

## Examples

### Example 1:

**Input:** `weights = [1,2,3,4,5,6,7,8,9,10]`, `days = 5`
**Output:** `15`
**Explanation:** Minimum capacity to ship in 5 days:

* Day 1: 1, 2, 3, 4, 5
* Day 2: 6, 7
* Day 3: 8
* Day 4: 9
* Day 5: 10

### Example 2:

**Input:** `weights = [3,2,2,4,1,4]`, `days = 3`
**Output:** `6`

### Example 3:

**Input:** `weights = [1,2,3,1,1]`, `days = 4`
**Output:** `3`

## Constraints

* `1 <= days <= weights.length <= 5 * 10^4`
* `1 <= weights[i] <= 500`

## Solution Approach

We solve this using **Binary Search on the answer**:

* The **minimum capacity** must be at least the maximum weight in the list (i.e., `max(weights)`), otherwise that item won't fit.
* The **maximum capacity** could be the sum of all weights (i.e., `sum(weights)`), which means shipping everything in one day.

### Binary Search Steps

1. Set left = `max(weights)`, right = `sum(weights)`
2. Perform binary search to find the minimum valid capacity
3. For each capacity guess, use a helper function `canShip(capacity)` to determine if the packages can be shipped within `days`

### Helper Function: `canShip(cap)`

Simulates loading packages one by one:

* Add a package to current ship until the ship is full
* If full, increase ship count and start a new ship
* If ships exceed `days`, return False

## Code Explanation

```python
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)  # Min and max capacity bounds
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1  # Try a smaller capacity
            else:
                l = cap + 1  # Increase capacity

        return res
```

### Code Comments

* `l, r = max(weights), sum(weights)`: initial binary search range
* `canShip(cap)`: checks if all packages can be shipped with given capacity
* `while l <= r`: standard binary search loop
* `res = min(res, cap)`: update result to lower capacity when valid

## Complexity Analysis

* **Time Complexity:** `O(n log(sum(weights) - max(weights)))`

  * `O(log(range))` binary search steps
  * `O(n)` for each capacity check
* **Space Complexity:** `O(1)` as only constant space is used

## Optimality

The binary search solution is optimal for this problem:

* Avoids brute-force checking of all capacities
* Efficient even for large inputs (up to 50,000 items)
* Time complexity is logarithmic with respect to capacity range, and linear in input size

## Test Cases

```python
# Test Case 1:
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))  # Expected Output: 15

# Test Case 2:
weights = [3,2,2,4,1,4]
days = 3
print(Solution().shipWithinDays(weights, days))  # Expected Output: 6

# Test Case 3:
weights = [1,2,3,1,1]
days = 4
print(Solution().shipWithinDays(weights, days))  # Expected Output: 3
```
