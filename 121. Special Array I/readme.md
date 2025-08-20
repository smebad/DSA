# Special Array I - LeetCode

## Problem Explanation

An array is considered **special** if the parity (evenness or oddness) of every pair of adjacent elements is different. This means:

* If one element in the pair is even, the other must be odd.
* No two adjacent elements can both be even or both be odd.

You are given an integer array `nums`. The task is to return `true` if `nums` is a special array, otherwise return `false`.

### Examples

**Example 1:**

```
Input: nums = [1]
Output: true
Explanation: There is only one element, so there are no adjacent pairs to compare. By definition, the array is special.
```

**Example 2:**

```
Input: nums = [2, 1, 4]
Output: true
Explanation: Adjacent pairs are (2,1) and (1,4). Both pairs contain one even and one odd number, so the array is special.
```

**Example 3:**

```
Input: nums = [4, 3, 1, 6]
Output: false
Explanation: The pair (3,1) has two odd numbers. Therefore, the array is not special.
```

### Constraints

* 1 <= nums.length <= 100
* 1 <= nums\[i] <= 100

---

## Code Explanation with Comments

### Solution 1: Modulo Comparison

```python
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Traverse the array from the 2nd element to the end
        for i in range(1, len(nums)):
            # If two adjacent numbers have the same parity (both even or both odd)
            if nums[i - 1] % 2 == nums[i] % 2:
                return False  # Not a special array
        return True  # Passed all checks, so it's special
```

### Solution 2: Bitwise AND Comparison

```python
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Traverse the array from the 2nd element to the end
        for i in range(1, len(nums)):
            # Use bitwise AND (&) with 1 to check parity
            # (num & 1 == 0) → even, (num & 1 == 1) → odd
            if nums[i - 1] & 1 == nums[i] & 1:
                return False  # Not a special array
        return True  # Passed all checks, so it's special
```

---

## Approaches and Logic

1. **Modulo Comparison Approach**

   * For each adjacent pair, check `num % 2`.
   * If both remainders are the same, they are either both even or both odd.
   * If this happens, return `false`.
   * If all adjacent pairs are alternating, return `true`.

2. **Bitwise AND Approach**

   * Instead of using `% 2`, we check parity with `num & 1`.
   * `num & 1` extracts the least significant bit:

     * Even numbers end with `0` in binary → `num & 1 == 0`.
     * Odd numbers end with `1` in binary → `num & 1 == 1`.
   * The logic is the same: if two adjacent results are equal, return `false`. Otherwise, return `true`.

---

## Differences Between the Solutions

* **Modulo Method:** Uses division and remainder to check even/odd.
* **Bitwise Method:** Uses binary representation and bitwise operations.

Both methods achieve the same result, but the bitwise approach is slightly faster in low-level computation because it avoids division. However, in Python, the performance difference is negligible.

---

## Time and Space Complexity

### Modulo Solution

* **Time Complexity:** O(n), because we check each adjacent pair once.
* **Space Complexity:** O(1), no extra data structures are used.

### Bitwise Solution

* **Time Complexity:** O(n), for the same reason as above.
* **Space Complexity:** O(1), constant extra space.

---

## Most Optimal Solution

Both solutions are equally optimal for this problem:

* Time Complexity: O(n)
* Space Complexity: O(1)

The **bitwise approach** can be considered slightly more optimal in terms of raw efficiency since bitwise operations are generally faster than modulo. However, in Python, the difference is negligible, so either solution is perfectly fine.