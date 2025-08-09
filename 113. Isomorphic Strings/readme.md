# Isomorphic Strings - LeetCode

## Problem Description

Two strings `s` and `t` are **isomorphic** if the characters in `s` can be replaced to get `t`.

* Each occurrence of a character must map to the same character in `t`.
* The mapping must preserve the order of characters.
* No two different characters from `s` can map to the same character in `t`.
* A character can map to itself.

### Example 1

```
Input: s = "egg", t = "add"
Output: true
Explanation: 'e' maps to 'a' and 'g' maps to 'd'.
```

### Example 2

```
Input: s = "foo", t = "bar"
Output: false
Explanation: 'o' would have to map to both 'a' and 'r', which is not allowed.
```

### Example 3

```
Input: s = "paper", t = "title"
Output: true
Explanation: 'p' maps to 't', 'a' maps to 'i', 'e' maps to 'l', 'r' maps to 'e'.
```

### Constraints

* `1 <= s.length <= 5 * 10^4`
* `t.length == s.length`
* `s` and `t` consist of valid ASCII characters.

---

## Code Explanation

### Hash Map Solution

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}  # Dictionaries to store mappings from s to t and t to s

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # If c1 is already mapped but not to c2, or c2 is already mapped but not to c1, it's invalid
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # Store the mapping in both directions
            mapST[c1] = c2
            mapTS[c2] = c1

        return True
```

**Comments in the code:**

1. `mapST` stores character mapping from `s` to `t`.
2. `mapTS` stores character mapping from `t` to `s`.
3. At each position, check:

   * If the existing mapping contradicts the current character pairing.
4. If any conflict is found, return `False`.
5. If the loop finishes without conflicts, return `True`.

---

## Approach and Logic

The solution works by:

* Iterating through each character position in `s` and `t`.
* Using two dictionaries to ensure a **one-to-one mapping**:

  * `mapST` for mapping `s` → `t`.
  * `mapTS` for mapping `t` → `s`.
* If a mismatch in mapping occurs at any point, we return `False` immediately.
* If all mappings are consistent, we return `True`.

**Why two maps?**

* One dictionary alone can prevent multiple characters in `s` from mapping to the same character in `t`.
* But we also need to ensure no two characters in `t` map back to the same character in `s`.
* Using two dictionaries enforces this bidirectional uniqueness.

---

## Complexity Analysis

* **Time Complexity:** `O(n)` where `n` is the length of `s` (or `t`). We traverse the strings once.
* **Space Complexity:** `O(m)` where `m` is the number of unique characters (at most the size of the ASCII set). This is due to the storage of mappings.

---

## Optimality

This is the most optimal approach for this problem because:

* We must inspect each character pair at least once, making `O(n)` the lower bound.
* The space used is minimal and unavoidable since we need to track the mapping.
* Attempting to solve without two-way checking can miss cases where mappings are invalid in one direction.

---

## Test Cases

```python
# Expected output: True
print(Solution().isIsomorphic("egg", "add"))

# Expected output: False
print(Solution().isIsomorphic("foo", "bar"))

# Expected output: True
print(Solution().isIsomorphic("paper", "title"))
```