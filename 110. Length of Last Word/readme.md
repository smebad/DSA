# Length of Last Word - LeetCode

## Problem Description

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A **word** is a maximal substring consisting of **non-space characters only**.

### Examples

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

### Constraints

* 1 <= s.length <= 10^4
* s consists of only English letters and spaces `' '`.
* There will be **at least one word** in `s`.

---

## Iteration-Based Solution

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        # Skip trailing spaces
        while s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
```

### Code Explanation (with comments)

* Start from the end of the string.
* Skip any trailing spaces (as the string may end with spaces).
* Then, count the number of characters until the next space (or start of string).
* This gives the length of the last word.

### Time and Space Complexity

* **Time Complexity:** O(n), where `n` is the length of the string `s`.
* **Space Complexity:** O(1), as no extra space is used.

This is the most optimal solution because it does a single pass and uses constant space.

---

## Built-in Method Solution

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())
```

### Code Explanation (with comments)

* Use `split()` to divide the string into a list of words, ignoring spaces.
* Use `pop()` to get the last word.
* Return the length of that word.

### Time and Space Complexity

* **Time Complexity:** O(n), because `split()` goes through the entire string.
* **Space Complexity:** O(n), since a list of words is created which can take up space proportional to the number of characters in the string.

This approach is simpler and readable but **less optimal** than the iteration method due to additional space used.

---

## Differences Between Solutions

| Feature               | Iteration-Based Solution | Built-in Method Solution |
| --------------------- | ------------------------ | ------------------------ |
| Space Usage           | O(1) (no list created)   | O(n) (creates a list)    |
| Readability           | Slightly verbose         | Very concise             |
| Efficiency            | More optimal             | Less optimal             |
| Interview Suitability | Highly preferred         | Sometimes discouraged    |

---

## Summary

The **iteration-based approach** is the most optimal for this problem as it does not require any additional space and directly processes the string from the end to find the last word. The **built-in method** is readable and easy to write but may not be space-efficient for large strings. It's recommended to prefer the iteration method in technical interviews.
