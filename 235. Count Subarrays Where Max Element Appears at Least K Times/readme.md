# Count Subarrays Where Max Element Appears at Least K Times – LeetCode

## 1. Problem Explanation

**Count Subarrays Where Max Element Appears at Least K Times** is a sliding window counting problem.

You are given:

* An integer array `nums`
* A positive integer `k`

Your task is to count how many **contiguous subarrays** exist such that the **maximum element of the entire array** appears **at least `k` times** inside that subarray.

### Important Clarification

* The maximum element is the **global maximum of `nums`**, not the maximum inside each subarray.
* A subarray is valid if this global maximum appears **`k` or more times** within it.

### Output

Return a single integer representing the number of valid subarrays.

---

## 2. Code With Comments

```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums)     # The maximum element in the entire array
        max_cnt = 0           # Counts occurrences of max_n in the current window
        l = 0                 # Left pointer of the sliding window
        res = 0               # Final count of valid subarrays

        # Move the right pointer through the array
        for r in range(len(nums)):

            # If current element is the maximum, increase its count
            if nums[r] == max_n:
                max_cnt += 1

            # Shrink the window while we have at least k max elements
            while max_cnt == k:
                if nums[l] == max_n:
                    max_cnt -= 1
                l += 1

            # All subarrays ending at r and starting before l are valid
            res += l

        return res
```

---

## 3. Solution Approach and Logic

### Key Insight

Instead of counting subarrays where the maximum appears **at least `k` times**, we track when it appears **exactly `k` times** and use that to count valid subarrays efficiently.

### Why Sliding Window Works

* Subarrays are contiguous
* We want to count all valid subarrays in a single pass
* Sliding window allows us to maintain the count dynamically

### How the Logic Works Step by Step

1. Identify the **global maximum element** in `nums`
2. Use two pointers `l` (left) and `r` (right) to define a window
3. Move `r` forward and count how many times the maximum appears
4. When the count reaches `k`:

   * Shrink the window from the left
   * Stop as soon as the count drops below `k`
5. At this point:

   * Any subarray ending at `r` and starting **before index `l`** is valid
   * Add `l` to the result

### Why `res += l` Works

* `l` represents the number of valid starting positions
* Each contributes a valid subarray ending at `r`

---

## 4. Time and Space Complexity

### Current and Optimal Solution

* **Time Complexity:** `O(n)`

  * Each element is processed once
  * Both pointers move only forward

* **Space Complexity:** `O(1)`

  * Only constant extra variables are used

### Why This Solution Is Optimal

* Any solution must inspect all elements at least once
* This approach avoids nested loops
* It achieves the lowest possible time complexity for this problem

---

## Test Cases

```python
sol = Solution()

# Test Case 1
nums = [1, 3, 2, 3, 3]
k = 2
print(sol.countSubarrays(nums, k))  # 6

# Test Case 2
nums = [1, 4, 2, 1]
k = 3
print(sol.countSubarrays(nums, k))  # 0
```