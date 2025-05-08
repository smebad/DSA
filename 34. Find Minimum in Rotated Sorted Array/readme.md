# Find Minimum in Rotated Sorted Array - LeetCode

## Problem Description

You are given a rotated sorted array of unique integers. Your task is to find the minimum element in the array. The array was originally sorted in ascending order but then rotated between 1 and n times.

### Examples:

* Input: `nums = [3,4,5,1,2]` -> Output: `1`
* Input: `nums = [4,5,6,7,0,1,2]` -> Output: `0`
* Input: `nums = [11,13,15,17]` -> Output: `11`

### Constraints:

* `1 <= nums.length <= 5000`
* `-5000 <= nums[i] <= 5000`
* All the integers of nums are unique
* nums is sorted and rotated between 1 and n times

### Goal:

Design an algorithm that runs in O(log n) time.

---

## Brute Force Solution

```python
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
```

### Time & Space Complexity:

* **Time Complexity:** O(n) — Linear scan to find the minimum.
* **Space Complexity:** O(1) — No extra space used.

**Drawback:** Does not meet the required O(log n) time complexity.

---

## Optimized Binary Search Solution

```python
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]  # Initialize result with the first element
        l, r = 0, len(nums) - 1  # Pointers to start and end of array

        while l <= r:
            # If the subarray is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2  # Midpoint
            res = min(res, nums[m])  # Update result

            # Determine which side to search
            if nums[m] >= nums[l]:  # Left side is sorted
                l = m + 1
            else:  # Pivot is in the left half
                r = m - 1

        return res
```

### Explanation of the Approach:

* The algorithm uses binary search to locate the smallest element in the array.
* It compares the `mid` element with the `left` and `right` pointers to determine which half of the array to search next.
* If the current subarray is sorted (i.e., `nums[l] < nums[r]`), then `nums[l]` is the minimum.
* Otherwise, it updates the result with the minimum of `nums[m]` and narrows down the search space.

### Time & Space Complexity:

* **Time Complexity:** O(log n) — Each iteration halves the search space.
* **Space Complexity:** O(1) — Only a few pointers and variables are used.

### Why This is Optimal:

* Meets the required logarithmic time constraint.
* Avoids scanning the whole array.
* Works correctly even if the array was rotated close to `n` times.

---

## Summary:

* Use brute force only for small inputs or non-time-sensitive problems.
* For optimal performance and large inputs, binary search ensures that you find the minimum in O(log n) time.
* The binary search leverages the sorted and rotated nature of the array to prune the search space efficiently.