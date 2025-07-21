# Range Sum Query 2D - Immutable - LeetCode

## Problem Overview

The **Range Sum Query 2D - Immutable** problem on LeetCode requires building a data structure that efficiently answers multiple queries to compute the sum of elements in a sub-rectangle of a 2D matrix.

Given a matrix, you need to support the following operation:

```python
sumRegion(row1, col1, row2, col2)
```

Which returns the **sum of the elements** in the rectangle from the upper-left corner `(row1, col1)` to the lower-right corner `(row2, col2)` (inclusive).

The constraint is that the function `sumRegion()` must run in **O(1)** time, while allowing up to **10^4** queries.

---

## Brute Force Solution

```python
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        # Iterate through each cell in the defined submatrix and sum the values
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                res += self.matrix[r][c]
        return res
```

### Explanation:

* On each call to `sumRegion`, we loop over the submatrix defined by the coordinates and compute the total.

### Time and Space Complexity:

* **Time:** O(m \* n) per query, where `m` and `n` are dimensions of the queried rectangle
* **Space:** O(1)

### Drawbacks:

* This approach is inefficient for large matrices or when queries are frequent since each query is expensive.

---

## Optimized Prefix Sum 2D Solution

```python
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create a prefix sum matrix with one extra row and column for easier boundary handling
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]  # Running sum in the current row
                above = self.sumMat[r][c + 1]  # Value directly above the current cell in sumMat
                # Fill the prefix sum cell
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Convert to 1-based indexing to simplify edge handling
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]

        # Inclusion-Exclusion principle to calculate the submatrix sum
        return bottomRight - above - left + topLeft
```

### Explanation:

* The idea is to precompute a 2D **prefix sum matrix**, where each cell stores the sum of elements from `(0,0)` to `(r,c)`.
* During a query, we use the inclusion-exclusion principle to get the sum in O(1) time.

### Time and Space Complexity:

* **Preprocessing Time:** O(m \* n)
* **Query Time:** O(1)
* **Space:** O(m \* n) to store the prefix sums

### Advantages:

* Extremely efficient for large matrices or when there are many queries.
* Queries run in constant time after the initial setup.

---

## Comparison of Approaches

| Approach      | Preprocessing Time | Query Time | Space Complexity | Use Case                                      |
| ------------- | ------------------ | ---------- | ---------------- | --------------------------------------------- |
| Brute Force   | O(1)               | O(m \* n)  | O(1)             | Small matrix or few queries                   |
| Prefix Sum 2D | O(m \* n)          | O(1)       | O(m \* n)        | Large matrix with many queries (most optimal) |

---

## Why Prefix Sum is Optimal

The Prefix Sum 2D method shines when you need to handle thousands of queries on the same static matrix. It incurs a one-time preprocessing cost and enables O(1) querying time, which drastically reduces the total runtime compared to brute force.

Even though it uses extra space, the tradeoff is worthwhile for performance, especially when real-time responsiveness is needed in applications like spreadsheets, games, or image processing.

---

## Sample Test Case

```python
numMatrix = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])

print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12
```
