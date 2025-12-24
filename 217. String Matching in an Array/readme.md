# String Matching in an Array - LeetCode

## Problem Explanation

"String Matching in an Array" is a problem where you are given a list of unique strings. Your task is to find all strings that are substrings of another string in the same list.

A string `a` is considered a substring of string `b` if `a` appears contiguously inside `b`.

You can return the answer in any order.

### Example

Input:

```
["mass", "as", "hero", "superhero"]
```

Output:

```
["as", "hero"]
```

Explanation:

* "as" is a substring of "mass"
* "hero" is a substring of "superhero"

---

## Code Explanation

Below is your provided brute-force solution with added comments to help you remember how it works.

```python
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []  # This list will store words that are substrings of other words

        # Loop through each word using index i
        for i in range(len(words)):
            # Compare it with every other word using index j
            for j in range(len(words)):
                if i == j:
                    continue  # Skip comparing the same word

                # Check if words[i] is a substring of words[j]
                if words[i] in words[j]:
                    res.append(words[i])  # Add substring to result
                    break  # No need to check further once found

        return res
```

---

## Solution Approach and Logic

### Brute Force Approach

1. Compare every word with every other word.
2. Skip comparison when both indices point to the same word.
3. Use Python's `in` operator to check if one string exists inside another.
4. If a word is found as a substring, add it to the result list and stop checking further for that word.

This approach works well because:

* The number of words is small (maximum 100).
* String lengths are also small (maximum 30 characters).

---

## Time and Space Complexity

### Time Complexity

* `O(n^2 * m^2)`

  * `n` = number of words
  * `m` = average length of a word
  * Nested loops + substring check

### Space Complexity

* `O(k)`

  * `k` = number of substrings found

---

## Optimal Solution?

Given the problem constraints, the brute-force approach is considered optimal in practice because:

* Input size is small
* Code is simple and readable
* No extra data structures are required

More advanced approaches would increase complexity without meaningful performance benefits for this problem.

---

## Test Cases:
```python
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    words1 = ["mass","as","hero","superhero"]
    print(solution.stringMatching(words1))  # Expected Output: ["as","hero"]

    # Test Case 2
    words2 = ["leetcode","et","code"]
    print(solution.stringMatching(words2))  # Expected Output: ["et","code"]

    # Test Case 3
    words3 = ["blue","green","bu"]
    print(solution.stringMatching(words3))  # Expected Output: []
```