# Sort Characters By Frequency - LeetCode

## Problem Description

Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string. Return the sorted string. If there are multiple valid answers, return any of them.

### Examples

**Example 1:**

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' appear once. "eetr" is also valid.
```

**Example 2:**

```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid.
```

**Example 3:**

```
Input: s = "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice while 'A' and 'a' appear once. "bbaA" is also valid.
```

### Constraints

* 1 <= s.length <= 5 * 10^5
* `s` consists of uppercase and lowercase English letters and digits.

## Code Explanation

```python
from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)  # Count frequency of each character
        buckets = defaultdict(list)  # Create buckets mapping frequency -> characters

        # Fill buckets
        for char, freq in count.items():
            buckets[freq].append(char)

        res = []
        # Iterate over frequencies in descending order
        for i in range(len(s), 0, -1):
            if i in buckets:
                for c in buckets[i]:
                    res.append(c * i)  # Repeat character by its frequency

        return "".join(res)  # Join list into final string
```

### Solution Explanation

1. **Count Frequencies:**

   * Use `Counter` to count how many times each character appears.

2. **Group by Frequency (Bucket Sort):**

   * Use a dictionary where the key is frequency and the value is a list of characters with that frequency.

3. **Build Result String:**

   * Iterate from the highest possible frequency down to 1.
   * For each frequency, append the character repeated by its count.
   * Join the characters to form the final string.

**Why Bucket Sort is Efficient:**

* It avoids sorting the entire string by frequency directly.
* By iterating through buckets in decreasing frequency, we construct the string in one pass.

### Time and Space Complexity

* **Time Complexity:** O(n), where n is the length of the string. Counting frequencies and constructing the result takes linear time.
* **Space Complexity:** O(n), due to storing frequency counts and bucket mapping.

### Test Cases

```python
sol = Solution()

# Test Case 1
s1 = "tree"
print(sol.frequencySort(s1))  # Expected output: "eert"

# Test Case 2
s2 = "cccaaa"
print(sol.frequencySort(s2))  # Expected output: "aaaccc"

# Test Case 3
s3 = "Aabb"
print(sol.frequencySort(s3))  # Expected output: "bbAa"
```