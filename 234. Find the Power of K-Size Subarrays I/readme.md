# Find the Power of K-Size Subarrays I – LeetCode

## 1. Problem Explanation

**Find the Power of K-Size Subarrays I** is a sliding window problem.

You are given:

* An integer array `nums` of length `n`
* A positive integer `k`

You must examine **every contiguous subarray of size `k`** and compute its **power**.

### Definition of Power

A subarray has a valid power **only if**:

1. Its elements are **strictly increasing**
2. Each element is **exactly 1 greater than the previous element**

If both conditions are satisfied:

* The power is the **maximum element** of the subarray

Otherwise:

* The power is `-1`

### Output

Return an array `results` of size `n - k + 1`, where:

* `results[i]` is the power of subarray `nums[i .. i + k - 1]`

---

## 2. Code With Comments

```python
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []          # Stores the power of each k-size subarray
        l = 0             # Left pointer of the sliding window

        # Move the right pointer across the array
        for r in range(len(nums)):

            # If window size exceeds k, shrink it from the left
            if r - l + 1 > k:
                l += 1

            # When the window size is exactly k, evaluate the subarray
            if r - l + 1 == k:
                valid = True  # Assume the subarray is valid

                # Check if the subarray is strictly increasing and consecutive
                for i in range(l, r):
                    if nums[i + 1] != nums[i] + 1:
                        valid = False
                        break

                # If valid, the last element is the maximum
                # Otherwise, append -1
                res.append(nums[r] if valid else -1)

        return res
```

---

## 3. Solution Approach and Logic

### Key Idea

The problem requires checking **every contiguous subarray of size `k`**. Since subarrays overlap, a **sliding window** approach is used.

### How the Sliding Window Works

1. Two pointers `l` (left) and `r` (right) define a window
2. The window always maintains a size of `k`
3. When the window size becomes `k`:

   * We verify whether all adjacent elements satisfy:

     ```
     nums[i + 1] == nums[i] + 1
     ```
4. If all pairs satisfy the condition:

   * The subarray is valid
   * The power is the last element (`nums[r]`)
5. If any pair fails the condition:

   * The power is `-1`

### Why the Last Element Is the Maximum

Because the subarray must be **strictly increasing**, the largest value will always appear at the end of the window.

### Difference From Failed Optimized Attempts

* Some optimized approaches try to track consecutive counts dynamically
* These often fail due to overlapping window transitions
* This solution prioritizes **correctness and clarity** over aggressive optimization

---

## 4. Time and Space Complexity

### Current Solution

* **Time Complexity:** `O(n × k)`

  * Each window of size `k` may require checking up to `k - 1` elements
* **Space Complexity:** `O(1)`

  * Only constant extra variables are used (excluding output array)

### Most Optimal Approach (Conceptual)

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

### Why an O(n) Solution Is Difficult

* Consecutiveness can break at any point
* A single invalid element invalidates the entire window
* Tracking this efficiently without rechecking elements is non-trivial

Given the constraints (`n ≤ 500`), the current solution is efficient, readable, and reliable.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
print(sol.resultsArray(nums, k))  # [3, 4, -1, -1, -1]

# Test Case 2
nums = [2, 2, 2, 2, 2]
k = 4
print(sol.resultsArray(nums, k))  # [-1, -1]

# Test Case 3
nums = [3, 2, 3, 2, 3, 2]
k = 2
print(sol.resultsArray(nums, k))  # [-1, 3, -1, 3, -1]
```
