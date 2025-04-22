# Longest Substring Without Repeating Characters - LeetCode

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

### Examples:

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

**Note:** The answer must be a substring, not a subsequence.

## Constraints
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces.

---

## Brute Force Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
```

### Explanation
- Loop through every possible starting point `i` of the string.
- For every start index `i`, create a new set to store unique characters.
- Loop from `j = i` to the end of the string.
- If the character is already in the set, break out of the inner loop.
- Otherwise, add the character to the set.
- Keep track of the maximum length found.

### Time Complexity:
- **O(n * m)** where `n` is the length of the string and `m` is the length of the longest substring without repeating characters.

### Space Complexity:
- **O(m)** where `m` is the number of unique characters in the current substring.

### Test Cases
```python
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # Output: 3
print(s.lengthOfLongestSubstring("bbbbb"))    # Output: 1
print(s.lengthOfLongestSubstring("pwwkew"))   # Output: 3
```

---

## Optimal Sliding Window Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
```

### Explanation
- Initialize a set `charSet` to keep track of characters in the current window.
- Use two pointers `l` (left) and `r` (right) to represent the window.
- Iterate `r` over the string.
- If the character at `r` is already in the set, remove characters from the left of the window until it's unique again.
- Update the result with the maximum window size found.

### Time Complexity:
- **O(n)** where `n` is the length of the string.

### Space Complexity:
- **O(m)** where `m` is the number of unique characters in the longest substring.

---

## Summary
- The brute force approach checks all possible substrings, resulting in a high time complexity.
- The sliding window approach is optimal, efficiently maintaining a window of unique characters and updating the maximum length in one pass.