# Get Equal Substrings Within Budget - LeetCode

## Problem Explanation

The **Get Equal Substrings Within Budget** problem asks us to find the longest substring of a string `s` that can be changed to match the corresponding substring in another string `t` without exceeding a given cost.

Each character change from `s[i]` to `t[i]` costs `|s[i] - t[i]|` (the absolute difference between their ASCII values). The goal is to determine the maximum length of a substring that can be transformed within the specified `maxCost`.

### Example

**Input:**

```
s = "abcd"
t = "bcdf"
maxCost = 3
```

**Output:**

```
3
```

**Explanation:**

* The substring `"abc"` in `s` can change to `"bcd"` in `t`.
* The total cost is `|a-b| + |b-c| + |c-d| = 1 + 1 + 1 = 3`, which is within the budget.
* Hence, the maximum possible substring length is `3`.

---

## Code Explanation (with Comments)

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0  # Keeps track of the total cost of the current window
        l = 0        # Left pointer of the window
        res = 0      # Stores the maximum length found

        for r in range(len(s)):  # Iterate with the right pointer
            curCost += abs(ord(s[r]) - ord(t[r]))  # Add cost of current character

            # If total cost exceeds the budget, shrink window from the left
            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1  # Move left pointer rightwards

            # Update the maximum length if current window is valid
            res = max(res, r - l + 1)

        return res
```

---

## Solution Approach

### Sliding Window Technique

This problem is efficiently solved using the **sliding window** approach.

#### Logic:

1. We use two pointers: **`l` (left)** and **`r` (right)** to form a dynamic window.
2. As the right pointer moves through the string, we accumulate the cost of transforming characters.
3. If the total cost exceeds `maxCost`, we move the left pointer to the right to reduce the cost.
4. The goal is to keep the window as large as possible while staying within budget.

This method ensures that we explore all possible substrings without recalculating costs repeatedly.

---

## Why Sliding Window is Efficient

* Instead of checking all possible substrings (which would be O(n²)), we adjust the window dynamically.
* Each character is processed **only twice** (once when entering the window and once when leaving).
* This reduces the time complexity to **O(n)**.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`
  Each character is visited at most twice (once by `r` and once by `l`), making the approach linear in time.

* **Space Complexity:** `O(1)`
  Only a few variables are used (`curCost`, `l`, `r`, `res`), and no additional data structures are required.

---

## Why This is the Most Optimal Solution

* The sliding window approach is **optimal** because:

  * It avoids recomputation by maintaining a running cost.
  * It ensures we always have the longest valid substring in a single pass.
  * No extra space is needed beyond simple variables.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
s = "abcd"
t = "bcdf"
maxCost = 3
print(sol.equalSubstring(s, t, maxCost))  # Output: 3

# Test Case 2
s = "abcd"
t = "cdef"
maxCost = 3
print(sol.equalSubstring(s, t, maxCost))  # Output: 1

# Test Case 3
s = "abcd"
t = "acde"
maxCost = 0
print(sol.equalSubstring(s, t, maxCost))  # Output: 1
```