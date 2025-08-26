# Sort Array By Parity - LeetCode

## Problem Explanation

The problem **Sort Array By Parity** asks us to rearrange an integer array `nums` so that all **even numbers** appear before all **odd numbers**. The order of even numbers among themselves and odd numbers among themselves does not matter, as long as all evens come first, followed by odds.

### Example 1:

Input: `nums = [3,1,2,4]`
Output: `[2,4,3,1]` (other valid outputs: `[4,2,3,1]`, `[2,4,1,3]`, `[4,2,1,3]`)

### Example 2:

Input: `nums = [0]`
Output: `[0]`

### Constraints:

* 1 <= nums.length <= 5000
* 0 <= nums\[i] <= 5000

---

## Code Implementations

### 1. Sorting Solution

```python
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Sort the list using a custom key.
        # The key "x & 1" returns 0 for even numbers and 1 for odd numbers.
        # So, all evens (0) will be placed before odds (1).
        nums.sort(key=lambda x: x & 1)
        return nums
```

**Explanation:**

* We use Python's built-in `sort()` method.
* The key function `x & 1` checks whether a number is even or odd.

  * If `x & 1 == 0` → the number is even.
  * If `x & 1 == 1` → the number is odd.
* Sorting ensures all even numbers come before odd numbers.

**Complexity:**

* Time Complexity: **O(n log n)**, because sorting takes O(n log n) time.
* Space Complexity: **O(1)** (in-place) or **O(n)** depending on the Python implementation.

This works but is **not optimal** since we do not need full sorting to just separate evens and odds.

---

### 2. Two Pointers Solution (Optimal)

```python
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0  # Left pointer to place the next even number
        for r in range(len(nums)):  # r scans through the array
            if nums[r] % 2 == 0:  # If the current number is even
                # Swap it with the element at index l
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  # Move left pointer forward
        return nums
```

**Explanation:**

* We maintain two pointers:

  * `r` scans through the entire array.
  * `l` keeps track of the position where the next even number should go.
* Whenever we find an even number, we swap it with the element at index `l` and move `l` forward.
* By the end, all evens will be placed before odds.

**Complexity:**

* Time Complexity: **O(n)**, since we only pass through the array once.
* Space Complexity: **O(1)**, as everything is done in-place without extra memory.

This is the **most optimal solution** for this problem.

---

## Differences Between the Two Solutions

* **Sorting Solution:** Simple and easy to understand but slower (**O(n log n)**). It does unnecessary work because it sorts instead of just separating.
* **Two Pointers Solution:** More efficient (**O(n)**) and optimal since it only rearranges elements without full sorting.

---

## Test Cases

```python
sol = Solution()

# Test Case 1:
nums1 = [3,1,2,4]
print(sol.sortArrayByParity(nums1))  # Output: [2,4,3,1] or any valid arrangement

# Test Case 2:
nums2 = [0]
print(sol.sortArrayByParity(nums2))  # Output: [0]

# Test Case 3:
nums3 = [1,3,5,7]
print(sol.sortArrayByParity(nums3))  # Output: [1,3,5,7] (no evens, array unchanged)

# Test Case 4:
nums4 = [2,4,6]
print(sol.sortArrayByParity(nums4))  # Output: [2,4,6] (all evens, array unchanged)
```

---

## Final Notes

* The **two pointers solution** is the recommended approach because it is **O(n) time and O(1) space**.
* The sorting solution works but should be avoided for larger arrays due to its extra time cost.