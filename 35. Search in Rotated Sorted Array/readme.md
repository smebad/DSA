# Search in Rotated Sorted Array - LeetCode

## Problem Statement

Given an array `nums` sorted in ascending order and possibly rotated at an unknown pivot, and an integer `target`, return the index of `target` if it exists in `nums`, otherwise return -1. The algorithm must run in O(log n) time.

### Example 1:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3:

```
Input: nums = [1], target = 0
Output: -1
```

## Constraints

* 1 <= nums.length <= 5000
* -10^4 <= nums\[i] <= 10^4
* All values of nums are unique.
* nums is an ascending array that is possibly rotated.
* -10^4 <= target <= 10^4

---

## Brute Force Solution

```python
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

### Explanation

This method iterates through every element in the array and checks if it matches the target.

### Time and Space Complexity

* **Time Complexity:** O(n) — In the worst case, every element is checked.
* **Space Complexity:** O(1) — No extra space is used.

---

## Optimal Solution: One-pass Binary Search

```python
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # Determine which side is properly sorted
            if nums[l] <= nums[mid]:
                # Target is not in the left sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # Target is not in the right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
```

### Explanation

* Use two pointers `l` and `r` to define the current search range.
* Calculate `mid` each time to compare with the target.
* Check if the left or right side is sorted.
* Use the sorted side to decide where to move the search space.

### Time and Space Complexity

* **Time Complexity:** O(log n) — Each iteration halves the search space.
* **Space Complexity:** O(1) — No additional space is used.

---

## Comparison of Approaches

| Approach      | Time Complexity | Space Complexity | Efficiency     |
| ------------- | --------------- | ---------------- | -------------- |
| Brute Force   | O(n)            | O(1)             | Not optimal    |
| Binary Search | O(log n)        | O(1)             | Most efficient |

### Why Binary Search is Optimal

* Utilizes the sorted and rotated nature of the array to reduce search time.
* Meets the problem constraint of O(log n) time.
* Efficient even for large arrays due to logarithmic time reduction.

---

## Test Cases

```python
# Test Case 1:
nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))  # Output: 4

# Test Case 2:
nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums, target))  # Output: -1

# Test Case 3:
nums = [1]
target = 0
print(Solution().search(nums, target))  # Output: -1
```

---

## Summary

The binary search solution is the optimal way to solve the Search in Rotated Sorted Array problem, fulfilling the O(log n) time constraint. While brute force is simpler to implement, it doesn't scale well. Understanding which half of the array is sorted helps narrow down the search efficiently.
