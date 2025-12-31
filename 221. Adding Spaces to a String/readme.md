# Adding Spaces to a String - LeetCode

## Problem Overview

"Adding Spaces to a String" is a problem where you are given a string `s` and an array `spaces` containing indices in `s`. Each index in `spaces` indicates a position **before which a space should be inserted**. The goal is to return the modified string with spaces added at the specified positions.

### Example 1

Input: `s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]`
Output: `"Leetcode Helps Me Learn"`

### Example 2

Input: `s = "icodeinpython", spaces = [1,5,7,9]`
Output: `"i code in py thon"`

### Example 3

Input: `s = "spacing", spaces = [0,1,2,3,4,5,6]`
Output: `" s p a c i n g"`

### Constraints

* 1 <= s.length <= 3 * 10^5
* s consists of lowercase and uppercase English letters.
* 1 <= spaces.length <= 3 * 10^5
* 0 <= spaces[i] <= s.length - 1
* `spaces` array is strictly increasing.

## Solution Explanation

The provided solution uses a **two pointers approach**:

* `i` is used to traverse the string `s`.
* `j` is used to traverse the `spaces` array.
* A result list `res` is used to build the final string efficiently.

### Approach

1. Initialize two pointers `i = 0` and `j = 0`, and an empty list `res`.
2. Traverse the string `s` with pointer `i` and the `spaces` array with pointer `j`.
3. If the current index `i` is less than `spaces[j]`, append `s[i]` to `res` and increment `i`.
4. If `i` reaches `spaces[j]`, append a space `' '` to `res` and increment `j` to move to the next space.
5. After the loop, append any remaining characters in `s` to `res`.
6. Join the list `res` into a string and return it.

### Code with Comments

```python
from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, j = 0, 0  # Pointers for string s and spaces array
        res = []     # Result list to build the final string

        # Traverse string and spaces array
        while i < len(s) and j < len(spaces):
            if i < spaces[j]:  # If current index is before the next space
                res.append(s[i])
                i += 1
            else:               # Insert a space before s[i] if i == spaces[j]
                res.append(' ')
                j += 1

        # Append any remaining characters after the last space
        if i < len(s):
            res.append(s[i:])

        return ''.join(res)  # Join the list into a string
```

### Logic

* We traverse `s` only once while keeping track of the space positions using the second pointer.
* Using a list `res` avoids inefficient string concatenation.
* This approach ensures we insert spaces exactly at the specified indices without shifting other characters incorrectly.

### Time and Space Complexity

* **Time Complexity:** `O(n + m)` where `n` is the length of `s` and `m` is the number of spaces. Each pointer traverses its array only once.
* **Space Complexity:** `O(n + m)` because we store the resulting string in a list before joining.

### Why Optimal

* The two pointers approach is optimal because it avoids repeated string slicing or concatenation, which would increase time complexity.
* It traverses each input exactly once and builds the output efficiently in linear time.

## Test Cases

```python
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "LeetcodeHelpsMeLearn"
    spaces1 = [8, 13, 15]
    print(solution.addSpaces(s1, spaces1))  # Output: "Leetcode Helps Me Learn"

    # Test Case 2
    s2 = "icodeinpython"
    spaces2 = [1, 5, 7, 9]
    print(solution.addSpaces(s2, spaces2))  # Output: "I code in py thon"

    # Test Case 3
    s3 = "spacing"
    spaces3 = [0, 1, 2, 3, 4, 5, 6]
    print(solution.addSpaces(s3, spaces3))  # Output: " s p a c i n g"
```