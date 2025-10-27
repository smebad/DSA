# Binary Subarrays With Sum - LeetCode

## Problem Explanation

The **Binary Subarrays With Sum** problem asks us to find how many contiguous subarrays (subsections of an array) have a sum equal to a given target `goal`. The array consists only of binary digits (0s and 1s).

A **subarray** means we must take consecutive elements — we cannot skip elements.

### Example

**Input:** `nums = [1,0,1,0,1]`, `goal = 2`
**Output:** `4`
**Explanation:** The 4 subarrays whose sums equal 2 are:

1. `[1,0,1]`
2. `[0,1,0,1]`
3. `[1,0,1,0]`
4. `[1,0,1]` (starting at index 2)

The problem can also be seen as counting all continuous parts of the array where the number of 1s equals `goal`.

---

## Code Explanation

```python
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Helper function to count subarrays with sum <= x
        def helper(x):
            if x < 0:
                return 0
            res = l = cur = 0
            for r in range(len(nums)):
                # Add current element to running sum
                cur += nums[r]
                # If sum exceeds x, move left pointer to reduce window
                while cur > x:
                    cur -= nums[l]
                    l += 1
                # Count all valid subarrays ending at r
                res += (r - l + 1)
            return res

        # Number of subarrays with sum == goal
        # = subarrays with sum <= goal - subarrays with sum <= goal-1
        return helper(goal) - helper(goal - 1)
```

### Code Walkthrough

1. The `helper(x)` function counts how many subarrays have a **sum less than or equal to x**.
2. It uses the **sliding window** technique:

   * Expand the right pointer `r` and keep adding to `cur`.
   * If `cur > x`, move the left pointer `l` to reduce the window.
   * Add `(r - l + 1)` to `res` because all subarrays ending at `r` and starting from any index between `l` and `r` are valid.
3. The main function then uses the property:

   `Subarrays with sum == goal = helper(goal) - helper(goal - 1)`

   This counts the exact subarrays whose sum equals the goal.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)` — The array is traversed twice (once for each helper call), but each traversal is linear.
* **Space Complexity:** `O(1)` — Only a few integer variables are used.

---

## Why This Solution is Optimal

* The **sliding window** approach leverages the binary nature of the array.
* It avoids extra data structures (like hash maps), resulting in constant space.
* Sorting or brute force methods would be too slow (O(n²)), making this O(n) approach optimal.

---

## Test Cases

```python
# Test Case 1
nums1 = [1, 0, 1, 0, 1]
goal1 = 2
print(Solution().numSubarraysWithSum(nums1, goal1))  # Expected Output: 4

# Test Case 2
nums2 = [0, 0, 0, 0, 0]
goal2 = 0
print(Solution().numSubarraysWithSum(nums2, goal2))  # Expected Output: 15
```