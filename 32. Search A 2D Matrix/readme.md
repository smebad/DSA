# Search a 2D Matrix - LeetCode

## Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

## Example

**Input:**

```python
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
```

**Output:**

```python
True
```

**Input:**

```python
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
```

**Output:**

```python
False
```

---

## Brute Force Solution

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Iterate over each row
        for r in range(len(matrix)):
            # Iterate over each column in the current row
            for c in range(len(matrix[0])):
                # Check if the current element equals the target
                if matrix[r][c] == target:
                    return True
        # If the element was not found, return False
        return False
```

### Time and Space Complexity

* **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
* **Space Complexity:** `O(1)`, as no extra space is used.

This brute force solution is not optimal for large matrices because it checks each element individually.

### Test Cases

```python
# Test case 1
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
print(sol.searchMatrix(matrix, target))  # Output: True

# Test case 2
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(sol.searchMatrix(matrix, target))  # Output: False

# Test case 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 1
print(sol.searchMatrix(matrix, target))  # Output: True
```

---

## Optimal Solution (Binary Search)

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # First, perform binary search to find the correct row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:  # If target is greater than the last element of the row
                top = row + 1
            elif target < matrix[row][0]:  # If target is smaller than the first element of the row
                bot = row - 1
            else:
                break  # Target must be in this row

        # If the target is not in any row range, return False
        if not (top <= bot):
            return False

        # Binary search in the found row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:  # Move right
                l = m + 1
            elif target < matrix[row][m]:  # Move left
                r = m - 1
            else:
                return True  # Target found
        return False
```

### Time and Space Complexity

* **Time Complexity:** `O(log(m) + log(n))`

  * `O(log(m))` for binary search on rows
  * `O(log(n))` for binary search on columns
* **Space Complexity:** `O(1)` as no extra space is used

### Why This Solution is Optimal

This solution is better than brute force because it leverages the sorted property of the matrix. Instead of scanning every element, it performs two binary searches:

1. To find the possible row that might contain the target.
2. To search within that row efficiently.

By reducing the number of comparisons from `m * n` to `log(m) + log(n)`, it becomes highly efficient even for large matrices.
