# Circular Sentence - LeetCode

## Problem Explanation

A **Circular Sentence** is defined as a sentence where:

1. The last character of each word matches the first character of the next word.
2. The last character of the last word matches the first character of the first word.

The input is a string `sentence`, and we need to return **true** if the sentence is circular and **false** otherwise.

### Examples

* Input: `"leetcode exercises sound delightful"` → Output: `true`
* Input: `"eetcode"` → Output: `true`
* Input: `"Leetcode is cool"` → Output: `false`

---

## Code Solutions

### 1. Splitting the String Solution

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        w = sentence.split(" ")  # Split the sentence into words

        # Check if the first character of each word matches the last character of the previous word
        for i in range(len(w)):
            if w[i][0] != w[i - 1][-1]:
                return False

        return True
```

**Explanation:**

* The sentence is split into words using spaces.
* We loop through each word and check if the first letter of the current word matches the last letter of the previous word.
* Finally, because we start at `i = 0`, Python handles `w[i-1]` as the last word, which ensures the circular condition is also checked between the last and first words.

**Complexity:**

* Time Complexity: **O(n)**, where `n` is the length of the sentence.
* Space Complexity: **O(n)**, since we store all words in a list.

---

### 2. Iteration Solution

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            # When encountering a space, check the last char before space and the first char after space
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        # Finally check if last char equals first char
        return sentence[0] == sentence[-1]
```

**Explanation:**

* Instead of splitting words, this method checks directly in the string.
* Whenever a space is found, it ensures the character before the space equals the character after the space.
* After the loop, it checks if the last character of the sentence equals the first.

**Complexity:**

* Time Complexity: **O(n)**, since we iterate through the sentence once.
* Space Complexity: **O(1)**, as we only use a few variables without extra storage.

---

## Comparing Solutions

* **Splitting Solution**: Easier to understand, but requires extra space for storing words.
* **Iteration Solution**: More optimal in space usage since it avoids storing words.

Both solutions run in **O(n)** time, but the **iteration solution** is more optimal because:

* It uses **O(1)** space.
* It avoids creating additional data structures.

---

## Final Notes

* If clarity is more important, use the **Splitting Solution**.
* If efficiency matters (especially space), use the **Iteration Solution**.
