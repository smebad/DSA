# Divide Array Into Arrays With Max Difference - LeetCode

## Problem Description

"Divide Array Into Arrays With Max Difference" is a problem where you are given an integer array `nums` of size `n` (with `n` being a multiple of 3) and a positive integer `k`. You need to divide `nums` into `n / 3` arrays of size 3 such that the difference between any two elements in one array is less than or equal to `k`. If it is impossible, return an empty array. If multiple solutions exist, returning any valid one is acceptable.

### Examples

**Example 1:**

```text
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
```

**Example 2:**

```text
Input: nums = [2,4,2,2,5,2], k = 2
Output: []
```

**Example 3:**

```text
Input: nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
Output: [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
```

## Solution Code with Comments

```python
from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Sort the array to easily group elements with minimal difference
        nums.sort()
        res = []

        # Iterate over the array in chunks of size 3
        for i in range(0, len(nums), 3):
            # If the max difference in the current triplet exceeds k, return empty list
            if nums[i + 2] - nums[i] > k:
                return []
            # Otherwise, add the triplet to the result
            res.append(nums[i: i + 3])

        return res
```

## Solution Approach and Logic

1. **Sorting:** By sorting the array first, we ensure that numbers close to each other in value are adjacent. This allows us to form triplets where the maximum difference is minimized.
2. **Chunking:** We iterate through the sorted array in chunks of 3 elements because the problem explicitly requires arrays of size 3.
3. **Validation:** For each chunk, we check if the difference between the largest and smallest numbers exceeds `k`. If it does, it's impossible to form a valid array, so we return an empty list.
4. **Result Construction:** If the chunk satisfies the difference constraint, we append it to the result array.

### Key Points

* Sorting guarantees that the difference between the first and third elements in a triplet is the maximum difference in that group.
* By iterating in steps of 3, we directly form the required number of arrays.
* If at any point a triplet violates the `k` difference rule, we know it's impossible to satisfy the condition for all elements.

## Time and Space Complexity

* **Time Complexity:** `O(n log n)` due to sorting, where `n` is the length of `nums`.
* **Space Complexity:** `O(n)` for storing the resulting arrays.

This is optimal because any valid solution must examine all numbers at least once, and sorting is the most efficient way to group elements based on difference constraints.

## Test Cases

```python
sol = Solution()

# Test Case 1:
nums1 = [1,3,4,8,7,9,3,5,1]
k1 = 2
print(sol.divideArray(nums1, k1))  # Output: [[1,1,3],[3,4,5],[7,8,9]]

# Test Case 2:
nums2 = [2,4,2,2,5,2]
k2 = 2
print(sol.divideArray(nums2, k2))  # Output: []

# Test Case 3:
nums3 = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
k3 = 14
print(sol.divideArray(nums3, k3))  # Output: [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
```