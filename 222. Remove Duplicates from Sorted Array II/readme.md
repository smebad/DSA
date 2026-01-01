# Remove Duplicates from Sorted Array II - LeetCode

## Problem Description

You are given a sorted integer array `nums` in non-decreasing order. The task is to remove duplicates **in-place** such that each unique element appears **at most twice**. The relative order of elements should remain the same.

Since the length of the array cannot be changed in some programming languages, the first `k` elements of `nums` should contain the final result after removing extra duplicates. Return `k`, the number of elements after removing duplicates.

**Constraints:**

* `1 <= nums.length <= 3 * 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` is sorted in non-decreasing order

## Example

**Example 1:**

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

## Solution Explanation

We can solve this efficiently using the **two pointers technique**:

### Approach

1. Use two pointers: `l` for the position to write into and `r` for iterating through the array.
2. For each unique number, count how many times it appears consecutively.
3. Copy the number into the array at most **twice**.
4. Continue until all elements are processed.
5. Return `l` as the new length of the array.

### Step-by-step Logic

* Initialize `l = 0` and `r = 0`.
* While `r < len(nums)`:

  * Count consecutive duplicates of `nums[r]`.
  * Copy `nums[r]` to `nums[l]` **min(2, count)** times.
  * Increment `r` to move to the next new element.
* `l` now points to the length of the array with at most two duplicates.

This approach ensures:

* **In-place modification:** no extra array is used.
* **Order preservation:** numbers are written sequentially.

## Code with Comments

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0  # l = write pointer, r = read pointer

        while r < len(nums):
            count = 1
            # Count duplicates for current element
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            # Write element at most twice
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1  # Move to next new element

        return l  # Return the new length of the array
```

## Complexity Analysis

* **Time Complexity:** O(n), because we traverse the array once with the right pointer.
* **Space Complexity:** O(1), since we are modifying the input array in-place and using constant extra space.
* **Optimality:** This is optimal because we process each element exactly once and maintain in-place modification without additional data structures.

## Test Cases

```python
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    print(f"Output: {k1}, nums = {nums1[:k1]}")  # Expected: Output: 5, nums = [1, 1, 2, 2, 3]

    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    print(f"Output: {k2}, nums = {nums2[:k2]}")  # Expected: Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
```