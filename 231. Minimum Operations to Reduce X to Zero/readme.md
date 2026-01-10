# Minimum Operations to Reduce X to Zero - LeetCode

## Problem Description

The problem **"Minimum Operations to Reduce X to Zero"** asks you to find the minimum number of operations required to reduce a given integer `x` to exactly `0`.

You are given:

* An integer array `nums`
* An integer `x`

In one operation, you can:

* Remove the **leftmost** element from `nums`, or
* Remove the **rightmost** element from `nums`

When an element is removed, its value is subtracted from `x`. The array is modified after every operation.

Your goal is to **reduce `x` to exactly `0` using the minimum number of operations**. If it is not possible, return `-1`.

---

## Examples

### Example 1

```
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: Removing the last two elements (2 and 3) reduces x to zero.
```

### Example 2

```
Input: nums = [5,6,7,8,9], x = 4
Output: -1
Explanation: It is not possible to reduce x to zero.
```

### Example 3

```
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: Removing the first two elements and the last three elements reduces x to zero.
```

---

## Key Insight

Instead of thinking about **what to remove**, think about **what to keep**.

If the total sum of the array is `total`, then removing elements whose sum is `x` means **keeping a contiguous subarray whose sum is `total - x`**.

So the problem becomes:

> Find the **longest subarray** with sum `total - x`.

The answer will be:

```
number of operations = len(nums) - length_of_longest_subarray
```

---

## Sliding Window Solution

### Code With Comments

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x   # Sum of the subarray we want to keep
        cur_sum = 0             # Current window sum
        max_window = -1         # Length of longest valid subarray
        l = 0                   # Left pointer of the sliding window

        for r in range(len(nums)):  # Right pointer moves forward
            cur_sum += nums[r]

            # Shrink the window if the sum exceeds target
            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            # If we find a window with the exact target sum
            if cur_sum == target:
                max_window = max(max_window, r - l + 1)

        # If no valid subarray was found, return -1
        return -1 if max_window == -1 else len(nums) - max_window
```

---

## Step-by-Step Approach

1. Compute the total sum of the array.
2. Convert the problem into finding a **longest subarray with sum = total - x**.
3. Use a sliding window because all numbers are positive.
4. Expand the window with the right pointer.
5. Shrink the window from the left when the sum exceeds the target.
6. Track the longest valid window.
7. Subtract its length from the total array size to get the minimum operations.

---

## Logic Explained in Simple Words

* Removing numbers from the ends is the same as keeping some middle part.
* We want to keep the **largest possible middle subarray** whose sum is `total - x`.
* The more we keep, the fewer operations we need to perform.
* Sliding window works efficiently because all values in `nums` are positive.

---

## Time and Space Complexity

### Time Complexity: `O(n)`

* Each element is visited at most twice (once by the right pointer and once by the left pointer).

### Space Complexity: `O(1)`

* Only a few variables are used.
* No extra data structures are required.

---

## Why This Solution Is Optimal

* Any solution must look at all elements at least once.
* Sliding window achieves this with minimal overhead.
* No extra memory is used.
* This is the fastest and most memory-efficient approach possible for this problem.

---

## Test Cases

```python
solution = Solution()

nums1 = [1, 1, 4, 2, 3]
x1 = 5
print(solution.minOperations(nums1, x1))  # Output: 2

nums2 = [5, 6, 7, 8, 9]
x2 = 4
print(solution.minOperations(nums2, x2))  # Output: -1

nums3 = [3, 2, 20, 1, 1, 3]
x3 = 10
print(solution.minOperations(nums3, x3))  # Output: 5
```