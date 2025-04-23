# Longest Repeating Character Replacement

## Problem Description
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Example 1:
**Input:** `s = "ABAB"`, `k = 2`
**Output:** `4`
**Explanation:** Replace the two 'A's with two 'B's or vice versa.

### Example 2:
**Input:** `s = "AABABBA"`, `k = 1`
**Output:** `4`
**Explanation:** Replace one 'A' in the middle with 'B' to form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.

### Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## Brute Force Solution
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)  # Count the frequency of characters in current window
                maxf = max(maxf, count[s[j]])  # Track the max frequency
                if (j - i + 1) - maxf <= k:  # If we can replace at most k chars
                    res = max(res, j - i + 1)
        return res
```

### Time Complexity:
- **O(n^2)** where `n` is the length of the string `s`. The outer loop iterates `n` times, and the inner loop can also go up to `n`.

### Space Complexity:
- **O(1)** (since there are at most 26 uppercase English letters).

This brute force approach checks all possible substrings, making it inefficient for larger inputs.

---

## Sliding Window (Optimal) Solution
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0  # Maximum frequency of a single character in the window

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)  # Count character frequency
            maxf = max(maxf, count[s[r]])  # Update the maximum frequency in the window

            while (r - l + 1) - maxf > k:  # If we need to replace more than k characters
                count[s[l]] -= 1  # Shrink the window from the left
                l += 1

            res = max(res, r - l + 1)  # Update the result with max window size

        return res
```

### Explanation:
- We use a sliding window with two pointers (`l` and `r`).
- `count` keeps track of character frequencies in the current window.
- `maxf` keeps the maximum frequency of a single character within the window.
- If the number of characters we need to replace (`window size - maxf`) exceeds `k`, we move the left pointer `l` to shrink the window.
- We update the result `res` with the size of the valid window.

### Time Complexity:
- **O(n)**, where `n` is the length of the string. Each character is visited at most twice (once by the `r` pointer and once by the `l` pointer).

### Space Complexity:
- **O(m)** where `m` is the number of unique characters in the string. For uppercase English letters, it is **O(1)**.

This solution is optimal and efficient for large strings.

---

## Test Cases
```python
# Test Case 1:
s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))  # Expected Output: 4

# Test Case 2:
s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))  # Expected Output: 4
```