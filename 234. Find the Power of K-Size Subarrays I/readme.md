# Find the Power of K-Size Subarrays I - LeetCode

## 1. Problem Explanation

**Find the Power of K-Size Subarrays I** is a sliding window problem where you are given:

* An integer array `nums` of length `n`
* A positive integer `k`

You must examine **every contiguous subarray of size `k`** and calculate its **power**.

### Definition of Power

A subarray has a valid power **only if**:

1. Its elements are **sorted in strictly ascending order**
2. All elements are **consecutive** (each next element is exactly `+1` from the previous)

If both conditions are satisfied, the power is:

* The **maximum element** of that subarray

Otherwise:

* The power is `-1`

### Output

Return an array `results` of size `n - k + 1` where:

* `results[i]` is the power of subarray `nums[i .. i + k - 1]`

---

## 2. Code With Comments
```python
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []              # Stores final power values for each window
        l = 0                 # Left pointer of sliding window
        consec_count = 1      # Counts how many consecutive pairs exist

        for r in range(len(nums)):  # Right pointer moves through array

            # Check if current and previous elements are consecutive
            if r > 0 and nums[r] == nums[r - 1] + 1:
                consec_count += 1

            # If window size exceeds k, shrink from the left
            if r - l + 1 > k:
                # If the outgoing pair was consecutive, reduce count
                if nums[l] + 1 == nums[l + 1]:
                    consec_count -= 1
                l += 1

            # When window size is exactly k
            if r - l + 1 == k:
                # If all k elements form k-1 consecutive pairs
                if consec_count == k:
                    res.append(nums[r])  # Max element (last element)
                else:
                    res.append(-1)

        return res
```

---

## 3. Solution Approach and Logic

### Key Idea

Instead of checking each subarray from scratch, we use a **sliding window** technique.

### Why Sliding Window?

* Each valid subarray is **contiguous**
* Sliding window avoids recomputing the same values repeatedly

### How the Logic Works

1. Two pointers (`l` and `r`) define a window of size `k`
2. As `r` moves forward:

   * We check if `nums[r]` is consecutive to `nums[r-1]`
   * If yes, we increase `consec_count`
3. If window size exceeds `k`:

   * Move `l` forward
   * Adjust `consec_count` if a valid consecutive pair leaves the window
4. When window size becomes exactly `k`:

   * If the number of consecutive transitions equals `k - 1`

     * The subarray is valid
     * Append the maximum element
   * Otherwise, append `-1`

### Why `k - 1` Consecutive Checks?

A subarray of size `k` needs **k - 1 consecutive relationships** to be strictly increasing.

Example:

```
[1, 2, 3]
1→2, 2→3 → 2 consecutive pairs (k - 1)
```

---

## 4. Time and Space Complexity

### Current Solution

* **Time Complexity:** `O(n * k)`

  * Because `max(nums[l:r+1])` is computed for each window
* **Space Complexity:** `O(1)`

  * Only constant extra variables are used

### Most Optimal Approach

The optimal approach achieves:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

### Why Is It Optimal?

* The maximum element in a valid window is always the **last element**
* No need to call `max()` repeatedly
* Each element is processed only once

### Optimized Insight

If a window is valid:

```python
max_value = nums[r]
```

This removes the expensive `max()` call and makes the algorithm linear.

---

## Test Cases:
```python
# Test Cases:
sol = Solution()

# Test Case 1
nums = [1,2,3,4,3,2,5]
k = 3
print(sol.resultsArray(nums, k))

# Test Case 2 
nums = [2,2,2,2,2]
k = 4
print(sol.resultsArray(nums, k))

# Test Case 3
nums = [3,2,3,2,3,2]
k = 2
print(sol.resultsArray(nums, k))
```
