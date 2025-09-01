# Count the Number of Consistent Strings - LeetCode

## Problem Explanation

You are given a string **allowed** consisting of distinct characters, and an array of strings **words**. A string is considered **consistent** if every character in the string also exists in the string **allowed**.

Your task is to return the **number of consistent strings** from the array **words**.

### Example 1

**Input:**

```python
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
```

**Output:**

```python
2
```

**Explanation:** Strings "aaab" and "baa" only contain characters `a` and `b`, so they are consistent.

### Example 2

**Input:**

```python
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
```

**Output:**

```python
7
```

**Explanation:** All strings are consistent.

### Example 3

**Input:**

```python
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
```

**Output:**

```python
4
```

**Explanation:** Strings "cc", "acd", "ac", and "d" are consistent.

### Constraints

* 1 <= words.length <= 10^4
* 1 <= allowed.length <= 26
* 1 <= words\[i].length <= 10
* The characters in allowed are distinct.
* words\[i] and allowed contain only lowercase English letters.

---

## Solutions

### 1. Brute Force Solution

```python
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for w in words:
            flag = 1  # Assume word is consistent
            for c in w:
                if c not in allowed:  # If a character is not allowed
                    flag = 0  # Mark word as inconsistent
                    break
            res += flag  # Add 1 if word is consistent

        return res
```

#### Explanation of Code

* Loop through each word in **words**.
* For each word, check every character.
* If a character is not in **allowed**, mark the word as inconsistent.
* Count the word only if all characters are in **allowed**.

#### Complexity

* **Time Complexity:** O(n \* m \* l), where:

  * `n` = number of words
  * `m` = max length of a word
  * `l` = length of allowed string (checking `c in allowed` is O(l))
* **Space Complexity:** O(1), since no extra data structures are used.

This works but is inefficient because checking membership in a string (`c in allowed`) is slow compared to a set.

---

### 2. Hash-Set Solution (Optimized)

```python
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)  # Convert allowed string into a set for O(1) lookups

        res = len(words)  # Assume all words are consistent initially
        for w in words:
            for c in w:
                if c not in allowed:  # Faster lookup using set
                    res -= 1  # Word is inconsistent, reduce count
                    break

        return res
```

#### Explanation of Code

* Convert **allowed** into a set for O(1) membership checks.
* Start with `res = len(words)`, assuming all are consistent.
* If any character in a word is not in **allowed**, decrement the count.

#### Complexity

* **Time Complexity:** O(n \* m + l), where:

  * `n` = number of words
  * `m` = max length of a word
  * `l` = length of allowed string (for creating the set)
* **Space Complexity:** O(l), where `l` is the size of allowed set.

This is much faster because checking membership in a set is constant time, unlike a string.

---

## Comparison of Solutions

| Solution    | Time Complexity | Space Complexity | Explanation                                                                                      |
| ----------- | --------------- | ---------------- | ------------------------------------------------------------------------------------------------ |
| Brute Force | O(n \* m \* l)  | O(1)             | Checks every character against the allowed string directly. Works but is slow for larger inputs. |
| Hash-Set    | O(n \* m + l)   | O(l)             | Converts allowed to a set for O(1) lookups, making it significantly more efficient.              |

---

## Most Optimal Solution

The **Hash-Set Solution** is the optimal approach:

* It reduces membership checks from O(l) to O(1).
* It scales well for large word lists.
* The small trade-off of O(l) extra space is acceptable since `l <= 26` (only lowercase letters).

Thus, the **Hash-Set approach** is the best choice for this problem.
