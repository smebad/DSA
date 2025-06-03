# Longest Common Prefix - LeetCode

## Problem Description

Given an array of strings, the task is to find the **longest common prefix** shared among all strings in the array. If there is no common prefix, return an empty string `""`.

### Example 1:

```
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
```

### Example 2:

```
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Constraints:

* 1 <= strs.length <= 200
* 0 <= strs\[i].length <= 200
* Each string consists of lowercase English letters only

---

## Code Explanation with Comments

### 1. Vertical Scanning Solution

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Loop through each character index in the first string
        for i in range(len(strs[0])):
            for s in strs:
                # If index exceeds any string's length OR characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]  # Return the prefix up to the mismatch index
        return strs[0]  # All characters matched
```

### 2. Sorting-Based Solution

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]  # If there's only one string, return it directly

        strs = sorted(strs)  # Sort the strings alphabetically
        # Compare only the first and last strings
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]  # Return the prefix up to the mismatch
        return strs[0]  # One string is a prefix of the other
```

---

## Approach and Logic (Beginner Friendly)

### Vertical Scanning

* Take the first string and check each character index.
* Compare that character with the same index in all other strings.
* Stop when a mismatch is found or the index exceeds a string's length.
* Return the prefix up to that point.

### Sorting-Based

* Sort the strings alphabetically.
* The first and last strings in the sorted list will be the most different.
* Only compare these two to find the common prefix, as they define the bounds.

### Key Differences:

| Feature          | Vertical Scanning  | Sorting-Based                       |
| ---------------- | ------------------ | ----------------------------------- |
| Comparison Scope | All strings        | Only first and last after sorting   |
| Sorting Needed   | No                 | Yes                                 |
| Practical Use    | Direct and optimal | Clean logic, slightly more overhead |

---

## Time and Space Complexity

### Vertical Scanning

* **Time Complexity:** `O(n * m)`

  * `n`: Number of strings
  * `m`: Length of the shortest string (or characters compared)
* **Space Complexity:** `O(1)`

  * Only a constant amount of extra space is used.
* **Why Optimal:** You stop checking as soon as a mismatch is found, and you don't sort the array.

### Sorting-Based

* **Time Complexity:** `O(n * m * log n)`

  * Due to sorting based on content of strings
* **Space Complexity:** `O(1)` (excluding sorting overhead)
* **Why Slightly Less Optimal:** Sorting the strings introduces extra computation, although the comparison is limited to just two strings.

---

## Final Verdict

If you are aiming for optimal performance, the **Vertical Scanning** method is the best choice due to its linear time complexity relative to the number and length of strings, without needing to sort.

For clean and simple logic with a little trade off in performance, the **Sorting-Based** approach is also a great alternative.
