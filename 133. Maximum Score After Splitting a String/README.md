# Maximum Score After Splitting a String - LeetCode

## Problem Explanation

The problem asks us to split a binary string (containing only `0`s and `1`s) into two **non-empty substrings** such that the score is maximized. The score is calculated as:

* The number of `0`s in the **left substring**
* Plus the number of `1`s in the **right substring**

We need to determine the **maximum possible score** after splitting.

### Example Walkthrough

**Input:** `s = "011101"`

All possible splits and their scores:

* `"0" | "11101"` → `1 + 4 = 5`
* `"01" | "1101"` → `1 + 3 = 4`
* `"011" | "101"` → `1 + 2 = 3`
* `"0111" | "01"` → `1 + 1 = 2`
* `"01110" | "1"` → `2 + 1 = 3`

The maximum score is **5**.

---

## Code with Explanation

```python
class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0                 # keeps track of number of zeros in the left substring
        one = s.count('1')       # total number of ones initially (entire string as right substring)
        res = 0                  # stores the maximum score found

        # Iterate through string, but stop before the last character to ensure non-empty right substring
        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1        # moving a '0' to the left substring
            else:
                one -= 1         # moving a '1' out of the right substring

            # Calculate current score and update maximum if higher
            res = max(res, zero + one)

        return res
```

---

## Solution Approach

### Iteration Solution

1. **Count total number of `1`s** in the string initially. This represents the number of ones in the right substring when no split is made yet.
2. **Iterate through the string** (excluding the last character to ensure the right part is non-empty):

   * If the current character is `0`, it moves to the left substring → increment left zeros.
   * If the current character is `1`, it moves out of the right substring → decrement right ones.
3. At each step, calculate `zeros in left + ones in right`.
4. Keep track of the **maximum score** encountered.

### Key Idea

The algorithm works by dynamically adjusting the counts of zeros and ones as we "slide" the split point across the string. This avoids recalculating counts for each split, making it efficient.

---

## Differences in Solutions

* **Naive approach (not implemented here):** Check every possible split, count zeros and ones separately each time. This would take **O(n²)** time.
* **Current solution:** Keeps running counts of zeros and ones while iterating once across the string. This reduces complexity to **O(n)**.

The provided solution is the **most optimal** one.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * We count the total ones once (`O(n)`)
  * We iterate once through the string (`O(n)`)
  * Total → `O(n)`

* **Space Complexity:** `O(1)`

  * We use only a few variables (`zero`, `one`, `res`)
  * No extra data structures are used.

### Why this is Optimal

* Since we need to inspect each character at least once, `O(n)` is the best possible time complexity.
* The algorithm achieves this with constant space, making it optimal in both **time and space**.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
s = "011101"
print(sol.maxScore(s))  # Expected output: 5

# Test Case 2
s = "00111"
print(sol.maxScore(s))  # Expected output: 5

# Test Case 3
s = "1111"
print(sol.maxScore(s))  # Expected output: 3
```