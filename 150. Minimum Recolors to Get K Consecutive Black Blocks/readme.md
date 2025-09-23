# Minimum Recolors to Get K Consecutive Black Blocks - LeetCode

## Problem Explanation

The problem "Minimum Recolors to Get K Consecutive Black Blocks" is about finding the minimum number of operations required to achieve **k consecutive black blocks** (`'B'`) in a given string of blocks. Each block in the string is either `'B'` (black) or `'W'` (white). In one operation, you can recolor a white block `'W'` into a black block `'B'`. The goal is to calculate the smallest number of recolors needed so that there exists at least one substring of length **k** that consists entirely of black blocks.

### Example 1

Input: `blocks = "WBBWWBBWBW", k = 7`
Output: `3`
Explanation: By recoloring the 0th, 3rd, and 4th blocks, we get `"BBBBBBBWBW"`, which contains 7 consecutive black blocks.

### Example 2

Input: `blocks = "WBWBBBW", k = 2`
Output: `0`
Explanation: The string already contains 2 consecutive black blocks, so no operations are needed.

---

## Brute Force Solution

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = len(blocks)
        # Loop through all possible substrings of length k
        for i in range(len(blocks) - k + 1):
            count_w = 0
            # Count how many 'W's are in this substring
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    count_w += 1
            # Keep track of the minimum recolors needed
            res = min(res, count_w)
        return res
```

### Explanation of Code

1. Start with `res = len(blocks)` as the maximum possible recolors.
2. Iterate over every possible window (substring) of size `k`.
3. For each window, count how many `'W'` blocks need recoloring.
4. Update the minimum result across all windows.

### Complexity

* **Time Complexity:** `O(n * k)` because for each possible starting index, we count `'W'` over `k` blocks.
* **Space Complexity:** `O(1)`, constant extra space.

This method is simple to understand but can be inefficient for large inputs.

---

## Sliding Window Solution (Optimal)

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = 0
        # Count 'W' in the first window of size k
        for i in range(k):
            if blocks[i] == 'W':
                count_w += 1

        res = count_w
        # Slide the window across the string
        for i in range(k, len(blocks)):
            # Remove the leftmost element from the count
            if blocks[i - k] == 'W':
                count_w -= 1
            # Add the new element in the window
            if blocks[i] == 'W':
                count_w += 1
            # Update the minimum result
            res = min(res, count_w)
        return res
```

### Explanation of Code

1. Initialize the count of `'W'` blocks in the first window of size `k`.
2. Slide the window across the string one block at a time.

   * If the leftmost block leaving the window was `'W'`, reduce the count.
   * If the new block entering the window is `'W'`, increase the count.
3. Update the minimum recolors required after each slide.

### Complexity

* **Time Complexity:** `O(n)` because each block is processed at most twice (once entering, once leaving the window).
* **Space Complexity:** `O(1)`, constant extra space.

---

## Comparison of Solutions

* **Brute Force:** Checks every possible window individually, recalculating counts each time. This leads to `O(n * k)` time complexity.
* **Sliding Window:** Optimizes by reusing the count from the previous window, avoiding redundant counting, making it `O(n)`.

---

## Optimal Solution

The **Sliding Window Solution** is the most efficient approach for this problem because:

* It reduces the time complexity from `O(n * k)` to `O(n)`.
* It uses only constant space.
* It is simple, easy to implement, and handles all edge cases effectively.

Thus, the sliding window method is the recommended optimal solution for this problem.

---

## Test Cases

```python
# Test Cases:
solution = Solution()

# Test Case 1
blocks = "WBBWWBBWBW"
k = 7
print(solution.minimumRecolors(blocks, k)) # Output: 3

# Test Case 2
blocks = "WBWBBBW"
k = 2
print(solution.minimumRecolors(blocks, k)) # Output: 0
```