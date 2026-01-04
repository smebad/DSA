# Sentence Similarity III - LeetCode

## Problem Overview

"Sentence Similarity III" is a string comparison problem where you are given two sentences made up of words separated by single spaces. The goal is to determine whether the two sentences can be made exactly the same by inserting an arbitrary sentence (possibly empty) into one of them.

The key rule is that the inserted words must be separated by spaces, meaning partial word matches are not allowed.

### Key Idea

Two sentences are considered similar if:

* One sentence can become the other by inserting extra words at any position (start, middle, or end).
* The order of existing words must remain unchanged.

---

## Understanding the Given Solution

The solution uses a **two-pointer technique** by comparing words from the beginning and the end of both sentences.

### Code with Detailed Comments

```python
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into lists of words
        s1 = sentence1.split()
        s2 = sentence2.split()

        # Ensure s1 is the shorter sentence
        if len(s2) < len(s1):
            s1, s2 = s2, s1

        # Pointer to compare words from the start
        l1 = 0
        while l1 < len(s1) and s1[l1] == s2[l1]:
            l1 += 1

        # Pointers to compare words from the end
        r1, r2 = len(s1) - 1, len(s2) - 1
        while r1 >= l1 and r2 >= 0 and s1[r1] == s2[r2]:
            r1 -= 1
            r2 -= 1

        # If all words in s1 are matched, the sentences are similar
        return l1 > r1
```

---

## Approach and Logic Explained

### Step-by-Step Strategy

1. **Split sentences into words** so comparisons are done word by word.
2. **Always compare the shorter sentence against the longer one**. This simplifies the logic.
3. **Match words from the beginning** until a mismatch occurs.
4. **Match words from the end** until a mismatch occurs.
5. If all words of the shorter sentence are matched by prefix and suffix comparisons, then the sentences are similar.

### Why This Works

* Any inserted sentence must lie between matching prefix and suffix words.
* If the unmatched middle portion exists only in the longer sentence, insertion is possible.

### Example Walkthrough

Sentence 1: "My name is Haley"
Sentence 2: "My Haley"

* Prefix match: "My"
* Suffix match: "Haley"
* Middle words ("name is") can be inserted
* Result: Similar

---

## Comparison with Other Possible Approaches

### Brute Force (Not Implemented)

* Try inserting all possible substrings and compare
* Very inefficient and complex

### Two-Pointer (Current Solution)

* Clean and intuitive
* Linear comparison
* No unnecessary string construction

This makes the current solution the best choice.

---

## Time and Space Complexity

### Time Complexity

* **O(min(n, m))**, where n and m are the number of words in the two sentences.
* Each word is compared at most once from the start and once from the end.

### Space Complexity

* **O(1)** extra space (excluding the split operation).
* No additional data structures are used.

---

## Why This Solution Is Optimal

* Uses only simple pointer comparisons
* Avoids rebuilding or modifying strings
* Handles all edge cases (insertion at start, middle, or end)
* Works efficiently within the given constraints

This makes it both time-efficient and easy to understand, especially for beginners.

---

## Test Cases:
```python
# Test Case 1:
sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(Solution().areSentencesSimilar(sentence1, sentence2))  # Output: True

# Test Case 2:
sentence1 = "of"
sentence2 = "A lot of words"
print(Solution().areSentencesSimilar(sentence1, sentence2))  # Output: False

# Test Case 3:
sentence1 = "Eating right now"
sentence2 = "Eating"
print(Solution().areSentencesSimilar(sentence1, sentence2))  # Output: True
```