# Squares of a Sorted Array - LeetCode

## Problem Description

The **Squares of a Sorted Array** problem asks you to take a non-decreasing sorted integer array and return a new array of the squares of each number, also sorted in non-decreasing order.

### Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

### Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

### Constraints:

* 1 <= nums.length <= 10^4
* -10^4 <= nums\[i] <= 10^4
* nums is sorted in non-decreasing order

### Follow-Up:

Can you find a solution with O(n) time complexity?

---

## Code and Comments

### Sorting Solution:

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square each number in the array
        for i in range(len(nums)):
            nums[i] *= nums[i]
        # Sort the squared numbers
        nums.sort()
        return nums
```

### Two-Pointers Solution:

```python
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, res = 0, len(nums) - 1, []  # Initialize left and right pointers, and result list

        while l <= r:
            # Compare squares of left and right values
            if (nums[l] * nums[l]) > (nums[r] * nums[r]):
                res.append(nums[l] * nums[l])  # Append larger square value
                l += 1  # Move left pointer right
            else:
                res.append(nums[r] * nums[r])  # Append larger square value
                r -= 1  # Move right pointer left

        return res[::-1]  # Reverse the result list to get sorted order
```

---

## Explanation of Solutions

### 1. Sorting Solution

* This solution first squares each element in the input array.
* Then, it sorts the array.
* It works correctly but does not use the fact that the original array is already sorted.

### 2. Two-Pointers Solution

* This solution uses two pointers: one starting at the beginning (`l`) and the other at the end (`r`) of the array.
* It compares the squares of the values pointed to by `l` and `r`, and appends the larger square to the result list.
* Since we append the largest square first, we reverse the list at the end to get the sorted order.
* This method leverages the sorted nature of the input array to avoid sorting afterward.

---

## Time and Space Complexity

### Sorting Solution:

* **Time Complexity**: O(n log n), due to the sorting step.
* **Space Complexity**: O(1) if done in-place, otherwise O(n) if a new array is created.

### Two-Pointers Solution:

* **Time Complexity**: O(n), as each element is visited exactly once.
* **Space Complexity**: O(n), for the result array.

---

## Which One is Optimal?

The **Two-Pointers Solution** is the most optimal:

* It runs in linear time, O(n), which is better than O(n log n).
* It avoids the need to sort the array again.
* It makes intelligent use of the already sorted input array.

This makes the two-pointer approach preferable for performance-sensitive use cases and larger input sizes.

---

## Test Cases

```python
# Test Case 1:
nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))  # Expected Output: [0, 1, 9, 16, 100]

# Test Case 2:
nums = [-7, -3, 2, 3, 11]
print(Solution().sortedSquares(nums))  # Expected Output: [4, 9, 9, 49, 121]
```