# Check If Two String Arrays are Equivalent - LeetCode

## Problem Description

The problem "Check If Two String Arrays are Equivalent" requires checking whether two string arrays, `word1` and `word2`, represent the same string. Each array represents a string by concatenating its elements in order. You need to return `true` if the resulting strings are equal, otherwise `false`.

### Examples

**Example 1:**

```
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation: Both arrays represent the string "abc".
```

**Example 2:**

```
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
```

**Example 3:**

```
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
```

### Constraints

* 1 <= word1.length, word2.length <= 10^3
* 1 <= word1[i].length, word2[i].length <= 10^3
* 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
* word1[i] and word2[i] consist of lowercase letters.

## Solution

We can solve this problem using a **two pointers approach** that compares characters from both arrays without concatenating the entire strings.

### Code Explanation with Comments

```python
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Initialize pointers for words and characters
        w1 = w2 = 0  # Index of word in word1 and word2
        i = j = 0    # Index of character in current word

        while w1 < len(word1) and w2 < len(word2):
            # Compare current characters
            if word1[w1][i] != word2[w2][j]:
                return False

            # Move to the next character in both words
            i, j = i + 1, j + 1

            # Move to the next word in word1 if end of current word is reached
            if i == len(word1[w1]):
                w1 += 1
                i = 0
            # Move to the next word in word2 if end of current word is reached
            if j == len(word2[w2]):
                w2 += 1
                j = 0

        # Both word arrays must be fully traversed for equality
        return w1 == len(word1) and w2 == len(word2)
```

## Approach and Logic

1. We maintain two sets of pointers: one for the current word and one for the character within that word for both arrays.
2. Compare characters at the current position.
3. If characters mismatch, return `False` immediately.
4. Move character pointers forward. If we reach the end of a word, move to the next word and reset the character pointer.
5. Finally, check if both arrays are fully traversed. If yes, return `True`.

### Why this approach is optimal

* Avoids concatenating strings, which can be inefficient for large inputs.
* Compares characters on-the-fly.
* Linear in total number of characters across both arrays.

### Time and Space Complexity

* **Time Complexity:** O(n + m), where n and m are total characters in word1 and word2 respectively.
* **Space Complexity:** O(1), constant extra space is used.

## Test Cases

```python
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert solution.arrayStringsAreEqual(word1, word2) == True

    # Test Case 2
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert solution.arrayStringsAreEqual(word1, word2) == False

    # Test Case 3
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    assert solution.arrayStringsAreEqual(word1, word2) == True

    # Test Case 4
    word1 = ["hello", "world"]
    word2 = ["helloworld"]
    assert solution.arrayStringsAreEqual(word1, word2) == True

    # Test Case 5
    word1 = ["a", "b", "c"]
    word2 = ["a", "b", "d"]
    assert solution.arrayStringsAreEqual(word1, word2) == False

    print("All test cases passed!")
```