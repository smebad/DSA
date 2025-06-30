# Guess Sqrt(x) - LeetCode

## Problem Explanation

The "Guess Sqrt(x)" problem requires computing the integer square root of a given non-negative integer `x`. The result must be the largest integer `r` such that `r * r <= x`. The twist is that you are not allowed to use built-in power functions like `pow()` or exponentiation operators like `x ** 0.5` in Python.

### Example:

* Input: `x = 4`
  Output: `2`
  Explanation: The square root of 4 is 2, so we return 2.

* Input: `x = 8`
  Output: `2`
  Explanation: The square root of 8 is 2.828..., and we round it down to get 2.

### Constraints:

* `0 <= x <= 2^31 - 1`

---

## 1. Binary Search Solution

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m  # store the best guess so far
            else:
                return m  # perfect square found

        return res  # return the floored square root
```

### Approach:

* This uses a binary search between 0 and `x`.
* Each guess `m` is squared and compared with `x`.
* If `m * m` is more than `x`, we search the left half.
* If it is less, we store `m` and search the right half.

### Time Complexity:

* `O(log n)`: Because we halve the search range each time.

### Space Complexity:

* `O(1)`: No extra space used except variables.

### Why Optimal:

* Fastest for large inputs.
* Doesn’t require recursion or iteration up to `x`.

---

## 2. Recursion Solution

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = self.mySqrt(x >> 2) << 1  # Recurse on x // 4 and double the result
        r = l + 1
        return l if r * r > x else r
```

### Approach:

* Uses bit shifting to divide the problem size by 4 on each recursive call.
* Recursively finds the sqrt of `x // 4` and doubles the result.
* Tests if `r * r` exceeds `x` to finalize the answer.

### Time Complexity:

* `O(log n)` due to recursive halving.

### Space Complexity:

* `O(log n)` because of recursion stack.

### Pros:

* Very elegant and math-based.
* Slightly more overhead due to recursion.

---

## 3. Brute Force Solution

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        res = 1
        for i in range(1, x + 1):
            if i * i > x:
                return res
            res = i

        return res
```

### Approach:

* Start from 1 and go up to `x`, checking when `i * i > x`.
* The last valid `i` is the square root.

### Time Complexity:

* `O(sqrt(n))`

### Space Complexity:

* `O(1)`

### When to Use:

* Simple to write and understand.
* Works fine for small values of `x`.
* Not efficient for large inputs.

---

## Conclusion

Among the three approaches:

* **Binary Search** is the most optimal in terms of both time and space.
* **Recursion** is neat but adds space overhead.
* **Brute Force** is simplest but least efficient.

Use **Binary Search** for all practical purposes, especially under tight time constraints or large input sizes.

---

## Test Cases

```python
# Test Case 1:
x = 4
print(Solution().mySqrt(x))  # Output: 2

# Test Case 2:
x = 8
print(Solution().mySqrt(x))  # Output: 2

# Test Case 3:
x = 0
print(Solution().mySqrt(x))  # Output: 0
```