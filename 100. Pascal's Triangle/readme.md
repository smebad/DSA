# Pascal's Triangle - LeetCode

## Problem Description

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

Pascal's triangle is a mathematical structure where each number is the sum of the two numbers directly above it. The triangle starts with a single `1` at the top, and each subsequent row contains one more element than the previous, with the outermost elements always being `1`.

### Example 1:

**Input:** `numRows = 5`

**Output:**

```
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
```

### Example 2:

**Input:** `numRows = 1`

**Output:** `[[1]]`

### Constraints:

* `1 <= numRows <= 30`

---

## Dynamic Programming Solution (Python Code)

```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result with the first row of Pascal's Triangle
        res = [[1]]

        # Generate each row starting from the second one
        for i in range(numRows - 1):
            # Pad the last row with zeros on both sides
            temp = [0] + res[-1] + [0]
            row = []
            # Generate the next row by summing adjacent elements
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
```

---

## Approach & Explanation

This solution uses **dynamic programming** to construct Pascal's Triangle row by row. Here's a breakdown of the logic:

1. **Start with the base case**: The triangle begins with a single `1`, so we initialize the result with `[[1]]`.
2. **Build each row based on the previous row**:

   * Pad the last row with zeros at both ends. This helps handle edge elements, which are always `1`.
   * For each index in the new row, add two adjacent numbers from the padded previous row.
   * Append the generated row to the result.
3. Continue this process `numRows - 1` times to complete the triangle.

### Why padding with zeros?

By adding `0` to both ends of the previous row, we simplify the logic. Each number in a new row is always the sum of two numbers from the previous row: the one directly above and the one to the left-above. Padding avoids index errors and handles edge values cleanly.

---

## Time and Space Complexity

### Time Complexity: `O(numRows^2)`

* Each row has `i` elements (where `i` ranges from 1 to `numRows`).
* Total number of operations is the sum of the first `numRows` integers.
* So total time is `O(1 + 2 + 3 + ... + numRows) = O(numRows^2)`.

### Space Complexity: `O(numRows^2)`

* We're storing the entire triangle in a list of lists.
* The total number of elements stored is `numRows * (numRows + 1) / 2`, which is still `O(numRows^2)`.

---

## Why This Solution is Optimal

This dynamic programming approach avoids redundant computations and builds each row using previously computed data. It's simple, clean, and runs efficiently within the given constraints (`numRows <= 30`). For this problem, the space complexity is acceptable since we are expected to return the entire triangle.

---

## Test Cases

```python
# Test Case 1:
print(Solution().generate(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Test Case 2:
print(Solution().generate(1))
# Output: [[1]]
```
