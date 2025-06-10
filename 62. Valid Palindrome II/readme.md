# Valid Palindrome II - LeetCode

## Problem Description

Given a string `s`, return `True` if `s` can become a palindrome after deleting **at most one character**. Otherwise, return `False`.

A **palindrome** is a string that reads the same forward and backward. For this problem, you are allowed to make **one** deletion to achieve this condition.

### Examples

* **Example 1:**

  * Input: `s = "aba"`
  * Output: `True`
  * Explanation: The string is already a palindrome.

* **Example 2:**

  * Input: `s = "abca"`
  * Output: `True`
  * Explanation: Removing 'c' results in "aba", which is a palindrome.

* **Example 3:**

  * Input: `s = "abc"`
  * Output: `False`
  * Explanation: No single deletion can make this string a palindrome.

### Constraints

* `1 <= s.length <= 10^5`
* `s` consists of lowercase English letters.

---

## Code with Explanation (Two Pointers Solution)

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize two pointers at start and end

        while l < r:
            if s[l] != s[r]:
                # If mismatch, try skipping either left or right character
                skipL = s[l + 1 : r + 1]  # Skip left character
                skipR = s[l : r]          # Skip right character
                # Check if either resulting substring is a palindrome
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1  # Move pointers inward if characters match

        return True  # If entire string is a palindrome without mismatch
```

---

## Approach and Logic Explained

### Two Pointers Technique

* **Step 1:** Use two pointers: one starting from the left (`l`) and one from the right (`r`).
* **Step 2:** While `l < r`, compare characters:

  * If they are equal, move both pointers inward.
  * If not equal, you can delete **one** character:

    * Try skipping the character at the left pointer.
    * Try skipping the character at the right pointer.
    * Check if either result is a palindrome.
* **Step 3:** If a palindrome is found after skipping, return `True`; otherwise, return `False`.

### Why It Works

This solution explores only **two possibilities** when a mismatch is found (skip left or skip right), keeping the check efficient.

---

## Differences Between Possible Solutions

There could be brute-force solutions where we try removing **every character** one by one to check if the result is a palindrome. But that would be too slow for large inputs.

The provided solution is optimal because it only checks **one mismatch**, and from there considers only two substrings, both of which are reversed and compared. This limits the number of checks significantly.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * We traverse the string only once using the two-pointer approach.
  * In case of a mismatch, we may reverse a substring (which also takes O(n) in the worst case).
  * So in total, the time complexity remains linear.

* **Space Complexity:** `O(n)`

  * Substrings like `s[l+1:r+1]` or `s[l:r]` create new strings.
  * Each substring and its reversal takes up memory.

> **Most Optimal Solution:**

To optimize space as well, instead of slicing strings, you could write a helper function that checks whether a substring is a palindrome **in-place** without creating a new string. That would reduce space to `O(1)`.

---

## Test Cases

```python
# Test Case 1:
s = "aba"
print(Solution().validPalindrome(s))  # Expected Output: True

# Test Case 2:
s = "abca"
print(Solution().validPalindrome(s))  # Expected Output: True

# Test Case 3:
s = "abc"
print(Solution().validPalindrome(s))  # Expected Output: False
```
