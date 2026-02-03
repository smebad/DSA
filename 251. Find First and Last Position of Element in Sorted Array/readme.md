# Find First and Last Position of Element in Sorted Array - LeetCode

## Problem Overview

The problem **Find First and Last Position of Element in Sorted Array** is a classic **binary search** problem from LeetCode.

You are given:

* A list of integers `nums` sorted in **non-decreasing order**.
* An integer `target`.

Your task is to:

* Find the **first (leftmost)** and **last (rightmost)** positions of `target` in the array.
* If the `target` does not exist in the array, return `[-1, -1]`.

### Why this problem is important

Because the array is already sorted, a simple linear scan would work, but it would take **O(n)** time. The problem specifically requires a solution with **O(log n)** time complexity, which forces us to use **binary search**.

This problem helps in understanding:

* How to modify binary search for different goals
* How to find boundaries (first and last occurrence)
* Efficient searching in sorted arrays

---

## Given Examples

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3, 4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1, -1]

Input: nums = [], target = 0
Output: [-1, -1]
```

---

## Code With Comments

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the leftmost (first) occurrence of target
        left = self.binarySearch(nums, target, True)

        # Find the rightmost (last) occurrence of target
        right = self.binarySearch(nums, target, False)

        # Return both positions as a list
        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # This will store the index of target if found
        i = -1

        # Standard binary search loop
        while l <= r:
            # Find middle index
            m = (l + r) // 2

            if target > nums[m]:
                # Target is on the right side
                l = m + 1
            elif target < nums[m]:
                # Target is on the left side
                r = m - 1
            else:
                # Target found at index m
                i = m

                if leftBias:
                    # Move left to find the first occurrence
                    r = m - 1
                else:
                    # Move right to find the last occurrence
                    l = m + 1

        # Return the found index, or -1 if not found
        return i
```

---

## Explanation of the Approach

### Key Idea

Instead of finding the target once, we:

1. Run **binary search to find the first occurrence** of the target.
2. Run **binary search again to find the last occurrence** of the target.

The only difference between the two searches is the **direction we continue searching after finding the target**.

---

### How the Modified Binary Search Works

When we find `target` at index `m`:

* We do **not stop immediately**.
* We save the index in a variable.
* Then we continue searching:

  * Left side if we want the **first occurrence**.
  * Right side if we want the **last occurrence**.

This ensures we find the extreme positions of the target.

---

## Differences Between the Two Searches

| Search Type  | Purpose          | Behavior After Finding Target |
| ------------ | ---------------- | ----------------------------- |
| Left-biased  | First occurrence | Move `r = m - 1`              |
| Right-biased | Last occurrence  | Move `l = m + 1`              |

Both searches use the same logic, but the **bias flag** changes the direction of search.

---

## Time and Space Complexity

### Time Complexity

* Each binary search takes **O(log n)** time.
* We perform two binary searches.

**Total Time Complexity:**

```
O(log n)
```

---

### Space Complexity

* Only a few variables are used.
* No extra data structures are created.

**Space Complexity:**

```
O(1)
```

---

## Most Optimal Solution and Why

The provided solution is **optimal** because:

* It uses binary search, which is the fastest possible method for searching in a sorted array.
* It meets the problem requirement of **O(log n)** runtime.
* It uses constant extra space.

Any solution faster than this is not possible because even binary search requires checking at least `log n` elements.

---

## Test Cases
```python
# Test Case 1:
nums = [5, 7, 7, 8, 8, 10]
target = 8
sol = Solution()
print(sol.searchRange(nums, target))  # Output: [3, 4]

# Test Case 2:
nums = [5, 7, 7, 8, 8, 10]
target = 6
print(sol.searchRange(nums, target))  # Output: [-1, -1]
```