# Arranging Coins - LeetCode

## Problem Explanation

The **Arranging Coins** problem is about building a staircase using `n` coins. The staircase is made row by row, where the first row requires 1 coin, the second row requires 2 coins, the third requires 3 coins, and so on. The task is to determine how many complete rows of the staircase can be built with the given `n` coins. If at some point there are not enough coins to complete the next row, the process stops.

### Example 1:

**Input:** `n = 5`
**Output:** `2`
**Explanation:** The first row uses 1 coin, the second row uses 2 coins, and we only have 2 coins left, which is not enough to complete the third row.

### Example 2:

**Input:** `n = 8`
**Output:** `3`
**Explanation:** The first row uses 1 coin, the second row uses 2 coins, the third row uses 3 coins, and 2 coins remain, which are not enough to complete the fourth row.

### Constraints:

* `1 <= n <= 2^31 - 1`

---

## Brute Force Solution

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        # Keep forming rows until we don't have enough coins left
        while n - row > 0:
            row += 1       # Move to the next row
            n -= row       # Subtract the coins used for this row
        return row
```

### Explanation of Code

1. Start with `row = 0`.
2. For each iteration, check if we have enough coins left to form the next row.
3. If yes, increment the row counter and subtract that row's coins from `n`.
4. Stop when there are not enough coins left for the next row.
5. Return the total number of complete rows.

### Complexity Analysis

* **Time Complexity:** `O(√n)` — because the number of rows we can build is about the square root of `2n`.
* **Space Complexity:** `O(1)` — only a few variables are used regardless of input size.

This approach is simple but can be slow for very large `n`.

---

## Binary Search Solution

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid * (mid + 1)) // 2   # Total coins needed for 'mid' rows

            if coins > n:
                r = mid - 1   # Too many coins required, reduce search space
            else:
                l = mid + 1   # Enough coins, try building more rows
                res = max(res, mid)

        return res
```

### Explanation of Code

1. Use binary search on the possible number of rows (from 1 to `n`).
2. For a midpoint `mid`, calculate how many coins are needed to build `mid` rows using the formula `mid * (mid + 1) / 2`.
3. If the required coins exceed `n`, reduce the search space (`r = mid - 1`).
4. Otherwise, update `res` and try to build more rows (`l = mid + 1`).
5. Continue until the search space is exhausted.

### Complexity Analysis

* **Time Complexity:** `O(log n)` — because binary search cuts the search space in half each step.
* **Space Complexity:** `O(1)` — only a few variables are used.

This solution is much faster and more efficient, especially for very large values of `n`.

---

## Comparison of Solutions

* **Brute Force:** Straightforward, iteratively subtracts coins until we run out. Slower for large `n`.
* **Binary Search:** Uses mathematical reasoning with binary search to find the result efficiently.

---

## Optimal Solution

The **Binary Search Solution** is the most optimal one:

* It runs in `O(log n)` time compared to `O(√n)` of the brute force.
* It uses constant space.
* It scales better when `n` is very large (close to `2^31 - 1`).