# Number of Pairs of Interchangeable Rectangles - LeetCode

## Problem Explanation

The **"Number of Pairs of Interchangeable Rectangles"** problem asks us to determine how many pairs of rectangles can be considered interchangeable. Two rectangles are **interchangeable** if they have the same width-to-height ratio.

Formally, given a list of rectangles, each represented as `[width, height]`, two rectangles `i` and `j` are interchangeable if:

[ \frac{width_i}{height_i} = \frac{width_j}{height_j} ]

We need to count how many such pairs `(i, j)` exist where `i < j`.

### Example:

**Input:** `rectangles = [[4,8],[3,6],[10,20],[15,30]]`

**Output:** `6`

**Explanation:**
All rectangles have the same ratio (0.5), so each pair of rectangles is interchangeable.
The pairs are: (0,1), (0,2), (0,3), (1,2), (1,3), and (2,3).

---

## Code Explanation

```python
from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}  # Dictionary to store the frequency of each unique ratio
        res = 0  # Variable to store total interchangeable pairs

        for w, h in rectangles:
            ratio = w / h  # Calculate the width-to-height ratio

            # Add the number of rectangles seen so far with the same ratio
            res += count.get(ratio, 0)

            # Update the count for this ratio
            count[ratio] = 1 + count.get(ratio, 0)

        return res
```

### Code Comments (Step-by-Step):

1. **Initialize a dictionary `count`:**

   * This will store how many times each unique width-to-height ratio has appeared.

2. **Initialize a variable `res`:**

   * Used to count total interchangeable rectangle pairs.

3. **Loop through each rectangle:**

   * For each rectangle `[w, h]`, calculate its ratio `w / h`.

4. **Count pairs dynamically:**

   * If the ratio has been seen before, every rectangle with the same ratio forms a new pair with the current one.
   * Add that count to `res`.

5. **Update the count of the ratio:**

   * Increase the count for that specific ratio by 1.

6. **Return the result.**

---

## Approach and Logic

The key idea is to **group rectangles by their width-to-height ratio**. Rectangles in the same group are interchangeable.

* Instead of comparing every pair (which would take O(n²) time), we use a **hashmap** (dictionary) to count occurrences of each ratio.
* When we find another rectangle with the same ratio, it can pair with all the previous ones that share that ratio.

### Intuitive Example:

Suppose we have the ratios: `[0.5, 0.5, 0.5]`

* When the first rectangle is processed, no pairs yet.
* When the second rectangle arrives, it forms **1 pair** with the first one.
* When the third rectangle arrives, it forms **2 pairs** (with the first and second).

Total pairs = 1 + 2 = 3.

This logic generalizes to any number of rectangles with the same ratio.

---

## Complexity Analysis

### Time Complexity: **O(n)**

* We traverse the list of rectangles once.
* Each lookup and insertion in the hashmap takes **O(1)** on average.

### Space Complexity: **O(n)**

* In the worst case, all rectangles have distinct ratios, and we store each ratio in the hashmap.

---

## Why This Solution is Optimal

* A naive approach would involve checking every pair of rectangles (O(n²)), which is inefficient for large inputs (up to 10⁵ rectangles).
* The **hashmap approach** avoids redundant pairwise comparisons by counting how many rectangles share the same ratio.
* It achieves the best possible time complexity **O(n)** and minimal space use for this problem.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
print(sol.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]]))  # Expected output: 6

# Test Case 2
print(sol.interchangeableRectangles([[4,5],[7,8]]))  # Expected output: 0
```