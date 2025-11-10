# Uncommon Words from Two Sentences - LeetCode

## Problem Explanation

The **Uncommon Words from Two Sentences** problem asks us to find words that appear **exactly once** in one of the two given sentences and **do not appear** in the other sentence.

Each sentence is composed of lowercase words separated by spaces, and we are asked to return a list of these uncommon words in any order.

### Example

**Input:**

```python
s1 = "this apple is sweet"
s2 = "this apple is sour"
```

**Output:**

```python
["sweet", "sour"]
```

**Explanation:**

* The word **"sweet"** appears once in `s1` and not in `s2`.
* The word **"sour"** appears once in `s2` and not in `s1`.

Thus, these two are the uncommon words.

---

## Code with Comments

```python
from typing import List
from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Create a hashmap (dictionary) to store the count of each word
        count = defaultdict(int)

        # Combine both sentences by splitting them into words
        # and counting occurrences of each word
        for w in s1.split(" ") + s2.split(" "):
            count[w] += 1

        # Store words that occur exactly once across both sentences
        res = []
        for w, cnt in count.items():
            if cnt == 1:
                res.append(w)

        return res
```

### Example Walkthrough

For `s1 = "this apple is sweet"` and `s2 = "this apple is sour"`:

1. Combine the words from both sentences:
   `["this", "apple", "is", "sweet", "this", "apple", "is", "sour"]`
2. Count occurrences:

   * this → 2 times
   * apple → 2 times
   * is → 2 times
   * sweet → 1 time
   * sour → 1 time
3. Filter words that appear exactly once → `["sweet", "sour"]`

---

## Approach and Logic Explained

1. **Step 1:** Split both sentences into words.
2. **Step 2:** Combine all words and count their occurrences using a **hashmap**.
3. **Step 3:** Traverse the hashmap and collect only those words that appear **exactly once**.
4. **Step 4:** Return the result list.

### Why Use a Hashmap?

A hashmap (dictionary) allows us to store each word as a key and efficiently update or check its count in **O(1)** average time.

This avoids having to manually search the list every time, which would otherwise take **O(n)** per lookup, resulting in slower performance.

---

## Alternate Approaches

1. **Using Python Counter (simpler code)**:

   ```python
   from collections import Counter

   class Solution:
       def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
           count = Counter(s1.split() + s2.split())
           return [word for word in count if count[word] == 1]
   ```

   * This solution does the same thing but uses the built-in `Counter` class for counting.
   * It is shorter and more readable but functionally identical.

2. **Manual comparison without hashmap** (less efficient):

   * You could compare each word between `s1` and `s2` directly, but this would require nested loops and increase the time complexity.
   * Hence, this method is **not optimal**.

---

## Time and Space Complexity

* **Time Complexity:** O(n + m)

  * Splitting both sentences and counting words each take linear time.
  * Here, `n` and `m` are the number of words in `s1` and `s2` respectively.

* **Space Complexity:** O(n + m)

  * In the worst case, every word is unique, so the hashmap stores all of them.

---

## Optimality

The **hashmap-based approach** is optimal for this problem because:

* It only requires **one pass** to count and **one pass** to collect results.
* Both counting and lookup operations are **O(1)** on average.
* It uses **constant extra space** aside from the hashmap and result list.

Therefore, the provided solution is both time-efficient and space-efficient for the given constraints.

---

## Test Cases

```python
solution = Solution()

# Test Case 1
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["sweet", "sour"]

# Test Case 2
s1 = "apple apple"
s2 = "banana"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["banana"]

# Test Case 3
s1 = "a b c"
s2 = "a b d"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["c", "d"]
```