# Minimum Size Subarray Sum - LeetCode

## Problem Description

The **Minimum Size Subarray Sum** problem asks us to find the **smallest length** of a contiguous subarray of which the **sum is greater than or equal to a given target**. If there is no such subarray, return 0.

You are given:

* A list of **positive integers** `nums`.
* A **positive integer** `target`.

Return the **minimal length** of a subarray whose sum is **≥ target**.

### Example 1:

* Input: `target = 7`, `nums = [2,3,1,2,4,3]`
* Output: `2`
* Explanation: The subarray `[4,3]` has the minimum required length.

### Example 2:

* Input: `target = 4`, `nums = [1,4,4]`
* Output: `1`

### Example 3:

* Input: `target = 11`, `nums = [1,1,1,1,1,1,1,1]`
* Output: `0`
* Explanation: No subarray meets the condition.

### Constraints:

* `1 <= target <= 10^9`
* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^4`

---

## Solution: Sliding Window

```python
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")  # Start with infinity as the minimum length

        for r in range(len(nums)):
            total += nums[r]  # Add current number to the running sum
            while total >= target:  # While our window sum is big enough
                res = min(r - l + 1, res)  # Update result if it's smaller
                total -= nums[l]  # Shrink the window from the left
                l += 1

        return 0 if res == float("inf") else res
```

### Code Explanation

* Use a **sliding window** with two pointers `l` (left) and `r` (right).
* Expand the window by moving `r` and adding to the sum.
* When the `sum` of the window reaches or exceeds `target`, try to **shrink** the window from the left (`l`) to find the minimum possible length.
* Keep updating the result with the smallest length found.
* If no valid subarray is found, return 0.

---

## Approach and Logic

The problem demands us to find the **smallest window** that meets a sum condition.

### Why Sliding Window?

* Because we are dealing with **contiguous subarrays** and need to adjust the size dynamically.
* Brute force (checking all subarrays) takes O(n^2), which is too slow for input sizes up to 10^5.

### Sliding Window Steps:

1. Start with `l = 0`, `total = 0`.
2. Expand the window by adding `nums[r]`.
3. While the `total >= target`, move the left pointer `l` to make the window smaller and check if the new window size is the smallest so far.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * Each element is processed at most twice (once added, once removed).
* **Space Complexity:** `O(1)`

  * Only pointers and a few variables are used.

### Why This is Optimal

* This solution passes all constraints efficiently.
* It avoids unnecessary computations by **greedily shrinking the window** only when the condition is met.
* It has both **linear time** and **constant space**, making it ideal for large inputs.

---

## Test Cases

```python
# Test Case 1:
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))  # Expected Output: 2

# Test Case 2:
target = 4
nums = [1,4,4]
print(Solution().minSubArrayLen(target, nums))  # Expected Output: 1

# Test Case 3:
target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums))  # Expected Output: 0
```
