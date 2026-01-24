# Minimum Add to Make Parentheses Valid - LeetCode

## 1. Problem Explanation

This problem asks you to make a string of parentheses valid using the minimum number of insertions.

A parentheses string is considered valid if:

* It is empty
* Or it can be formed by concatenating two valid strings
* Or it is surrounded by a matching pair of parentheses

You are given a string `s` that only contains `(` and `)` characters. In one move, you are allowed to insert either `(` or `)` at any position. Your task is to find the minimum number of insertions required to make the string valid.

Examples:

* `"())"` needs 1 insertion to become valid
* `"((("` needs 3 closing parentheses to become valid

---

## 2. Code With Comments

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0   # Keeps track of how many '(' are currently unmatched
        res = 0        # Stores how many parentheses we need to add

        # Traverse through every character in the string
        for c in s:
            if c == "(":
                # Found an opening bracket, increase count
                open_cnt += 1
            else:
                # Found a closing bracket
                if open_cnt == 0:
                    # No '(' available to match this ')', so we must add one
                    res += 1
                # Try to match this ')' with an existing '('
                open_cnt = max(open_cnt - 1, 0)

        # Any remaining '(' must be closed with ')'
        return res + open_cnt
```

---

## 3. Solution Approach and Logic

The idea is to keep track of how many opening parentheses are waiting to be matched.

We go through the string character by character:

* When we see `(`, we increase `open_cnt` because it needs a `)` in the future.
* When we see `)`:

  * If we already have an unmatched `(`, we match them.
  * If we do not have one, this means the `)` is invalid, so we must insert a `(`. We increase `res`.

After processing the whole string, if there are still unmatched `(` left, we must add the same number of `)` to close them.

### Why this works

Every invalid `)` needs a `(` before it.
Every remaining `(` needs a `)` after it.

The algorithm simply counts these two cases.

---

## 4. Time and Space Complexity

Time Complexity: O(n)
We scan the string once.

Space Complexity: O(1)
Only two integer variables are used.

This is the most optimal solution because every character must be read at least once, and no extra data structures are needed.

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
