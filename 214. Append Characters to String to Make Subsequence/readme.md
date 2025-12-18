# Append Characters to String to Make Subsequence - LeetCode

## Problem Explanation

The problem **Append Characters to String to Make Subsequence** asks us to determine the minimum number of characters that must be appended to the end of a string `s` so that another string `t` becomes a subsequence of `s`.

A **subsequence** is formed by deleting zero or more characters from a string without changing the order of the remaining characters. This means the characters of `t` must appear in `s` in the same order, but not necessarily contiguously.

We are only allowed to **append characters at the end of `s`**, not insert them in the middle or remove any existing characters.

---

## Key Idea

Instead of trying all possible append operations, we observe that:

* We want to match as many characters of `t` as possible **inside `s`**.
* Any characters of `t` that cannot be matched in order must be appended at the end.

So the problem reduces to finding **how many characters of `t` are already a subsequence of `s`**.

---

## Code with Comments

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # i -> pointer for string s
        # j -> pointer for string t
        i, j = 0, 0

        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move both pointers
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                # If they do not match, only move pointer of s
                i += 1

        # j indicates how many characters of t were matched
        # Remaining characters = total length of t - matched characters
        return len(t) - j
```

---

## Step-by-Step Approach and Logic

### Step 1: Use Two Pointers

* One pointer `i` iterates over string `s`.
* Another pointer `j` iterates over string `t`.

### Step 2: Match Characters in Order

* If `s[i] == t[j]`, it means this character of `t` can be matched inside `s`.

* Move both pointers forward.

* If they do not match, move only the `s` pointer to try the next character.

This ensures we are matching `t` as a subsequence of `s`.

### Step 3: Count Unmatched Characters

* When traversal ends, `j` tells us how many characters of `t` were matched.
* The remaining characters `len(t) - j` must be appended to `s`.

---

## Example Walkthrough

### Example 1

```
s = "coaching"
t = "coding"
```

Matched characters in order: `c`, `o`

Unmatched characters in `t`: `d`, `i`, `n`, `g`

Answer: `4`

---

### Example 2

```
s = "abcde"
t = "a"
```

`t` is already a subsequence of `s`

Answer: `0`

---

### Example 3

```
s = "z"
t = "abcde"
```

No characters match

All characters of `t` must be appended

Answer: `5`

---

## Time and Space Complexity

### Time Complexity

* **O(n + m)** where:

  * `n` = length of string `s`
  * `m` = length of string `t`

Each string is traversed at most once.

### Space Complexity

* **O(1)**

Only two pointers are used. No extra data structures are required.

---

## Why This Is the Most Optimal Solution

* The constraints allow strings up to `10^5` characters, so inefficient approaches would time out.
* This method avoids extra memory usage and avoids nested loops.
* It directly leverages the definition of a subsequence.

Because it runs in linear time and constant space, this two-pointer approach is the **most optimal solution** for this problem.

---

## Test Cases
```python
# Test Case 1:
s1 = "coaching"
t1 = "coding"
print(Solution().appendCharacters(s1, t1))  # Output: 4

# Test Case 2:
s2 = "abcde"
t2 = "a"
print(Solution().appendCharacters(s2, t2))  # Output: 0

# Test Case 3:
s3 = "z"
t3 = "abcde"
print(Solution().appendCharacters(s3, t3))  # Output: 5
```