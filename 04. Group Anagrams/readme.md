# Group Anagrams - Leetcode Blind 75

## Problem Statement
Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:
**Input:**
```plaintext
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
```
**Output:**
```plaintext
[["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
```

### Example 2:
**Input:**
```plaintext
strs = ["x"]
```
**Output:**
```plaintext
[["x"]]
```

### Example 3:
**Input:**
```plaintext
strs = [""]
```
**Output:**
```plaintext
[[""]]
```

### Constraints:
- `1 <= strs.length <= 1000`
- `0 <= strs[i].length <= 100`
- `strs[i]` is made up of lowercase English letters.

---

## Solutions
### 1. Sorting Solution
### Approach:
- Create a dictionary `res` where sorted versions of strings act as keys.
- Iterate over the list, sort each string, and use the sorted string as a key in the dictionary.
- Append the original string to the corresponding key.
- Convert the dictionary values into a list and return.

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
```

### Time Complexity:
- **O(m * nlogn)** where `m` is the number of strings and `n` is the maximum length of a string (due to sorting).

### Space Complexity:
- **O(m * n)** since we store all strings in a dictionary.

### Test Cases:
```python
# Test case 1
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

# Test case 2
strs = ["x"]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [["x"]]

# Test case 3
strs = [""]
solution = Solution()
print(solution.groupAnagrams(strs))  # Expected output: [[""]]
```

---

### 2. Hash Table Solution
### Approach:
- Instead of sorting, use a **count array of size 26** to track the frequency of characters.
- Convert the count array into a tuple and use it as a key in a dictionary.
- Append the original string to the corresponding key.

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # 26 lowercase letters
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
```

### Time Complexity:
- **O(m * n)** where `m` is the number of strings and `n` is the maximum length of a string (linear traversal for character counting).

### Space Complexity:
- **O(m * n)** for storing all strings in the dictionary.

---

## Summary
- **Sorting-based approach**: Slower but intuitive (`O(nlogn)` per string).
- **Hash Table-based approach**: Faster, using character frequency count (`O(n)`).
- Both solutions store grouped anagrams in a dictionary, leading to `O(m * n)` space complexity.

This problem is a great example of utilizing hashing techniques to improve efficiency in string-based problems.

