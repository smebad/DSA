# First Unique Character in a String - LeetCode

## Problem Description

The problem "First Unique Character in a String" asks us to find the index of the first character in a given string that does not repeat anywhere else in the string. If no such unique character exists, we must return `-1`.

### Example 1

**Input:** `s = "leetcode"`
**Output:** `0`
**Explanation:** The character `l` at index `0` is the first character that appears only once.

### Example 2

**Input:** `s = "loveleetcode"`
**Output:** `2`
**Explanation:** The character `v` at index `2` is the first non-repeating character.

### Example 3

**Input:** `s = "aabb"`
**Output:** `-1`
**Explanation:** Every character is repeated, so there is no unique character.

### Constraints

* `1 <= s.length <= 10^5`
* `s` consists of only lowercase English letters.

---

## Code Implementation

We use a hash-map (dictionary) to count the occurrences of each character in the string, and then we check the string in order to find the first unique character.

```python
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)  # Dictionary to store frequency of characters
        
        # First pass: count occurrences of each character
        for c in s:
            count[c] += 1

        # Second pass: find the first index where count is 1 (unique)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
```

---

## Explanation of the Code

1. **Counting characters:**

   * We use a hash-map (`defaultdict(int)`) to keep track of how many times each character appears.
   * Example: For `s = "loveleetcode"`, the dictionary becomes: `{ 'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1 }`.

2. **Finding the first unique character:**

   * We iterate through the string again, checking the frequency of each character.
   * The first character with a count of `1` is returned as its index.
   * If no such character exists, we return `-1`.

---

## Solution Approach and Logic

* We solve the problem in **two passes**:

  1. Count the frequency of each character.
  2. Iterate again to find the first character with frequency `1`.
* This ensures that we return the **first unique character** in order.

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * We make two passes over the string (`n` characters).
  * Each dictionary operation (insert, lookup) is `O(1)`.

* **Space Complexity:** `O(1)`

  * Although we use a hash-map, the size is limited to 26 lowercase English letters.
  * Hence, space does not grow with input size.

---

## Optimal Solution

The above implemented **hash-map approach** is the optimal because:

* It processes the string in linear time.
* It only requires constant extra space since the character set is fixed.
* It is simple, efficient, and works well even for the maximum input size (`10^5`).

---

## Test Cases

```python
sol = Solution()

# Test Case 1:
s = "leetcode"
print(sol.firstUniqChar(s))  # Expected output: 0

# Test Case 2:
s = "loveleetcode"
print(sol.firstUniqChar(s))  # Expected output: 2

# Test Case 3:
s = "aabb"
print(sol.firstUniqChar(s))  # Expected output: -1
```