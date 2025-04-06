# Product of Array Except Self - Leetcode Blind 75

## Problem Description
Given an integer array `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

### Constraints
- Each product is guaranteed to fit in a 32-bit integer.
- Solve it in O(n) time without using the division operation.

### Examples
**Example 1:**
```
Input: nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]
```
**Example 2:**
```
Input: nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]
```

## Solution 1: Brute Force Approach
In this approach, for every element in the array, we iterate over the array again and multiply all elements except the current one.

```python
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res
```

### Time Complexity: O(n^2)
### Space Complexity: O(1) (excluding output array)

---

## Solution 2: Optimal Prefix and Suffix Approach
This optimal approach uses two passes:
1. First pass to compute the prefix product for each element.
2. Second pass to multiply with postfix product from the right.

```python
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
```

### Time Complexity: O(n)
### Space Complexity: O(1) (excluding output array)

This is the most optimal and recommended solution.

---

## Test Cases
```python
# Test Case 1:
nums = [1, 2, 4, 6]
print(Solution().productExceptSelf(nums))  # Output: [48, 24, 12, 8]

# Test Case 2:
nums = [-1, 0, 1, 2, 3]
print(Solution().productExceptSelf(nums))  # Output: [0, -6, 0, 0, 0]

# Test Case 3:
nums = [0, 0, 0, 0]
print(Solution().productExceptSelf(nums))  # Output: [0, 0, 0, 0]
```

---

## Conclusion
- The brute force solution is easy to understand but inefficient.
- The prefix-postfix method is optimal in both time and space, and avoids division as required.
- This problem demonstrates efficient traversal techniques using prefix and postfix products for array manipulation.