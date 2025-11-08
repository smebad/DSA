# Sign of the Product of an Array - LeetCode

## Problem Explanation

The **Sign of the Product of an Array** problem requires determining whether the product of all elements in an integer array is positive, negative, or zero.

We define a helper function `signFunc(x)` as follows:

* Returns `1` if `x` is positive.
* Returns `-1` if `x` is negative.
* Returns `0` if `x` is equal to `0`.

Your task is to compute the product of all numbers in the array and return the **sign** of the result using `signFunc(product)`.

### Example 1

**Input:** `nums = [-1, -2, -3, -4, 3, 2, 1]`
**Output:** `1`
**Explanation:** Product = 144 → `signFunc(144)` = 1 (positive)

### Example 2

**Input:** `nums = [1, 5, 0, 2, -3]`
**Output:** `0`
**Explanation:** Product = 0 → `signFunc(0)` = 0

### Example 3

**Input:** `nums = [-1, 1, -1, 1, -1]`
**Output:** `-1`
**Explanation:** Product = -1 → `signFunc(-1)` = -1 (negative)

---

## Code Implementation and Comments

### Approach 1: Counting Negative Numbers

```python
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0  # Counter for negative numbers
        for num in nums:
            if num == 0:  # If any number is zero, the product will be zero
                return 0
            if num < 0:  # Count how many negative numbers exist
                neg += 1
        # If the count of negative numbers is odd, product is negative; else positive
        return -1 if neg % 2 else 1
```

### Approach 2: Tracking Product Sign Directly

```python
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1  # Assume the product starts positive
        for num in nums:
            if num == 0:  # If we find a zero, product is zero
                return 0
            if num < 0:   # Flip sign whenever we find a negative number
                sign *= -1
        return sign  # Return final sign after processing all numbers
```

---

## Solution Explanation

Both solutions aim to determine whether the final product is positive, negative, or zero — without actually calculating the potentially very large product.

### Approach 1: Counting Negatives

* Count how many negative numbers are in the array.
* If the number of negative numbers is **even**, their product is **positive**.
* If the number is **odd**, their product is **negative**.
* If any number is `0`, immediately return `0`.

**Example:**
`nums = [-1, -2, -3, -4, 3, 2, 1]` → 4 negatives → even → return `1`.

### Approach 2: Tracking Sign Multiplicatively

* Keep a variable `sign` that represents the current sign of the product.
* For each negative number, flip the sign (`sign *= -1`).
* If a `0` is found, return `0`.
* Return the final value of `sign`.

**Example:**
`nums = [-1, 1, -1, 1, -1]`
Step-by-step sign changes:
`1 → -1 → -1 → 1 → 1 → -1` → result = `-1`.

---

## Comparison of Approaches

| Feature                   | Counting Negatives           | Tracking Sign                      |
| ------------------------- | ---------------------------- | ---------------------------------- |
| **Logic**                 | Count total negative numbers | Flip sign for each negative number |
| **Memory Used**           | Uses an integer counter      | Uses a sign variable               |
| **Ease of Understanding** | Very intuitive for beginners | Slightly more compact and direct   |
| **Performance**           | Identical                    | Identical                          |

Both methods achieve the same result with `O(n)` time and `O(1)` space. The **Tracking Sign** approach is a bit more direct and is often considered more elegant.

---

## Complexity Analysis

### Time Complexity: **O(n)**

We iterate through the list once, checking each number. Both solutions perform a single pass.

### Space Complexity: **O(1)**

We use only a few variables (`neg` or `sign`), regardless of input size.

---

## Optimal Solution

Both approaches are optimal because:

* They avoid multiplying the entire array, which could cause overflow or unnecessary computation.
* They detect zeros early to avoid redundant processing.

However, **Approach 2 (Tracking Sign)** is slightly more concise and direct, making it preferable in clean coding and interview scenarios.

## Test Cases

``` python
sol = Solution()

# Test Case 1:
nums1 = [-1,-2,-3,-4,3,2,1]
print(sol.arraySign(nums1))  # Output: 1

# Test Case 2:
nums2 = [1,5,0,2,-3]
print(sol.arraySign(nums2))  # Output: 0

# Test Case 3:
nums3 = [-1,1,-1,1,-1]
print(sol.arraySign(nums3))  # Output: -1
```