# Maximum Difference Between Even and Odd Frequency I - LeetCode

## Problem Statement

You are given a string `s` consisting of lowercase English letters.

Your task is to find the **maximum difference** between the frequency of any character `a1` (with an **odd** frequency) and any character `a2` (with an **even** frequency).

Formally, compute:

```
diff = freq(a1) - freq(a2)
```

Where:

* `a1` has an **odd** frequency in the string
* `a2` has an **even** frequency in the string

Return the **maximum difference** that satisfies the conditions above.

### Constraints:

* `3 <= s.length <= 100`
* `s` contains only lowercase English letters
* The string contains **at least one** character with an odd frequency and **at least one** character with an even frequency

---

## Examples

### Example 1:

```
Input: s = "aaaaabbc"
Output: 3
Explanation: 'a' has frequency 5 (odd), 'b' has frequency 2 (even). 5 - 2 = 3.
```

### Example 2:

```
Input: s = "abcabcab"
Output: 1
Explanation: 'a' has frequency 3 (odd), 'c' has frequency 2 (even). 3 - 2 = 1.
```

---

## Code Explanation with Comments

```python
from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # Count the frequency of each character in the string
        count = Counter(s)

        # Initialize oddMax to track the largest odd frequency
        # Initialize evenMin to track the smallest even frequency (set to length of string as upper bound)
        oddMax, evenMin = 0, len(s)

        # Iterate through the frequency values
        for cnt in count.values():
            if cnt & 1:  # If count is odd (bitwise check)
                oddMax = max(oddMax, cnt)  # Update maximum odd frequency
            else:
                evenMin = min(evenMin, cnt)  # Update minimum even frequency

        # Return the difference between the largest odd and smallest even frequency
        return oddMax - evenMin
```

---

## Explanation of Solution and Logic

### Step-by-Step Logic:

1. Use `collections.Counter` to count the frequency of each character.
2. Go through each frequency:

   * If the frequency is **odd**, compare it with the current `oddMax` and keep the maximum.
   * If the frequency is **even**, compare it with the current `evenMin` and keep the minimum.
3. After examining all characters, return the difference: `oddMax - evenMin`.

This approach is simple and effective:

* We **only need the largest odd frequency** and the **smallest even frequency** to get the maximum possible difference.

---

## Time and Space Complexity

### Time Complexity:

* **O(n)**, where `n` is the length of the string `s`.

  * Counting frequencies takes O(n)
  * Iterating over the frequency values (at most 26 English lowercase characters) is constant time

### Space Complexity:

* **O(1)** in terms of frequency storage because the alphabet size is fixed (26 letters)
* `Counter` uses space proportional to the number of unique characters, which is at most 26

---

## Why This is Optimal

* This solution is optimal because:

  * It uses **one pass** to count frequencies and another short pass to evaluate maximum and minimum values.
  * It avoids unnecessary comparisons and brute-force pairings.
  * It leverages the fixed size of the character set (26 lowercase letters), ensuring constant overhead.

There are no better approaches for this problem that improve on both time and space, given the fixed constraints.

---

## Conclusion

This solution provides a clean, efficient, and beginner-friendly way to solve the "Maximum Difference Between Even and Odd Frequency I" problem. It uses a simple idea of tracking the **maximum odd** and **minimum even** frequencies, which directly leads to the answer with minimal computation.