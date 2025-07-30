# Move Zeroes - LeetCode

## Problem Statement

The **"Move Zeroes"** problem requires us to take an array of integers `nums` and move all `0`s to the end of the array **while maintaining the relative order** of the non-zero elements. This must be done **in-place**, meaning the original array must be modified without making a copy of it.

### Example 1:

```python
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### Example 2:

```python
Input: nums = [0]
Output: [0]
```

### Constraints:

* `1 <= nums.length <= 10^4`
* `-2^31 <= nums[i] <= 2^31 - 1`
* Must perform the operation in-place

---

## Two Pointers Solution with Explanation and Comments

```python
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0  # Pointer to track the position of the last non-zero element

        # Iterate through the array with another pointer `r`
        for r in range(len(nums)):
            # If the current element is not zero, swap it with the element at index `l`
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  # Move the `l` pointer forward to the next position
```

### Step-by-Step Logic:

1. Use two pointers:

   * `l` (left pointer): keeps track of the position where the next non-zero should go.
   * `r` (right pointer): scans every element in the array.

2. If a non-zero is found at index `r`, it is swapped with the element at index `l`, and `l` is moved forward.

3. This continues until all non-zero elements are shifted to the beginning in their original order, and all zeros are pushed to the end.

---

## Why This Solution is Optimal

* The solution does exactly **one pass** over the array.
* It does **minimal operations**: only swapping when a non-zero element is found.
* It modifies the array **in-place** and doesn't use any extra memory.

---

## Time and Space Complexity

* **Time Complexity**: `O(n)` where `n` is the number of elements in the array. This is because each element is visited only once.
* **Space Complexity**: `O(1)` since no additional memory is used. The array is modified in-place.

---

## Test Cases

```python
# Test Case 1:
sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Test Case 2:
nums = [0]
sol.moveZeroes(nums)
print(nums)  # Output: [0]
```

---

## Summary

* The problem is about rearranging the array such that all zeroes go to the end and the order of non-zero elements remains unchanged.
* The two-pointer approach is both intuitive and optimal.
* Time complexity is linear, and no extra memory is used.
