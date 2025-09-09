# Longest Palindrome - LeetCode

## Problem Explanation

The **Longest Palindrome** problem asks us to determine the length of the longest palindrome that can be formed using the letters of a given string `s`. A palindrome is a string that reads the same forwards and backwards (e.g., `"racecar"`, `"abba"`).

Important details:

* The string `s` can contain both lowercase and uppercase English letters.
* Case sensitivity matters, meaning `"A"` and `"a"` are considered different characters.
* We do not need to return the palindrome itself, only its length.

### Example

* Input: `s = "abccccdd"`
* Output: `7`
* Explanation: The longest palindrome that can be built is `"dccaccd"`, which has a length of 7.

---

## Code with Comments

### Hash Map Solution

```python
from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)  # Store character frequencies
        res = 0  # Length of palindrome

        for c in s:
            count[c] += 1
            # Every time a character count becomes even, we can use it in pairs
            if count[c] % 2 == 0:
                res += 2

        # If there are leftover characters, we can place one in the middle
        return res + (res < len(s))
```

### Hash Set Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()  # Track unmatched characters
        res = 0

        for c in s:
            if c in seen:
                # Found a pair, add 2 to result
                seen.remove(c)
                res += 2
            else:
                # Store the character if it's not paired yet
                seen.add(c)

        # If there are any characters left, we can place one in the middle
        return res + 1 if seen else res
```

---

## Approach and Logic

### 1. Hash Map Solution

* Count how many times each character appears.
* Each time a character count becomes even, it means we can use that pair in the palindrome.
* At the end, if there are still characters with odd counts, we can add **one** extra character in the middle.

### 2. Hash Set Solution

* Keep a set of characters that have not yet been paired.
* If a character appears again (already in set), remove it and add 2 to the palindrome length.
* After processing, if there are unpaired characters left, add **one** to the palindrome length.

### Difference Between the Two Solutions

* **Hash Map Solution** explicitly counts the frequency of each character.
* **Hash Set Solution** directly tracks pairs as they appear, making it simpler to reason about.

Both produce the same result but approach the problem differently.

---

## Complexity Analysis

### Hash Map Solution

* **Time Complexity:** O(n), where n is the length of the string. We iterate over the string once.
* **Space Complexity:** O(m), where m is the number of unique characters (up to 52, since both lowercase and uppercase letters are allowed).

### Hash Set Solution

* **Time Complexity:** O(n), since we traverse the string once.
* **Space Complexity:** O(m), for storing unique characters in the set.

### Most Optimal Solution

Both solutions are equally optimal in terms of time complexity (O(n)) and space complexity (O(m)). However, the **Hash Set Solution** is often preferred because:

* It avoids counting exact frequencies.
* It uses direct pairing logic, which is simpler and more intuitive.

Thus, the **Hash Set Solution** is the more elegant and practical choice while maintaining optimal efficiency.
