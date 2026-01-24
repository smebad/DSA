# Minimum Add to Make Parentheses Valid - LeetCode

## 1. Problem Overview

You are given a string consisting only of '(' and ')'. A parentheses string is valid if:

* It is empty, or
* It can be written as two valid strings concatenated, or
* It can be written as '(' + valid string + ')'.

You can insert parentheses anywhere in the string. Your task is to find the minimum number of insertions required to make the string valid.

## 2. Code with Comments

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0  # Counts how many '(' are currently unmatched
        res = 0       # Counts how many ')' we need to insert

        for c in s:
            if c == "(":
                # Found an opening bracket, increase count
                open_cnt += 1
            else:
                # Found a closing bracket
                if open_cnt > 0:
                    # If we have an opening to match it, use it
                    res += 1
                # Reduce open count, but never go below 0
                open_cnt = max(open_cnt - 1, 0)

        # Add remaining unmatched '(' as ')'
        return res + open_cnt
```

## 3. Solution Explanation

We scan the string once.

* When we see '(', we increase `open_cnt` because we have an opening bracket waiting to be matched.
* When we see ')':

  * If there is an unmatched '(', we match it.
  * Otherwise, we need to add an opening bracket before it.

At the end, any remaining '(' must be closed by inserting ')'.

This approach avoids using a stack and uses counters instead.

## 4. Complexity

* Time: O(n)
* Space: O(1)

---

## 5. Test Cases
```python
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    s1 = "())"
    print(sol.minAddToMakeValid(s1))  # Expected output: 1

    # Test Case 2
    s2 = "((("
    print(sol.minAddToMakeValid(s2))  # Expected output: 3
```
