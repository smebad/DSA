# Valid Palindrome

## Problem Description

**Valid Palindrome** is a classic string-based problem from the LeetCode Blind 75 list. The task is to determine whether a given string is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

A string is considered a palindrome if it reads the same forward and backward after the transformations. Alphanumeric characters include both letters and numbers.

### Example 1
**Input:** `"A man, a plan, a canal: Panama"`

**Output:** `True`

**Explanation:** After removing non-alphanumeric characters and converting to lowercase, the string becomes `"amanaplanacanalpanama"`, which is a palindrome.

### Example 2
**Input:** `"race a car"`

**Output:** `False`

**Explanation:** After transformation, the string becomes `"raceacar"`, which is not a palindrome.

### Example 3
**Input:** `" "`

**Output:** `True`

**Explanation:** An empty string after removing non-alphanumeric characters is trivially a palindrome.

### Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## Solutions and Explanation

### 1. Reverse String Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
```

#### Step-by-Step Explanation:
1. Initialize an empty string `newStr`.
2. Loop through each character `c` in the input string.
3. If the character is alphanumeric, convert it to lowercase and append it to `newStr`.
4. After cleaning the string, compare it to its reverse using slicing (`[::-1]`).
5. Return `True` if both strings are equal, otherwise `False`.

#### Time and Space Complexity:
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

This solution is straightforward and uses additional space to store the cleaned string.

---

### 2. Two Pointers Solution (Optimal)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
```

#### Step-by-Step Explanation:
1. Use two pointers, `l` at the start and `r` at the end of the string.
2. Move `l` forward until an alphanumeric character is found.
3. Move `r` backward until an alphanumeric character is found.
4. Compare characters at `l` and `r` (after converting to lowercase). If they differ, return `False`.
5. Move the pointers inward (`l += 1`, `r -= 1`) and repeat.
6. If the loop finishes without mismatches, return `True`.

#### Time and Space Complexity:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1), because we only use a constant number of variables.

This is the most **optimal** solution. It avoids the extra space of building a new string and checks characters in-place.

---

## Summary of Solutions

| Solution               | Time Complexity | Space Complexity | Notes                        |
|------------------------|------------------|-------------------|-------------------------------|
| Reverse String         | O(n)             | O(n)              | Easy to implement            |
| Two Pointers (Optimal) | O(n)             | O(1)              | Best in terms of efficiency  |

---

## Test Cases
```python
print(Solution().isPalindrome('A man, a plan, a canal: Panama'))  # True
print(Solution().isPalindrome('race a car'))                       # False
print(Solution().isPalindrome(' '))                                # True
```

---

## Conclusion
The Valid Palindrome problem is an excellent exercise in string manipulation and the two-pointer technique. While both approaches solve the problem correctly, the two-pointer method is preferred for its optimal space usage and clean logic.