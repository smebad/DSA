# Number of Zero-Filled Subarrays - LeetCode

## Problem Description

Given an integer array `nums`, return the number of subarrays that are completely filled with 0.

* A **subarray** is a contiguous non-empty sequence of elements within an array.

### Examples

**Example 1:**

```
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
- Single-element zero subarrays: [0], [0], [0], [0] → 4 occurrences
- Two-element zero subarrays: [0,0], [0,0] → 2 occurrences
- Total subarrays filled with 0 = 6
```

**Example 2:**

```
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
- Single-element zero subarrays: 5 occurrences
- Two-element zero subarrays: 3 occurrences
- Three-element zero subarray: 1 occurrence
- Total subarrays filled with 0 = 9
```

**Example 3:**

```
Input: nums = [2,10,2019]
Output: 0
Explanation: No zero-filled subarrays.
```

### Constraints

* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9

## Approach and Solution

We use a simple counting technique to calculate the number of zero-filled subarrays efficiently.

### Solution Explanation

1. Initialize two variables: `count` to keep track of consecutive zeros, and `res` to store the total number of zero-filled subarrays.
2. Iterate through each element of the array:

   * If the element is 0, increment `count` by 1.
   * If the element is not 0, reset `count` to 0.
   * Add `count` to `res` at each step.
3. Return `res` after iterating through the array.

The logic behind this approach:

* For a sequence of consecutive zeros of length `n`, the number of subarrays is the sum of the first `n` natural numbers: `1 + 2 + ... + n = n * (n + 1) / 2`.
* Instead of computing this formula for each block, we incrementally count using the `count` variable.

### Code with Comments

```python
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = count = 0  # Initialize result and current consecutive zero count

        for num in nums:
            if num == 0:
                count += 1  # Increase consecutive zero count
            else:
                count = 0  # Reset count if non-zero element encountered
            res += count  # Add current count to result, capturing all zero-filled subarrays

        return res
```

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the length of the array. We traverse the array once.
* **Space Complexity:** O(1), since we only use two extra variables (`count` and `res`).

### Why it is Optimal

* This solution efficiently counts all zero-filled subarrays in a single pass without extra data structures or nested loops.
* Using a formula for consecutive zeros implicitly while iterating makes it linear time and constant space, which is optimal for this problem.

## Test Cases

```python
solution = Solution()

# Test Case 1
nums1 = [1, 3, 0, 0, 2, 0, 0, 4]
print(solution.zeroFilledSubarray(nums1))  # Output: 6

# Test Case 2
nums2 = [0, 0, 0, 2, 0, 0]
print(solution.zeroFilledSubarray(nums2))  # Output: 9

# Test Case 3
nums3 = [2, 10, 2019]
print(solution.zeroFilledSubarray(nums3))  # Output: 0
```