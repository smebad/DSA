# Minimum Difference Between Highest and Lowest of K Scores - LeetCode

## Problem Explanation

The problem **Minimum Difference Between Highest and Lowest of K Scores** requires us to select `k` students' scores from an array `nums` such that the difference between the maximum and minimum score in that selection is minimized.

In simple words: we want to pick `k` scores that are as close together as possible.

### Example

* Input: `nums = [9, 4, 1, 7]`, `k = 2`
* Possible selections: `[9, 4]`, `[9, 1]`, `[9, 7]`, `[4, 1]`, `[7, 4]`, `[7, 1]`
* Differences: `5, 8, 2, 3, 3, 6`
* Minimum difference = `2` (from `[9, 7]`).

Thus, the answer is `2`.

---

## Code with Comments

```python
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array so that close values are next to each other
        nums.sort()
        
        # Step 2: Use two pointers (sliding window of size k)
        l, r = 0, k - 1
        
        # Step 3: Initialize result with infinity (so any real difference will be smaller)
        res = float("inf")
        
        # Step 4: Slide the window of size k across sorted nums
        while r < len(nums):
            # Difference between highest (nums[r]) and lowest (nums[l]) in current window
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        
        # Step 5: Return the minimum difference found
        return res
```

---

## Approach and Logic

1. **Sorting**: Sorting arranges numbers in increasing order. This helps because the closest `k` numbers will always be next to each other in the sorted list.

2. **Sliding Window**: After sorting, instead of checking all combinations of size `k` (which would be very slow), we only need to check windows of `k` consecutive numbers.

   * For each window, compute the difference between the last and first element.
   * Keep track of the smallest difference.

3. **Result**: The smallest difference found is the minimum possible.

### Why This Works

Sorting ensures that the closest possible `k` numbers appear together. Thus, scanning consecutive groups is sufficient to guarantee the optimal answer.

---

## Complexity Analysis

* **Time Complexity**:

  * Sorting takes **O(n log n)**.
  * Sliding window traversal takes **O(n)**.
  * Total = **O(n log n)**, dominated by sorting.

* **Space Complexity**:

  * Sorting requires **O(log n)** space (depending on the sorting algorithm).
  * Sliding window uses constant space.
  * Total = **O(1)** extra space (ignoring sorting overhead).

---

## Why This Solution is Optimal

* A brute force approach would try all combinations of `k` elements, which is **O(n choose k)** and infeasible for larger inputs.
* Sorting + sliding window reduces the problem to just **O(n log n)**, which is efficient and scalable.
* Since sorting is necessary to align close numbers together, this is the most optimal approach.

---

## Test Cases

```python
sol = Solution()

# Test Case 1: Single element
nums1 = [90]
k1 = 1
print(sol.minimumDifference(nums1, k1))  # Output: 0

# Test Case 2: Small array
nums2 = [9, 4, 1, 7]
k2 = 2
print(sol.minimumDifference(nums2, k2))  # Output: 2

# Test Case 3: Larger range
nums3 = [10, 20, 30, 100, 200]
k3 = 3
print(sol.minimumDifference(nums3, k3))  # Output: 20 (from [10, 20, 30])
```