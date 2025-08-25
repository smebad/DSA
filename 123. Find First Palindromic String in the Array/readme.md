# Find First Palindromic String in the Array - LeetCode

## Problem Explanation

The problem "Find First Palindromic String in the Array" requires us to return the first palindromic string from a given array of words. If no palindromic string exists, we return an empty string.

A **palindrome** is a string that reads the same forward and backward. For example:

* "ada" and "racecar" are palindromes.
* "car" and "def" are not palindromes.

### Example 1

**Input:** words = \["abc","car","ada","racecar","cool"]
**Output:** "ada"
**Explanation:** The first palindrome encountered is "ada".

### Example 2

**Input:** words = \["notapalindrome","racecar"]
**Output:** "racecar"

### Example 3

**Input:** words = \["def","ghi"]
**Output:** "" (no palindrome found)

---

## Code Solutions with Comments

### Solution 1: Reverse String Approach

```python
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            # Check if word is equal to its reverse
            if w == w[::-1]:
                return w  # Return the first palindrome found
        return ""  # If no palindrome exists
```

### Solution 2: Two-Pointers Approach

```python
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            l, r = 0, len(w) - 1  # Initialize left and right pointers
            # Move pointers towards the center
            while w[l] == w[r]:
                if l >= r:
                    return w  # Found a palindrome
                l, r = l + 1, r - 1
        return ""  # No palindrome found
```

---

## Approach and Logic

### Reverse String Solution

* For each word, we reverse it and check if it is the same as the original.
* If yes, return the word immediately.
* If no palindrome is found after checking all words, return an empty string.

**Why it works:** Reversing a string gives us a direct way to compare forward and backward characters.

### Two-Pointers Solution

* For each word, we use two pointers: one starting from the left (`l`) and one from the right (`r`).
* Compare characters at `l` and `r`.
* If they match, move inward (`l+1`, `r-1`).
* If all pairs match until the center, it is a palindrome.
* Return the first palindrome found.

**Why it works:** By comparing characters from both ends, we can check for palindrome properties without creating a reversed copy.

---

## Differences Between the Two Approaches

1. **Reverse String Method:**

   * Simpler to write and understand.
   * Uses Python slicing to reverse a string.
   * May be slightly less efficient because reversing creates a new string.

2. **Two-Pointers Method:**

   * Slightly more efficient because it compares characters directly without creating a new string.
   * Uses only pointers and character checks.
   * More control over the checking process.

Both approaches solve the problem within the given constraints.

---

## Complexity Analysis

### Reverse String Solution

* **Time Complexity:** O(n \* m), where:

  * n = number of words
  * m = average length of each word
  * Each word takes O(m) time to reverse and compare.
* **Space Complexity:** O(m) (because reversing a string creates a new copy).

### Two-Pointers Solution

* **Time Complexity:** O(n \* m), same reasoning as above.
* **Space Complexity:** O(1), as no extra string is created.

---

## Most Optimal Solution

The **Two-Pointers Solution** is the most optimal:

* Same time complexity as the reverse string method.
* Better space complexity (constant space).
* Avoids creating a reversed string, making it slightly more memory efficient.

Thus, in real-world usage where memory efficiency matters, the **two-pointers solution** is preferred, though both are acceptable for the problem constraints.

## Test Cases

```python
sol = Solution()

# Test Case 1
words1 = ["abc","car","ada","racecar","cool"]
print(sol.firstPalindrome(words1))  # Output: "ada"

# Test Case 2
words2 = ["notapalindrome","racecar"]
print(sol.firstPalindrome(words2))  # Output: "racecar"

# Test Case 3
words3 = ["def","ghi"]
print(sol.firstPalindrome(words3))  # Output: ""
