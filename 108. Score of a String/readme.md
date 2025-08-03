# Score of a String - LeetCode

## Problem Statement

Given a string `s`, the **score** of the string is defined as the **sum of the absolute differences** between the ASCII values of each pair of **adjacent characters**.

You need to return the score of the given string.

### Example 1:

**Input:** `s = "hello"`
**Output:** `13`

**Explanation:**

* ASCII values: `h = 104`, `e = 101`, `l = 108`, `o = 111`
* Differences: `|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13`

### Example 2:

**Input:** `s = "zaz"`
**Output:** `50`

**Explanation:**

* ASCII values: `z = 122`, `a = 97`
* Differences: `|122 - 97| + |97 - 122| = 25 + 25 = 50`

### Constraints:

* `2 <= s.length <= 100`
* `s` consists only of lowercase English letters

---

## Code Explanation

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))
        return res
```

### Code Comments (for understanding)

* `res = 0`: Initialize a result variable to store the total score.
* `for i in range(len(s) - 1)`: Iterate through the string until the second last character.
* `abs(ord(s[i]) - ord(s[i + 1]))`: Compute the absolute difference of ASCII values between the current character and the next.
* `res += ...`: Add that difference to the result.
* `return res`: Return the total score after the loop.

---

## Detailed Explanation & Logic

### What is the goal?

We want to calculate how much each character in the string differs from its neighbor in terms of ASCII values. This total sum of differences gives the "score" of the string.

### Step-by-step approach:

1. Convert each character in the string to its ASCII value using Python's built-in `ord()` function.
2. Loop over every adjacent character pair.
3. For each pair, calculate the absolute difference of their ASCII values.
4. Add that difference to a running total.
5. Return the total after the loop completes.

### Why does it work?

ASCII values of characters are just integers, so their differences are also integers. By using the absolute value, we ensure that we always count the positive difference, regardless of the order of characters.

---

## Time and Space Complexity

### Time Complexity: `O(n)`

* We make a single pass through the string of `n` characters, doing constant-time work for each pair of adjacent characters.

### Space Complexity: `O(1)`

* We use only a constant amount of space for storing the result, no additional data structures.

---

## Optimality

This is the **most optimal** solution possible for this problem:

* **Linear time complexity (`O(n)`):** We cannot avoid looking at each pair of adjacent characters, so we are already doing the minimum work.
* **Constant space complexity (`O(1)`):** No extra memory is used beyond the result variable.

Other than implementation style (e.g., recursion or using a list), there's no way to significantly improve on this solution.

---

## Sample Test Cases

```python
# Test Case 1:
s1 = "hello"
print(Solution().scoreOfString(s1))  # Expected output: 13

# Test Case 2:
s2 = "zaz"
print(Solution().scoreOfString(s2))  # Expected output: 50
```

---

## Summary

This problem demonstrates basic string traversal and working with character encoding using ASCII values. The efficient and straightforward approach uses iteration and absolute differences to calculate the score. It is optimal in both time and space, and easy for beginners to understand.
