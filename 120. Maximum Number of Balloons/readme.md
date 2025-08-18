# Maximum Number of Balloons - LeetCode

## Problem Explanation

The problem asks us to determine how many times we can form the word **"balloon"** from the characters of a given string `text`.

* We can only use each character in `text` once.
* We must check if there are enough occurrences of each character required to form the word.
* The word **"balloon"** contains characters: `b`, `a`, `l`, `l`, `o`, `o`, `n`.
* Notice that `l` appears twice and `o` appears twice, so we must account for these duplicates.

### Examples

* Input: `text = "nlaebolko"` → Output: `1` (we can form "balloon" once)
* Input: `text = "loonbalxballpoon"` → Output: `2`
* Input: `text = "leetcode"` → Output: `0`

### Constraints

* `1 <= text.length <= 10^4`
* `text` consists of lowercase English letters only.

---

## Provided Solution (Hash-Map / Counter)

The solution uses Python's **Counter** from the `collections` module to count characters in the input string and compare them to the required characters of the word "balloon".

```python
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequency of characters in the input string
        countText = Counter(text)
        
        # Count frequency of characters required to form "balloon"
        balloon = Counter("balloon")

        # Initialize result with a large number (upper bound)
        res = len(text)
        
        # For each character in "balloon",
        # find how many times it can be formed using available characters
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        
        return res
```

### Code Walkthrough with Comments

1. `Counter(text)` → creates a dictionary-like object with the frequency of each character in the input string.
2. `Counter("balloon")` → creates the frequency dictionary for the word "balloon".

   * Example: `{ 'b':1, 'a':1, 'l':2, 'o':2, 'n':1 }`
3. For each character in the word "balloon":

   * Check how many times it can be provided from the input string.
   * Divide the available frequency (`countText[c]`) by the required frequency (`balloon[c]`).
4. `min(res, ...)` ensures that the answer is limited by the scarcest required character.

   * Example: if we have enough of every letter but only one `b`, then the maximum is `1`.

---

## Approach and Logic

* **Step 1:** Count frequencies of all letters in the input string.
* **Step 2:** Compare against the required frequencies for "balloon".
* **Step 3:** Determine the maximum possible number of times "balloon" can be formed by taking the minimum ratio across all required letters.

### Why it Works

The minimum across all required letters ensures we are not exceeding the available characters. The limiting character determines the maximum number of "balloon" words we can build.

---

## Complexity Analysis

### Time Complexity

* **O(n)**, where `n` is the length of the string `text`.
* This comes from counting characters in the string using `Counter`, which requires one traversal.
* Checking characters in "balloon" is constant time since the word has only 7 unique letters.

### Space Complexity

* **O(1)**, because:

  * The `Counter` for the string holds at most 26 letters (constant).
  * The `Counter` for "balloon" always has 5 unique characters.
* Thus, memory usage does not scale with input size.

---

## Why This Solution is Optimal

This solution is optimal because:

* It runs in **linear time O(n)**, which is necessary since we must at least look at every character of the string.
* It uses **constant extra space O(1)**, since only fixed-size hash maps are used.
* Any faster or more memory-efficient approach is not possible due to the problem's nature (we must inspect all characters).

---

## Key Takeaways

* The problem is about frequency counting.
* Use `collections.Counter` to quickly count character occurrences.
* The minimum ratio of available vs. required characters gives the answer.
* Optimal solution: **O(n) time, O(1) space**.