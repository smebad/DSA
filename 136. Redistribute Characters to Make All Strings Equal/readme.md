# Redistribute Characters to Make All Strings Equal - LeetCode

## Problem Explanation

The problem **Redistribute Characters to Make All Strings Equal** asks us to determine if we can make all strings in a given list equal by redistributing characters. The operation allowed is:

* Choose two distinct indices `i` and `j`.
* Pick any character from `words[i]` and insert it into any position in `words[j]`.

The goal is to see if, after performing any number of such operations, all strings in the list can become identical.

### Example Walkthrough

* Example 1: `words = ["abc", "aabc", "bc"]`

  * Move one `'a'` from `"aabc"` to `"bc"` → Now all strings can become `"abc"`.
  * Answer: `True`

* Example 2: `words = ["ab", "a"]`

  * No redistribution will allow both strings to be equal.
  * Answer: `False`

The key observation is that for all words to become equal, **the count of each character across all words must be divisible by the number of words**.

---

## Code with Explanation

```python
from typing import List
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Dictionary to count occurrences of each character
        char_cnt = defaultdict(int)

        # Count all characters from all words
        for w in words:
            for c in w:
                char_cnt[c] += 1

        # For each character, check if its count can be evenly distributed
        for c in char_cnt:
            if char_cnt[c] % len(words):
                return False  # If not divisible, equal distribution is impossible
        return True
```

### Commented Code Walkthrough

1. We use a hashmap (`char_cnt`) to store the frequency of each character across all words.
2. For every word and every character, we increase its count.
3. Finally, for each character, check if the total count is divisible by `len(words)`.

   * If **yes**, we can distribute evenly.
   * If **no**, it's impossible to make all strings equal.

---

## Solution Approach

### Hashmap Solution

* Count frequency of all characters across all words.
* If every character's frequency is divisible by the total number of words, then redistribution is possible, otherwise not.

### Difference Between Approaches

Here, we only have one main approach, which is **frequency counting with a hashmap**. It is straightforward and optimal because:

* It avoids simulating redistribution.
* It leverages a simple mathematical check (divisibility condition).

---

## Time and Space Complexity

* **Time Complexity:** `O(n * m)`

  * `n` = number of words.
  * `m` = average length of each word.
  * We iterate over all characters of all words once.

* **Space Complexity:** `O(1)`

  * At most 26 lowercase English letters are stored in the hashmap.
  * This is constant space.

---

## Optimality

The hashmap solution is the most optimal because:

* It solves the problem in **linear time relative to input size**.
* It uses **constant extra space** since there are only 26 possible characters.
* No simulation of moves is required; only divisibility checks are needed.

Thus, this approach is efficient and optimal for the given constraints.