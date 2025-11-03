# Repeated DNA Sequences

## Problem Explanation

The DNA sequence is composed of characters `A`, `C`, `G`, and `T`. We are given a DNA string `s` and must find all **10‑letter long substrings** that appear **more than once** in it.

A substring counts only if:

* It is exactly 10 characters long
* It occurs **at least twice** in the string

We return all such repeated substrings.

Example:

* Input: `AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT`
* Output: `{"AAAAACCCCC", "CCCCCAAAAA"}`

## Intuition

We slide a window of length **10** across the string and record each substring. If we ever see the same substring again, it is a repeated DNA sequence.

This works because all repeats must be found by checking every possible 10‑character window.

## Provided Solutions & Code Explanation

### Hash Set Solution

```python
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()  # seen stores all substrings, res stores repeated ones

        for l in range(len(s) - 9):  # loop until last possible 10-char window
            cur = s[l: l + 10]      # extract substring of length 10
            if cur in seen:        # if seen before, it's a repeat
                res.add(cur)
            seen.add(cur)          # track this substring
        return list(res)
```

### Hash Map Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        mp = defaultdict(int)  # map substring to its frequency
        res = []
        for l in range(len(s) - 9):
            cur = s[l: l + 10]
            mp[cur] += 1  # count the substring
            if mp[cur] == 2:  # add only at second occurrence
                res.append(cur)

        return res
```

## Explanation of Logic

For both approaches:

1. Iterate through string, extract each 10‑length substring
2. Track how many times each substring appears
3. If we see it again, it is a repeated DNA sequence
4. Store and return the repeated ones

### Difference Between Set and Hash Map Method

| Approach | Uses                | When we detect repeat            | Pros                            |
| -------- | ------------------- | -------------------------------- | ------------------------------- |
| Hash Set | `seen` + `res` sets | When substring already in `seen` | Simple and clean                |
| Hash Map | dictionary to count | When count reaches 2             | Allows exact frequency tracking |

Set method is enough since we only care about repeats, not total frequency.

## Time and Space Complexity

### Time Complexity: **O(n)**

We slide over the string once, extracting each 10‑char substring.

### Space Complexity: **O(n)**

We may store all substrings in worst case.

## Most Optimal Approach

The **Hash Set solution** is optimal because:

* Only checks existence, does not store counts
* Fast lookup
* Less memory overhead than full frequency map

So its simple logic and minimal data storage make it optimal for this problem.

## Test Cases
``` python
sol = Solution()

# Test Case 1:
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))  # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

# Test Case 2:
s = "AAAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))  # Output: ["AAAAAAAAAA"]
```