# Is Subsequence - LeetCode

## Problem Description

The problem **"Is Subsequence"** asks us to determine whether a given string `s` is a subsequence of another string `t`. A **subsequence** is a sequence derived from another string by deleting some or none of the characters without changing the order of the remaining characters.

For example:

* `s = "abc"` is a subsequence of `t = "ahbgdc"` because we can remove characters 'h', 'g', and 'd' from `t` to get `"abc"`.
* `s = "axc"` is **not** a subsequence of `t = "ahbgdc"` because although 'a' is present before 'c', the character 'x' is not present in `t`.

## Code with Comments

### Two-Pointers Solution

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # Initialize pointers for both strings
        while i < len(s) and j < len(t):  # Loop until we reach end of either string
            if s[i] == t[j]:  # If characters match, move both pointers
                i += 1
            j += 1  # Always move pointer in t
        return i == len(s)  # If we have matched all characters of s, return True
```

### Recursive Solution

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def rec(i, j):
            if i == len(s):  # All characters in s matched
                return True
            if j == len(t):  # t is exhausted but s is not
                return False

            if s[i] == t[j]:  # If characters match, move both pointers
                return rec(i + 1, j + 1)
            return rec(i, j + 1)  # Otherwise, skip character in t

        return rec(0, 0)  # Start recursion from beginning of both strings
```

## Solution Approach & Logic

### Two-Pointers Technique

This approach uses two pointers, `i` for string `s` and `j` for string `t`. We iterate through both strings:

* If `s[i] == t[j]`, it means we have found a match for the current character in `s`, so we increment both `i` and `j`.
* If the characters do not match, we move only the pointer `j` in `t`, looking for a match.
* If pointer `i` reaches the end of string `s`, it means every character in `s` was found in `t` in the correct order.

This is a very efficient approach and works well even if the length of `t` is large.

### Recursive Approach

This approach breaks the problem into smaller subproblems by comparing characters recursively:

* If the current characters in `s` and `t` match, we move to the next characters in both.
* If they don’t match, we only move forward in `t`.
* If we reach the end of `s`, it means we have matched all characters.
* If we reach the end of `t` before matching all characters in `s`, it is not a subsequence.

While this solution is elegant and clear, it uses additional space on the call stack, which may not be optimal for long strings.

## Time and Space Complexity

### Two-Pointers Solution

* **Time Complexity**: O(n), where `n` is the length of string `t`. In the worst case, we scan every character of `t` once.
* **Space Complexity**: O(1), because we only use two pointers and no additional data structures.
* **Why it is optimal**: This method does not involve recursion or extra storage, making it fast and memory-efficient.

### Recursive Solution

* **Time Complexity**: O(n \* m) in the worst case due to many recursive calls (with overlapping subproblems if memoization is not used).
* **Space Complexity**: O(n + m) due to the depth of the recursion stack.
* **Why it's less optimal**: While this solution is easier to understand conceptually, it is not as efficient for longer strings due to the recursive overhead.

## Conclusion

The **Two-Pointers** solution is the most optimal and preferred method for checking if one string is a subsequence of another. It is both time-efficient and space-efficient. The recursive solution can serve as a good educational approach but is not suitable for large-scale inputs without optimization.
