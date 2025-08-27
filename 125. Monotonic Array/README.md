# Monotonic Array - LeetCode

## Problem Explanation

A **monotonic array** is an array that is either entirely non-increasing or non-decreasing:

* **Monotone increasing**: For every pair of indices `i <= j`, we have `nums[i] <= nums[j]`.
* **Monotone decreasing**: For every pair of indices `i <= j`, we have `nums[i] >= nums[j]`.

The task is to check if a given integer array `nums` is monotonic.

### Examples

* Input: `[1, 2, 2, 3]` → Output: `true` (monotone increasing)
* Input: `[6, 5, 4, 4]` → Output: `true` (monotone decreasing)
* Input: `[1, 3, 2]` → Output: `false` (not monotonic)

### Constraints

* `1 <= nums.length <= 10^5`
* `-10^5 <= nums[i] <= 10^5`

---

## Code with Explanation

```python
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Assume the array can be both increasing and decreasing initially
        increase, decrease = True, True

        # Traverse the array once
        for i in range(len(nums) - 1):
            # If a pair violates increasing property, set increase = False
            if not (nums[i] <= nums[i + 1]):
                increase = False
            # If a pair violates decreasing property, set decrease = False
            if not (nums[i] >= nums[i + 1]):
                decrease = False

        # If the array is either entirely increasing or decreasing, return True
        return increase or decrease
```

### Key Notes in Code

1. Two flags `increase` and `decrease` are used to keep track of whether the array could still be increasing or decreasing.
2. If any pair breaks the monotonic rule for one direction, that flag is set to `False`.
3. At the end, if at least one flag is `True`, the array is monotonic.

---

## Approach and Logic

There are two main ways to solve this problem:

1. **One-Pass Solution (Optimal)**

   * Traverse the array once.
   * Keep two flags (`increase` and `decrease`).
   * Update them as you find violations.
   * Return whether at least one of the flags remains `True`.

2. **Two-Pass Solution (Alternative)**

   * Check once if the array is monotone increasing.
   * Check again if it is monotone decreasing.
   * Return true if either check passes.
   * This approach is simpler but requires scanning the array twice.

**Difference:**

* The **one-pass solution** is more efficient since it combines both checks in a single traversal.
* The **two-pass solution** is easier to understand conceptually but is slightly less efficient.

---

## Complexity Analysis

* **Time Complexity**: `O(n)`, where `n` is the length of the array. We only make a single pass through the array.
* **Space Complexity**: `O(1)`, as we use only constant extra space for the two flags.

### Why This Is Optimal

* Any solution must look at all elements in the array to confirm monotonicity. Therefore, `O(n)` is the best achievable time complexity.
* Since the problem only requires logical checks without extra data structures, the constant space solution is the most efficient possible.

---

## Test Cases

```python
sol = Solution()

# Test Case 1: Monotone increasing
nums1 = [1, 2, 2, 3]
print(sol.isMonotonic(nums1))  # Output: True

# Test Case 2: Monotone decreasing
nums2 = [6, 5, 4, 4]
print(sol.isMonotonic(nums2))  # Output: True

# Test Case 3: Not monotonic
nums3 = [1, 3, 2]
print(sol.isMonotonic(nums3))  # Output: False
```

---

## Conclusion

The **one-pass solution** is both time and space optimal. It efficiently determines whether the array is monotonic by checking for both increasing and decreasing trends in a single traversal.