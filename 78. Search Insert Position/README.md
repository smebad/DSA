# Search Insert Position - LeetCode

## Problem Description

The **Search Insert Position** problem requires determining the index at which a target value should be inserted into a sorted list of distinct integers to maintain the list's order. If the target is already present, return its index.

You must solve the problem with an algorithm that runs in **O(log n)** time.

### Constraints:

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* All integers in `nums` are distinct and sorted in ascending order
* `-10^4 <= target <= 10^4`

---

## Binary Search Solution (Optimal)

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        # If target is not found, return the insertion position
        return left
```

### Time Complexity: `O(log n)`

* We halve the search range in each iteration, making it logarithmic.

### Space Complexity: `O(1)`

* Only a few integer variables are used regardless of input size.

### Why It's Optimal:

This is the most efficient solution for large datasets due to its logarithmic time complexity, as required by the problem.

---

## Linear Search Solution (Simpler but Less Efficient)

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Iterate through the list
        for i in range(len(nums)):
            # If current number is greater than or equal to target, insert here
            if nums[i] >= target:
                return i

        # If target is greater than all elements, insert at the end
        return len(nums)
```

### Time Complexity: `O(n)`

* In the worst case, we might have to check every element.

### Space Complexity: `O(1)`

* Constant extra space.

### When to Use:

* Only suitable when `nums` is very small or binary search is not permitted.

---

## Test Cases

```python
# Binary Search Tests
sol = Solution()

nums1 = [1, 3, 5, 6]
target1 = 5
print(sol.searchInsert(nums1, target1))  # Output: 2

nums2 = [1, 3, 5, 6]
target2 = 2
print(sol.searchInsert(nums2, target2))  # Output: 1

nums3 = [1, 3, 5, 6]
target3 = 7
print(sol.searchInsert(nums3, target3))  # Output: 4
```
