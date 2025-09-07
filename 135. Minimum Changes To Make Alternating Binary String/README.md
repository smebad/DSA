# Minimum Changes To Make Alternating Binary String - LeetCode

## Problem Explanation

An **alternating binary string** is a string where no two adjacent characters are the same. For example:

* "0101" and "1010" are alternating.
* "0100" and "1111" are not alternating.

You are given a binary string `s` (containing only '0' and '1'). In one operation, you can flip a character from '0' to '1' or from '1' to '0'. The task is to return the **minimum number of operations** required to make the string alternating.

### Example Walkthrough

* Input: `s = "0100"`

  * Option 1: Make it "0101" → Only 1 change (last character).
  * Option 2: Make it "1010" → More than 1 change.
  * Answer: `1`

* Input: `s = "1111"`

  * Option 1: Convert to "0101" → 2 changes.
  * Option 2: Convert to "1010" → 2 changes.
  * Answer: `2`

This shows that we need to check **both possible alternating patterns** and return the minimum.

---

## Code with Comments

```python
class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        # Check assuming the string should start with '1'
        for i in range(len(s)):
            if i % 2 == 0:  # Even index → expect '1'
                count += 1 if s[i] == '0' else 0
            else:           # Odd index → expect '0'
                count += 1 if s[i] == '1' else 0

        # count = number of changes if starting with '1'
        # (len(s) - count) = number of changes if starting with '0'
        return min(count, len(s) - count)
```

---

## Solution Approach

1. There are only two possible alternating patterns:

   * Pattern A: starts with '0' → "010101..."
   * Pattern B: starts with '1' → "101010..."

2. We loop through the string and count mismatches for one pattern.

   * If we assume it should start with '1', we count how many flips are needed.
   * The number of flips for starting with '0' can be derived as `len(s) - count`.

3. Finally, we take the minimum of the two counts.

---

## Explanation in Simple Words

* Think of the problem as trying to match the string to one of two templates: "010101..." or "101010...".
* For each position in the string, we check if it matches the template.
* If not, we count a change.
* At the end, we compare how many changes each template would take and return the smaller number.

This way we do not need to build both patterns separately, saving time and memory.

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * We loop through the string once, where `n` is the length of `s`.
* **Space Complexity:** `O(1)`

  * We use only a few variables (`count`, index variables) regardless of input size.

---

## Optimality

* This solution is **optimal** because:

  * We only check each character once.
  * No extra storage like arrays or strings is used.
  * Both possible alternating patterns are covered in a single pass.

Thus, it achieves the best possible time (`O(n)`) and space (`O(1)`) for this problem.