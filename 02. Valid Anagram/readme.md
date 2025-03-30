# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Example 1:
**Input:**
```python
s = "anagram"
t = "nagaram"
```
**Output:**
```python
True
```

### Example 2:
**Input:**
```python
s = "rat"
t = "car"
```
**Output:**
```python
False
```

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Solution 1: Sorting
### Approach
1. If `s` and `t` have different lengths, they cannot be anagrams.
2. Sort both strings.
3. Compare the sorted versions; if they are the same, return `True`, otherwise return `False`.

### Code Implementation
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

### Time & Space Complexity
- **Time Complexity:** `O(n log n + m log m)`, where `n` and `m` are the lengths of the two strings.
- **Space Complexity:** `O(1)` if sorting is done in place, otherwise `O(n + m)`.

---

## Solution 2: Hashmap (Frequency Count)
### Approach
1. If `s` and `t` have different lengths, they cannot be anagrams.
2. Use two dictionaries (`countS` and `countT`) to store the frequency of each character in `s` and `t`.
3. Compare the frequency dictionaries; if they are identical, return `True`, otherwise return `False`.

### Code Implementation
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
```

### Time & Space Complexity
- **Time Complexity:** `O(n + m)`, where `n` and `m` are the lengths of the two strings.
- **Space Complexity:** `O(1)`, since there are at most 26 lowercase English letters.

---

## Summary
| Solution | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting | `O(n log n + m log m)` | `O(1)` or `O(n + m)` |
| Hashmap (Frequency Count) | `O(n + m)` | `O(1)` |

The hashmap solution is generally more efficient for larger inputs since it avoids sorting.

---

## Test Cases
```python
# Test Case 1
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: True

# Test Case 2
s = "rat"
t = "car"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: False

# Test Case 3 (Using Sorting)
s = "carrace"
t = "racecar"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: True

# Test Case 4 (Using Hashmap)
s = "hello"
t = "world"
solution = Solution()
print(solution.isAnagram(s, t))  # Output: False
```