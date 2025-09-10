# Largest Substring Between Two Equal Characters - LeetCode

## Problem Explanation

The problem asks us to find the length of the **longest substring between two equal characters** in a given string `s`. The substring excludes the two equal characters themselves. If no such pair of equal characters exists, we return `-1`.

* A **substring** is a contiguous sequence of characters within a string.
* Example: In `"abca"`, the characters `a` at indices `0` and `3` form a substring `"bc"` between them. Its length is `2`.

### Examples

1. **Input:** `s = "aa"`
   **Output:** `0`
   Explanation: The only substring is empty (between the two `a`s).

2. **Input:** `s = "abca"`
   **Output:** `2`
   Explanation: Substring between the two `a`s is `"bc"`.

3. **Input:** `s = "cbzxy"`
   **Output:** `-1`
   Explanation: No characters appear twice.

### Constraints

* `1 <= s.length <= 300`
* `s` contains only lowercase English letters.

---

## Code Implementation with Comments

```python
# Hash Map Solution:
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}  # Dictionary to store the first occurrence index of each character
        res = -1         # Default result if no substring is found

        # Traverse the string with index and character
        for i, c in enumerate(s):
            if c in char_index:
                # If character was seen before, calculate substring length
                res = max(res, i - char_index[c] - 1)
            else:
                # Store the index of the first occurrence of the character
                char_index[c] = i

        return res
```

---

## Approach and Logic

1. **Store first occurrence:**

   * Use a dictionary (`char_index`) to store the index of the **first occurrence** of each character.

2. **Check repeating characters:**

   * When encountering the same character again, calculate the substring length between the current index and the stored first index (excluding both characters).
   * Formula: `i - char_index[c] - 1`

3. **Track maximum:**

   * Keep updating the result (`res`) with the maximum substring length found.

4. **Final result:**

   * If no repeating characters exist, the result remains `-1`.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * We traverse the string once, checking and updating the dictionary in constant time.

* **Space Complexity:** `O(1)`

  * Since there are only 26 lowercase English letters, the dictionary size is bounded by a constant.

---

## Why This Solution is Optimal

* The solution is **optimal** because it uses a **single pass** through the string (`O(n)`), storing only necessary information (first occurrence index).
* Any brute-force method (checking all substrings) would take `O(n^2)` time, which is inefficient for longer strings.
* Thus, this **hash-map solution** is the most efficient and optimal approach for the given constraints.

---

## Test Cases

```python
sol = Solution()

# Test Case 1:
s = "aa"
print(sol.maxLengthBetweenEqualCharacters(s))  # Output: 0

# Test Case 2:
s = "abca"
print(sol.maxLengthBetweenEqualCharacters(s))  # Output: 2

# Test Case 3:
s = "cbzxy"
print(sol.maxLengthBetweenEqualCharacters(s))  # Output: -1
```