# Apply Operations to an Array - LeetCode

## Problem Overview

The **Apply Operations to an Array** problem asks you to process a list of non-negative integers by applying a set of rules sequentially and then rearranging the array.

You are given a 0-indexed array `nums` of length `n`. You must perform `n - 1` operations in order:

1. For each index `i` from `0` to `n - 2`:

   * If `nums[i] == nums[i + 1]`, multiply `nums[i]` by `2` and set `nums[i + 1]` to `0`.
   * Otherwise, do nothing.
2. After all operations are applied, move all `0` values to the end of the array while keeping the relative order of non-zero elements the same.

The final array after these steps must be returned.

This problem mainly tests your understanding of:

* Sequential array updates
* In-place modification
* Two-pointer techniques

---

## Code With Comments

```python
from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Step 1: Apply the operations sequentially
        # We compare each element with the next one
        for i in range(len(nums) - 1):
            # If two adjacent elements are equal
            if nums[i] == nums[i + 1]:
                # Double the current element
                nums[i] *= 2
                # Set the next element to zero
                nums[i + 1] = 0

        # Step 2: Move all non-zero elements to the front
        # l keeps track of the position where the next non-zero should go
        l = 0
        for i in range(len(nums)):
            # If the current element is non-zero
            if nums[i] != 0:
                # Swap it with the element at index l
                nums[l], nums[i] = nums[i], nums[l]
                # Move l forward
                l += 1

        # The array is modified in place and returned
        return nums
```

---

## Solution Approach and Logic

### Step 1: Apply Operations

We iterate through the array from left to right and compare each element with the one next to it.

* If two adjacent values are equal, we:

  * Double the left value
  * Replace the right value with `0`
* Operations are applied immediately, so the updated array affects future comparisons

This matches the problem requirement that operations are applied sequentially, not all at once.

### Step 2: Shift Zeros to the End

After applying all operations, zeros may appear anywhere in the array. To fix this:

* We use a two-pointer technique
* One pointer (`i`) scans the array
* Another pointer (`l`) tracks where the next non-zero value should be placed

Every time we find a non-zero value, we swap it forward. This preserves the order of non-zero elements.

---

## Why This Approach Works Well

* The operations are applied in a single pass
* The zero-shifting is done in another single pass
* No extra arrays or data structures are used
* The array is modified directly, making the solution efficient and simple

This approach closely follows the problem statement and avoids unnecessary complexity.

---

## Time and Space Complexity

### Time Complexity

* Applying operations: `O(n)`
* Shifting zeros: `O(n)`

Overall time complexity:

```
O(n)
```

Where `n` is the length of the array.

### Space Complexity

```
O(1)
```

* The algorithm modifies the input array in place
* Only a few variables are used
* No additional space grows with input size

---

## Optimal Solution

The provided two-pointer solution is the most optimal for this problem because:

* It runs in linear time
* It uses constant extra space
* It avoids unnecessary array copies
* It follows the problem constraints exactly

Given the constraints and requirements, this is the best possible approach for solving this problem efficiently.

---

## Test Cases:
```python
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 2, 1, 1, 0]
    print(solution.applyOperations(nums1))  # Expected Output: [1, 4, 2, 0, 0, 0]

    # Test Case 2
    nums2 = [0, 1]
    print(solution.applyOperations(nums2))  # Expected Output: [1, 0]

    # Test Case 3
    nums3 = [2, 2, 2, 2]
    print(solution.applyOperations(nums3))  # Expected Output: [4, 4, 0, 0]

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print(solution.applyOperations(nums4))  # Expected Output: [2, 2, 1, 0, 0]

    # Test Case 5
    nums5 = [0, 0, 0]
    print(solution.applyOperations(nums5))  # Expected Output: [0, 0, 0]
```