# Merge Strings Alternately - LeetCode

## Problem Statement

Given two strings `word1` and `word2`, merge them by adding letters in alternating order starting with `word1`. If one string is longer than the other, append the extra letters to the end of the merged string.

### Example 1:

**Input:** word1 = "abc", word2 = "pqr"
**Output:** "apbqcr"
**Explanation:**

* word1:  a   b   c
* word2:    p   q   r
* merged: a p b q c r

### Example 2:

**Input:** word1 = "ab", word2 = "pqrs"
**Output:** "apbqrs"

### Example 3:

**Input:** word1 = "abcd", word2 = "pq"
**Output:** "apbqcd"

### Constraints:

* 1 <= word1.length, word2.length <= 100
* `word1` and `word2` consist of lowercase English letters.

---

## Two Pointers I Solution (Basic Alternating Approach)

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0         # Pointers for word1 and word2
        res = []            # Result list to store merged characters

        # Add characters in alternating order
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters (if any)
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)  # Convert list back to string
```

## Two Pointers II Solution (Simpler Conditional Check)

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        res = []
        i = j = 0

        # Loop until both strings are fully traversed
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])
            i += 1
            j += 1

        return "".join(res)
```

---

## Explanation of Solutions

### Approach:

Both solutions use the **two-pointer technique** to traverse the input strings and merge them alternately. They track indices of `word1` and `word2` to add characters one by one into the result list.

* In **Solution I**, the `while` loop runs as long as both pointers are within bounds. After that, remaining characters from either string are appended using slicing.
* In **Solution II**, the loop condition allows iteration even when one string is exhausted, and characters are only appended if the current pointer is valid. This eliminates the need for slicing and makes the logic a bit simpler.

### Differences:

* **Solution I** slices and appends leftover characters after the loop.
* **Solution II** handles leftovers directly inside the loop using conditionals.
* Both are logically equivalent in terms of output, but Solution II may be slightly more intuitive.

---

## Time and Space Complexity

### Time Complexity:

* Both solutions iterate through the combined lengths of `word1` and `word2`, so the time complexity is **O(n + m)**.

### Space Complexity:

* Both use a result list to build the final string, which will have a length of **n + m**, so the space complexity is also **O(n + m)**.

### Optimality:

These solutions are **optimal** for this problem:

* They traverse each input string only once.
* They use no unnecessary data structures beyond a single result list.
* The use of two pointers is a classic and efficient method for problems involving two sequences.

---

## Test Cases

```python
# Test Case 1:
word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2))  # Output: "apbqcr"

# Test Case 2:
word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2))  # Output: "apbqrs"

# Test Case 3:
word1 = "abcd"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2))  # Output: "apbqcd"
```

---

## Conclusion

The problem "Merge Strings Alternately" teaches the application of two pointer techniques and string manipulation. The provided solutions are optimal in both time and space. The difference lies mainly in code readability and implementation style.
