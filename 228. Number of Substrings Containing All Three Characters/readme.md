# Number of Substrings Containing All Three Characters - LeetCode

## Problem Description

"Number of Substrings Containing All Three Characters" is a problem where you are given a string `s` consisting only of the characters `a`, `b`, and `c`. Your task is to find the total number of substrings that contain at least one occurrence of all three characters.

### Examples

**Example 1:**

```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing 'a', 'b', and 'c' include "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc", and "abc".
```

**Example 2:**

```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing all three characters are "aaacb", "aacb", and "acb".
```

**Example 3:**

```
Input: s = "abc"
Output: 1
Explanation: The entire string "abc" is the only valid substring.
```

### Constraints

* `3 <= s.length <= 5 * 10^4`
* `s` only contains the characters `'a'`, `'b'`, and `'c'`.

## Solution

We can solve this problem efficiently using a **sliding window approach**.

### Code Explanation with Comments

```python
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0  # Left pointer of the sliding window
        res = 0  # Result to store number of valid substrings
        count = defaultdict(int)  # Dictionary to keep track of character counts

        for r in range(len(s)):  # Right pointer of the sliding window
            count[s[r]] += 1  # Include current character in the window

            # Shrink the window from the left while all three characters are present
            while len(count) == 3:
                res += len(s) - r  # All substrings ending from r to end are valid
                count[s[l]] -= 1  # Remove character at left pointer
                if count[s[l]] == 0:  # If count becomes zero, remove from dictionary
                    count.pop(s[l])
                l += 1  # Move left pointer to shrink window

        return res
```

### Approach and Logic

1. Use a **sliding window** with two pointers: `l` (left) and `r` (right).
2. Expand the window by moving `r` and include the current character in a `count` dictionary.
3. Once all three characters are present (`len(count) == 3`), every substring starting from `l` and ending from `r` to the end of the string is valid. Add this to `res`.
4. Shrink the window by moving `l` forward and updating the `count` dictionary.
5. Continue until `r` reaches the end of the string.

This ensures we efficiently count all substrings containing `a`, `b`, and `c` without checking every possible substring individually.

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the length of the string `s`. Each character is processed at most twice (once by `r` and once by `l`).
* **Space Complexity:** O(1), because the `count` dictionary will contain at most three keys (`'a'`, `'b'`, `'c'`).

### Why Optimal

This approach is optimal because:

* We avoid generating all substrings, which would be O(n^2).
* Using the sliding window ensures each character is considered only a few times.
* Constant extra space is used.

## Test Cases

```python
solution = Solution()

# Test Case 1
s = "abcabc"
print(solution.numberOfSubstrings(s))  # Output: 10

# Test Case 2
s = "aaacb"
print(solution.numberOfSubstrings(s))  # Output: 3

# Test Case 3
s = "abc"
print(solution.numberOfSubstrings(s))  # Output: 1
```