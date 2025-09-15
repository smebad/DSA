# Find Common Characters - LeetCode

## Problem Explanation

The problem **Find Common Characters** asks us to find all characters that appear in **every string** of the given array of words. Importantly, characters must include duplicates if they appear multiple times across all strings.

For example:

* Input: `words = ["bella","label","roller"]`
* Output: `["e","l","l"]`

Here, the character `e` appears in all words once, and the character `l` appears in all words at least twice, so we return them accordingly.

If no common characters exist, the result will be an empty list.

---

## Code Walkthrough

```python
from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Start with the character frequency count of the first word
        cnt = Counter(words[0])

        # For each word, update the count to keep only the minimum frequency
        # This ensures we only keep characters common across all words
        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        # Build the result list by repeating each character based on its frequency
        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)

        return res
```

---

## Solution Approach

1. **Frequency Counting**:

   * First, count the frequency of each character in the first word.
   * Then, for every other word, update the counts by taking the minimum frequency for each character. This ensures we only keep characters that are present in all words.

2. **Building the Result**:

   * After processing all words, the counter will contain only the characters that exist in every word, with their minimum occurrence across words.
   * Expand these counts into a result list, including duplicates.

---

## Complexity Analysis

* **Time Complexity**: **O(n \* m)**

  * `n` = number of words
  * `m` = average length of each word
  * We count characters for each word and update frequencies.

* **Space Complexity**: **O(1)**

  * Even though we use counters, the alphabet is fixed (26 lowercase English letters).
  * This means space usage does not grow with input size.

---

## Why This is Optimal

* Since the character set is limited, using frequency counts is the most efficient solution.
* The algorithm ensures minimal passes: one for each word.
* Both runtime and space are well-suited for the problem constraints (`n, m <= 100`).

Thus, the **frequency count solution** is the most optimal one.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
words1 = ["bella","label","roller"]
print(sol.commonChars(words1))  # Expected Output: ["e","l","l"]

# Test Case 2
words2 = ["cool","lock","cook"]
print(sol.commonChars(words2))  # Expected Output: ["c","o"]
```