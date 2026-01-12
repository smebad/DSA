# Max Consecutive Ones III - LeetCode

## Problem Description

The problem **"Max Consecutive Ones III"** asks you to find the longest contiguous subarray containing only `1`s after flipping at most `k` zeros to ones.

You are given:

* A binary array `nums` (containing only `0` and `1`)
* An integer `k` representing the maximum number of `0`s you are allowed to flip

Each flip turns a `0` into a `1`. The goal is to return the **maximum length of consecutive ones** that can be achieved.

---

## Examples

### Example 1

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
```

By flipping two zeros, we can form a longest subarray of six consecutive ones.

### Example 2

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
```

Flipping three zeros allows a subarray of length ten.

---

## Sliding Window Solution

This problem is best solved using a **sliding window** technique, which efficiently keeps track of a valid window containing at most `k` zeros.

### Code With Comments

```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0          # Left pointer of the sliding window
        res = 0        # Stores the maximum window size

        for r in range(len(nums)):  # Right pointer expands the window
            # If current element is 0, we need to flip it
            if nums[r] == 0:
                k -= 1

            # If we used more than k flips, shrink window from left
            while k < 0:
                if nums[l] == 0:
                    k += 1          # Restore one flip when removing a zero
                l += 1

            # Update the maximum length found so far
            res = max(res, r - l + 1)

        return res
```

---

## Step-by-Step Approach

1. Initialize two pointers (`l` and `r`) to form a sliding window.
2. Move the right pointer and include elements in the window.
3. Decrease `k` when encountering a zero (using a flip).
4. If `k` becomes negative, move the left pointer to restore validity.
5. Track the maximum valid window size.

---

## Logic Explained in Simple Words

* Think of the window as a stretch of numbers where zeros can be flipped.
* You are allowed only `k` flips at a time.
* If too many zeros enter the window, move the left side forward.
* Keep updating the longest valid window.

---

## Time and Space Complexity

### Time Complexity: `O(n)`

* Each element is visited at most twice.

### Space Complexity: `O(1)`

* Only constant extra space is used.

---

## Why This Solution Is Optimal

* Any correct solution must inspect every element at least once.
* Sliding window ensures minimal operations.
* No additional data structures are required.
* This approach is the most efficient possible under the constraints.

---

## Test Cases

```python
solution = Solution()

nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
print(solution.longestOnes(nums1, k1))  # Output: 6

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3
print(solution.longestOnes(nums2, k2))  # Output: 10

nums3 = [1,0,1,0,1]
k3 = 1
print(solution.longestOnes(nums3, k3))  # Output: 4
```