# Maximum Width Ramp - LeetCode

## 1. Problem Explanation

You are given an integer array `nums`. A **ramp** is a pair of indices `(i, j)` such that:

* `i < j`
* `nums[i] <= nums[j]`

The **width** of a ramp is `j - i`. Your task is to find the **maximum width** among all valid ramps. If no such pair exists, return `0`.

This problem asks you to find two positions as far apart as possible while still satisfying the condition that the value on the left is less than or equal to the value on the right.

---

## 2. Code With Comments

```python
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # max_right[i] will store the maximum value from index i to the end of the array
        max_right = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0

        # Build the max_right array by scanning from right to left
        for n in reversed(nums):
            max_right[i] = max(n, prev_max)  # max value seen so far from the right
            prev_max = max_right[i]
            i -= 1

        res = 0  # stores the maximum ramp width
        l = 0    # left pointer

        # Iterate with right pointer
        for r in range(len(nums)):
            # Move left pointer until nums[l] <= max_right[r]
            # This ensures there exists some j >= r where nums[j] >= nums[l]
            while nums[l] > max_right[r]:
                l += 1
            # Update the maximum width
            res = max(res, r - l)
        
        return res
```

---

## 3. Solution Approach and Logic

### Key Idea

For each index `i`, we want to find the farthest `j` to the right such that `nums[i] <= nums[j]`. Brute force checking all pairs would be too slow, so we optimize using preprocessing and two pointers.

### Step 1: Precompute Right Maximums

We build an array `max_right` where `max_right[i]` is the maximum value from index `i` to the end of the array. This tells us the best possible `nums[j]` we can get for any `j >= i`.

Example:
If `nums = [6, 0, 8, 2, 1, 5]`
Then `max_right = [8, 8, 8, 5, 5, 5]`

### Step 2: Sliding Window with Two Pointers

We use two pointers `l` and `r`:

* `r` moves from left to right
* `l` moves forward only when necessary

For a given `r`, we check if `nums[l] <= max_right[r]`. If not, it means no valid `j >= r` can satisfy the ramp condition with this `l`, so we increase `l`.

Once the condition is satisfied, we know there exists some `j >= r` such that `nums[j] >= nums[l]`, so `(l, r)` can form a ramp. We update the width as `r - l`.

### Why This Works

The `max_right` array guarantees that if `nums[l] <= max_right[r]`, then there exists at least one valid `j` to the right of `r`.

This allows us to safely move pointers in linear time without missing any valid ramp.

---

## 4. Time and Space Complexity

### Current Solution

* **Time Complexity:** `O(n)`

  * One pass to build `max_right`
  * One pass with the two pointers

* **Space Complexity:** `O(n)`

  * Extra array `max_right` is used

### Most Optimal Approach

There is also a stack-based solution that achieves:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Both approaches are optimal in time. The stack solution uses a monotonic stack to track decreasing indices and then scans from the right to compute widths. The sliding window with `max_right` is often easier to understand and implement.

This solution is optimal because each element is processed only a constant number of times, and no nested loops are used.

---

## 5. Test Cases
```python
# Test Case 1:
nums1 = [6,0,8,2,1,5]
print(Solution().maxWidthRamp(nums1)) # 4

# Test Case 2:
nums2 = [9,8,1,0,1,9,4,0,4,1]
print(Solution().maxWidthRamp(nums2)) # 7
```