# Continuous Subarray Sum - LeetCode

## Problem Description

Given an integer array `nums` and an integer `k`, return `true` if there exists a **continuous subarray** of length at least two whose sum is a **multiple of `k`**. Otherwise, return `false`.

### A good subarray must:

* Contain **at least two elements**
* Have a sum that is a multiple of `k` (including zero, since 0 is always a multiple of any integer)

### Example

**Input:** `nums = [23,2,4,6,7], k = 6`
**Output:** `true`
**Explanation:** `[2,4]` sums to `6`, which is a multiple of `6`.

---

## Intuition

We need to check if any continuous subarray (length ≥ 2) has a sum divisible by `k`.

A naive approach would try all subarrays and check their sums, but that would be too slow (O(n²)).

A better way uses **prefix sum + remainder hashing**:

* Keep a running sum
* Track the **remainder** when dividing prefix sums by `k`
* If the **same remainder reappears**, it means the subarray between those two points has a sum divisible by `k`
* Ensure the subarray length is at least 2

---

## Solution Code (with comments)

```python
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store remainder and its first index
        # Initialize with remainder 0 at index -1 to handle cases from start
        remainder = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num  # prefix sum

            # Handle k = 0 separately to avoid division by zero
            if k != 0:
                r = total % k
            else:
                r = total

            # If remainder not seen before, store first occurrence
            if r not in remainder:
                remainder[r] = i
            # If seen and subarray length >= 2, return True
            elif i - remainder[r] > 1:
                return True

        return False
```

---

## Explanation for Beginners

* Prefix sum tracks cumulative total
* Remainders help detect if difference between prefix sums is divisible by `k`
* Using a hashmap avoids checking all subarrays manually

Example:
If prefix remainders seen are:

```
index:    0  1  2  3
nums:    23  2  4  6
remainders: [5, 1, 5, 5]
```

Remainder 5 repeats at index 0 and 2, so the subarray from index 1 to 2 sums to a multiple of k.

---

## Time and Space Complexity

| Approach                       | Time Complexity | Space Complexity | Explanation                     |
| ------------------------------ | --------------- | ---------------- | ------------------------------- |
| Prefix Sum + Hashmap (Optimal) | **O(n)**        | **O(k)**         | Tracks remainders efficiently   |

**Optimal Approach:** Prefix Sum + Remainder Hashmap

* Only one pass through array
* O(n) time makes it best for large inputs

---

## Key Takeaways

* Use prefix sum to track cumulative values
* Use hashmap to detect repeating remainders
* If remainder repeats and subarray is length ≥ 2, answer is true
* Efficient O(n) solution

---

## Test Cases

```python
# Test Case 1:
nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))  # Output: True

# Test Case 2:
nums = [23, 2, 6, 4, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))  # Output: True

# Test Case 3:
nums = [23, 2, 6, 4, 7]
k = 13
print(Solution().checkSubarraySum(nums, k))  # Output: False
```