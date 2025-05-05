# Binary Search - LeetCode

## Problem Statement

Given a sorted array of integers `nums` in ascending order, and a target integer `target`, implement a function to search for the `target` in `nums`. If the target exists, return its index. Otherwise, return `-1`.

The algorithm must run in **O(log n)** time complexity.

---

## What is Binary Search?

Binary Search is a classic divide and conquer algorithm used to efficiently search for a target element in a **sorted** array. Instead of scanning every element linearly (O(n)), it repeatedly divides the search interval in half, leading to a logarithmic time complexity.

### Key Idea

* Start with the whole array as the search space.
* Compare the target with the middle element.

  * If equal, return the index.
  * If the target is smaller, search in the left half.
  * If the target is larger, search in the right half.

This process continues until the element is found or the search space becomes empty.

---

## Iterative Binary Search Solution

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Define left and right boundaries

        while l <= r:
            # Prevents integer overflow in languages with fixed integer sizes
            m = l + ((r - l) // 2)  # Find the middle index

            if nums[m] > target:
                r = m - 1  # Target is in the left half
            elif nums[m] < target:
                l = m + 1  # Target is in the right half
            else:
                return m  # Target found

        return -1  # Target not found
```

### Step-by-Step Code Explanation:

* Initialize pointers `l` and `r` to the start and end of the list.
* Calculate the middle index `m` using `l + ((r - l) // 2)`.
* Compare `nums[m]` with `target`:

  * If greater, discard the right half.
  * If smaller, discard the left half.
  * If equal, return the index `m`.
* If the loop exits, return `-1`.

### Time and Space Complexity:

* **Time Complexity:** `O(log n)` because the array is halved each iteration.
* **Space Complexity:** `O(1)` since only constant extra space is used.

---

## Lower Bound Binary Search

Useful for finding the **first occurrence** of the target.

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m  # Keep the lower half
            else:
                l = m + 1  # Discard the lower half

        return l if (l < len(nums) and nums[l] == target) else -1
```

### Time and Space Complexity:

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Upper Bound Binary Search

Useful for finding the **last occurrence** of the target.

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m  # Keep the lower half
            else:
                l = m + 1  # Discard the lower half

        return l - 1 if (l and nums[l - 1] == target) else -1
```

### Time and Space Complexity:

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Test Cases

```python
# Test Case 1:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
sol = Solution()
print(sol.search(nums, target))  # Output: 4

# Test Case 2:
nums = [-1, 0, 3, 5, 9, 12]
target = 2
sol = Solution()
print(sol.search(nums, target))  # Output: -1

# Test Case 3:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
sol = Solution()
print(sol.search(nums, target))  # Output: 4
```

---

## Summary

Binary search is an essential algorithm in computer science with optimal logarithmic time complexity. The iterative approach is widely used for its efficiency. Lower and upper bound variants offer more control for range based searches like finding the first or last occurrences.

Always ensure the array is sorted before applying binary search.
