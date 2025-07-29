# Ransom Note - LeetCode

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true` if the `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only be used once in `ransomNote`.

### Examples

**Example 1:**

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

**Example 2:**

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

**Example 3:**

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

### Constraints

* 1 <= ransomNote.length, magazine.length <= 10^5
* ransomNote and magazine consist of lowercase English letters.

---

## Brute Force Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Convert the magazine string to a list so we can remove used characters
        magazine = list(magazine)

        # For each character in ransomNote, check if it exists in the magazine
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                # Remove the character from magazine to avoid reuse
                magazine.remove(c)
        return True
```

### Explanation

* Convert `magazine` to a list so characters can be removed once used.
* Loop through each character in `ransomNote`:

  * If it exists in `magazine`, remove it.
  * If not found, return `False`.
* If all characters are found, return `True`.

### Time and Space Complexity

* **Time Complexity:** O(m \* n) where `m` is the length of `ransomNote` and `n` is the length of `magazine`.
* **Space Complexity:** O(n) because we convert the `magazine` to a list.

---

## Count Frequency Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Initialize a fixed-size list to count character frequency (26 lowercase letters)
        count = [0] * 26

        # Count frequency of each letter in magazine
        for c in magazine:
            count[ord(c) - ord('a')] += 1

        # For each letter in ransomNote, reduce the count and check availability
        for c in ransomNote:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False

        return True
```

### Explanation

* Create a list `count` of size 26 to track frequency of each character.
* Iterate over `magazine` to populate the frequency list.
* Iterate over `ransomNote`, reducing the frequency count:

  * If any count goes below 0, return `False` (not enough letters).
* If all characters are available, return `True`.

### Time and Space Complexity

* **Time Complexity:** O(m + n) where `m` is the length of `ransomNote` and `n` is the length of `magazine`.
* **Space Complexity:** O(1) because the frequency list has a constant size of 26.

---

## Comparison of Solutions

| Solution Type   | Time Complexity | Space Complexity | Suitable For |
| --------------- | --------------- | ---------------- | ------------ |
| Brute Force     | O(m \* n)       | O(n)             | Small inputs |
| Count Frequency | O(m + n)        | O(1)             | Large inputs |

### Why Count Frequency is Optimal

The Count Frequency approach is optimal because:

* It avoids nested iteration by counting character frequencies directly.
* It maintains constant space due to the fixed 26-character alphabet.
* It performs better on large input sizes due to linear time complexity.

---

## Test Cases

```python
# Test Case 1:
ransomNote1 = "a"
magazine1 = "b"
solution1 = Solution()
print(solution1.canConstruct(ransomNote1, magazine1))  # Output: False

# Test Case 2:
ransomNote2 = "aa"
magazine2 = "ab"
solution2 = Solution()
print(solution2.canConstruct(ransomNote2, magazine2))  # Output: False

# Test Case 3:
ransomNote3 = "aa"
magazine3 = "aab"
solution3 = Solution()
print(solution3.canConstruct(ransomNote3, magazine3))  # Output: True
```

---

## Conclusion

* The brute force approach works but is inefficient for larger input sizes.
* The frequency counting method is the most efficient due to linear time and constant space.
* For real-world applications or large datasets, the count frequency solution is the recommended choice.