# Check If a String Contains All Binary Codes of Size K - LeetCode

## Problem Summary

This problem checks whether a binary string `s` contains **every possible binary code** of length `k` as a substring. A binary code is a sequence made up of `0`s and `1`s.

For example, if `k = 2`, all possible binary codes are:

* 00
* 01
* 10
* 11

The task is to confirm that each one appears somewhere inside string `s`.

## Problem Definition

We are given:

* A binary string `s`
* An integer `k`

Return `true` if **every binary code** of length `k` exists in `s` as a substring. Otherwise return `false`.

## Key Idea

There are `2^k` possible binary strings of length `k`. We need to check if all of them appear in `s`.

If the number of unique substrings of length `k` in `s` equals `2^k`, we return `true`.

## Code with Explanation

```python
# Hashset Solution:
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # If the string is too short to contain all possible codes
        if len(s) < 2 ** k:
            return False

        codeSet = set()  # to store unique substrings of length k

        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            codeSet.add(s[i:i + k])  # extract substring and store

        # Check if we found all possible 2^k binary codes
        return len(codeSet) == 2 ** k
```

### How It Works

1. There are `2^k` possible binary patterns of length `k`.
2. We collect all substrings of length `k` from `s`.
3. If the number of unique substrings equals `2^k`, then all binary codes are present.
4. If even one is missing, result is `false`.

### Example Walkthrough

#### Input: `s = "00110110", k = 2`

Substrings of length 2:

* 00
* 01
* 11
* 10

All possible 2-bit codes exist, so output is `true`.

## Time and Space Complexity

| Approach | Time Complexity | Space Complexity | Explanation                                                 |
| -------- | --------------- | ---------------- | ----------------------------------------------------------- |
| Hash Set | O(n)            | O(2^k)           | We slide through string once and store up to `2^k` patterns |

### Why This Solution is Optimal

* We must inspect each substring of length `k`, so O(n) is necessary.
* There are at most `2^k` binary strings of length `k`, so storing these makes the space complexity optimal.
* This problem fundamentally requires seeing all patterns, so we cannot do better than O(2^k) space.

## Test Cases

```python
# Test Case 1:
s = "00110110"
k = 2
print(Solution().hasAllCodes(s, k))  # True

# Test Case 2:
s = "0110"
k = 1
print(Solution().hasAllCodes(s, k))  # True

# Test Case 3:
s = "0110"
k = 2
print(Solution().hasAllCodes(s, k))  # False
```