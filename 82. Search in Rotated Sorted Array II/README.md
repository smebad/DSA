# Search in Rotated Sorted Array II - LeetCode

## Problem Statement

Given a rotated sorted array `nums` (possibly containing duplicates), and an integer `target`, your task is to determine if the `target` exists in the array.

The array was originally sorted in non-decreasing order but then rotated at some pivot unknown to you beforehand. Your goal is to search for the target using as few steps as possible.

## Example

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

## Constraints

* 1 <= nums.length <= 5000
* -10^4 <= nums\[i] <= 10^4
* nums is rotated at an unknown pivot
* -10^4 <= target <= 10^4

## Follow-up

This problem is similar to "Search in Rotated Sorted Array", but in this version, `nums` may contain duplicates, which can affect the runtime complexity.

---

## Code Explanation (Binary Search Approach)

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2

            # Check if the middle element is the target
            if nums[m] == target:
                return True

            # If left part is sorted
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # If right part is sorted
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            # If we can't determine the sorted part due to duplicates
            else:
                l += 1

        return False
```

### Code Comments

* We use binary search logic with additional handling for duplicates.
* If the left side is sorted and the target lies within it, we move the right pointer.
* If the right side is sorted and the target lies within it, we move the left pointer.
* If there are duplicates and we can't determine the sorted half, we increment the left pointer to shrink the search space.

---

## Time and Space Complexity

### Time Complexity

* **Average case:** O(log n)
* **Worst case:** O(n), especially when the array contains many duplicate elements (e.g., `[1,1,1,1,1,1]`) which reduce the effectiveness of binary search.

### Space Complexity

* **O(1)**: Only a few integer variables are used regardless of input size.

## Why This Solution is Optimal

* This binary search adaptation works well even with duplicates by carefully adjusting the search space.
* While the worst case is linear, the average performance remains logarithmic, making it efficient for most practical inputs.

---

## Test Cases

```python
# Test Case 1
nums = [2,5,6,0,0,1,2]
target = 0
print(Solution().search(nums, target))  # Output: True

# Test Case 2
nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums, target))  # Output: False
```
