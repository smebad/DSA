# Number of Ways to Split Array - LeetCode

## Problem Explanation

The **Number of Ways to Split Array** problem asks us to find how many valid ways we can split an array into two non-empty parts such that the **sum of the left part is greater than or equal to the sum of the right part**.

A split is considered valid if:

1. The sum of the first `(i + 1)` elements is **greater than or equal** to the sum of the remaining elements.
2. There is **at least one element** on the right side after the split (so we only check up to index `n - 2`).

### Example

**Input:** `nums = [10, 4, -8, 7]`
**Output:** `2`

**Explanation:**

* Split at index 0 → Left = [10], Right = [4, -8, 7] → 10 >= 3 (Valid)
* Split at index 1 → Left = [10, 4], Right = [-8, 7] → 14 >= -1 (Valid)
* Split at index 2 → Left = [10, 4, -8], Right = [7] → 6 < 7 (Invalid)

There are **2 valid splits**.

---

## Code Explanation

```python
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)  # Start by calculating the total sum of all elements.
        left = res = 0  # Initialize left sum and result counter.

        for i in range(len(nums) - 1):  # Iterate until the second last element.
            left += nums[i]  # Add the current number to the left sum.
            right -= nums[i]  # Subtract the same number from the right sum.

            # If left sum is greater than or equal to right sum, count it as valid.
            res += 1 if left >= right else 0

        return res  # Return the total count of valid splits.
```

### Key Points to Remember

* `right` keeps track of the remaining sum of elements on the right side.
* `left` keeps track of the sum of elements on the left side.
* We update both in every iteration.
* The check `left >= right` determines if a split is valid.

---

## Approach and Logic

1. **Prefix Sum Concept:**

   * The idea is to efficiently compute the sum of both left and right parts as we iterate through the array.
   * Instead of recalculating sums from scratch, we use a running total for `left` and `right`.

2. **Steps:**

   * Calculate the **total sum** of the array and store it in `right`.
   * Start iterating from the first element to the second last element.
   * In each iteration:

     * Add the current element to `left`.
     * Subtract the same element from `right`.
     * If `left >= right`, increment the count.

3. **Why it works:**

   * We efficiently track both halves in a single pass without needing extra arrays.
   * The condition ensures that we split only where the left sum is not smaller than the right sum.

4. **No Extra Structures:**

   * The solution works purely with integer variables, not with prefix arrays or auxiliary data.

---

## Complexity Analysis

### Time Complexity: **O(n)**

* We iterate through the array once, performing constant-time operations per element.
* This is the best possible complexity for this problem.

### Space Complexity: **O(1)**

* We use only a few variables (`left`, `right`, `res`) — independent of input size.

---

## Why This is Optimal

* Any valid solution must at least check each split position once, so **O(n)** is the theoretical lower bound.
* This approach achieves that bound using minimal memory.
* Prefix sum or cumulative tracking avoids redundant recalculation of subarray sums.

---

## Test Cases

```python
solution = Solution()

# Test Case 1
nums1 = [10, 4, -8, 7]
print(solution.waysToSplitArray(nums1))  # Output: 2

# Test Case 2
nums2 = [2, 3, 1, 0]
print(solution.waysToSplitArray(nums2))  # Output: 2
```