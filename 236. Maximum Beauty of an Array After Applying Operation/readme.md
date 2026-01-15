# Maximum Beauty of an Array After Applying Operation - LeetCode

## Problem Overview

You are given a 0-indexed integer array `nums` and a non-negative integer `k`.

You may perform **at most one operation on each index**. In one operation, you can replace `nums[i]` with **any integer in the range**:

```
[nums[i] - k, nums[i] + k]
```

After applying operations any number of times (or none), the **beauty of the array** is defined as:

> The length of the longest subsequence consisting of equal elements.

Your task is to return the **maximum possible beauty** after applying the operations optimally.

A subsequence does not need to be contiguous, but the relative order must remain the same.

---

## Key Insight

Because every element can be adjusted within a range of size `2k`, multiple different values can be **converted into the same number**.

So instead of thinking about the final value itself, we think in terms of:

> How many numbers can be adjusted to lie within the same range of width `2k`.

This turns the problem into a **range frequency problem**, which can be efficiently solved using sorting and a sliding window.

---

## Sliding Window Solution
### Code with Comments

```python
from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array
        # Sorting helps us group close values together
        nums.sort()

        res = 0   # Stores the maximum beauty found
        l = 0     # Left pointer of the sliding window

        # Step 2: Expand the window using the right pointer
        for r in range(len(nums)):
            # If the current window becomes invalid (range > 2k)
            # move the left pointer to shrink the window
            while nums[r] - nums[l] > 2 * k:
                l += 1

            # Update the maximum size of a valid window
            res = max(res, r - l + 1)

        return res
```

---

## How the Logic Works

### Why Sorting Helps

After sorting, all values that are close to each other appear together. This allows us to easily find the largest group of numbers that lie within a range of `2k`.

### Why `2k`?

Each number can be increased or decreased by at most `k`.

So two numbers `a` and `b` can be converted into the same value **if and only if**:

```
|a - b| ≤ 2k
```

That means any group of numbers where:

```
max_value - min_value ≤ 2k
```

can all be converted into the same number.

### Sliding Window Strategy

* The **left pointer `l`** marks the smallest value in the current group
* The **right pointer `r`** expands the group
* If the range becomes invalid, move `l` forward
* Keep track of the **largest valid window size**

That window size is the maximum possible beauty.

---

## Time and Space Complexity

### Time Complexity

* Sorting: **O(n log n)**
* Sliding window traversal: **O(n)**

Overall:

```
O(n log n)
```

### Space Complexity

* No extra data structures used
* Sorting is done in-place

```
O(1)
```

---

## Why This Solution Is Optimal

* The problem inherently requires ordering or grouping values
* Sorting is unavoidable for efficient range grouping
* Sliding window ensures **each element is processed once**
* No nested loops or extra memory

This makes it both **fast and memory-efficient**, well within the problem constraints.

---

## Example Walkthrough

### Input

```
nums = [4, 6, 1, 2]
k = 2
```

### Sorted

```
[1, 2, 4, 6]
```

### Valid Windows

* `[2, 4, 6]` → `6 - 2 = 4 ≤ 2k`

Maximum window size = **3**

### Output

```
3
```

---

## Test Cases
```python
solution = Solution()
nums1 = [4, 6, 1, 2]
k1 = 2
print(solution.maximumBeauty(nums1, k1))  # Output: 3

nums2 = [1, 1, 1, 1]
k2 = 10
print(solution.maximumBeauty(nums2, k2))  # Output: 4
```