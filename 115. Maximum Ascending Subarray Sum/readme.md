# Maximum Ascending Subarray Sum - LeetCode

## Problem Description

Given an array of positive integers `nums`, return the maximum possible sum of a **strictly increasing subarray** in `nums`.

A **subarray** is a contiguous sequence of numbers in an array.

### Example 1:

**Input:**

```python
nums = [10, 20, 30, 5, 10, 50]
```

**Output:**

```
65
```

**Explanation:** `[5, 10, 50]` is the ascending subarray with the maximum sum of 65.

### Example 2:

**Input:**

```python
nums = [10, 20, 30, 40, 50]
```

**Output:**

```
150
```

**Explanation:** `[10, 20, 30, 40, 50]` is the ascending subarray with the maximum sum of 150.

### Example 3:

**Input:**

```python
nums = [12, 17, 15, 13, 10, 11, 12]
```

**Output:**

```
33
```

**Explanation:** `[10, 11, 12]` is the ascending subarray with the maximum sum of 33.

**Constraints:**

```
1 <= nums.length <= 100
1 <= nums[i] <= 100
```

---

## Iterative Solution (Efficient)

```python
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = curSum = nums[0]  # Initialize result and current sum with the first element

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  # If current number is not greater, start a new subarray sum
                curSum = 0

            curSum += nums[i]  # Add current number to current sum
            res = max(res, curSum)  # Update result if current sum is larger

        return res
```

### Step-by-step logic:

1. Start with the first element as both the `current sum` and the `result`.
2. Iterate through the array starting from index `1`.
3. If the current number is **not** greater than the previous one, reset the current sum (start new subarray).
4. Add the current number to the `current sum`.
5. Keep track of the largest sum found so far.
6. Return the result.

**Time Complexity:** `O(n)` — We loop through the array once.

**Space Complexity:** `O(1)` — We use only constant extra space.

This is the **most optimal solution** because it processes the array in a single pass without extra storage.

---

## Brute Force Solution (Simpler but Slower)

```python
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curSum = nums[i]  # Start sum from current element
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[j - 1]:  # Stop if sequence is not strictly increasing
                    break
                curSum += nums[j]  # Add to sum if ascending
            res = max(res, curSum)  # Update result if needed
        return res
```

### Step-by-step logic:

1. Start from each index `i` in the array.
2. For each `i`, keep adding elements until the ascending order breaks.
3. Track the maximum sum found.
4. Return the result.

**Time Complexity:** `O(n^2)` — Nested loops for checking all subarrays.

**Space Complexity:** `O(1)` — Only uses a few extra variables.

This solution is **less efficient** than the iterative one, but easier for beginners to understand.

---

## Differences Between Solutions

| Aspect                | Iterative Solution    | Brute Force Solution       |
| --------------------- | --------------------- | -------------------------- |
| Time Complexity       | `O(n)` (faster)       | `O(n^2)` (slower)          |
| Space Complexity      | `O(1)`                | `O(1)`                     |
| Ease of Understanding | Medium                | Easy                       |
| Practical Use         | Best for large inputs | Only good for small inputs |

**Why Iterative is Optimal:**

* It scans the array **once** instead of checking every possible subarray.
* It resets the sum immediately when the ascending order breaks, making it more efficient.