# Brick Wall - LeetCode

## Problem Explanation

The "Brick Wall" problem involves a wall constructed using rows of bricks. Each row has bricks of different widths, but the total width of each row remains the same. The goal is to draw a vertical line from the top to the bottom of the wall that crosses the fewest number of bricks.

A brick is considered crossed if the vertical line goes through it. However, if the line goes through a brick edge (a gap between bricks), then that brick is not counted as crossed. The line cannot be drawn along the left or right boundary of the wall.

## Problem Statement

Given a 2D list `wall`, where each element represents a row of bricks and contains the width of each brick in that row, return the minimum number of crossed bricks after drawing such a vertical line.

---

## Key Idea

Instead of counting how many bricks the line crosses, we count how many brick edges (gaps) align vertically. The best place to draw the line is where the most gaps align, resulting in the fewest crossed bricks.

We avoid counting the final edge of each row because drawing a line at the right boundary is not allowed.

---

## Approach & Logic

1. Use a hashmap to count the frequency of brick edge positions across all rows.
2. For each row, compute cumulative widths to find gap positions.
3. Track how many rows share each gap position.
4. The optimal line passes through the maximum number of aligned gaps.
5. The minimum number of crossed bricks = total rows - maximum aligned gaps.

---

## Code Explanation

```python
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Dictionary to store frequency of each gap position
        # Start with {0: 0} to handle case where no internal gaps exist
        countGap = {0: 0}

        for r in wall:
            total = 0
            # We do not include the last brick because we cannot cut at the wall boundary
            for i in range(len(r) - 1):
                total += r[i]  # Cumulative width to represent gap position
                countGap[total] = 1 + countGap.get(total, 0)  # Count gap occurrences

        # Maximum gaps means minimum bricks crossed
        return len(wall) - max(countGap.values())
```

---

## Time Complexity

* **O(n)** where `n` is the total number of bricks in the wall
* We iterate through all bricks once to calculate gap positions

## Space Complexity

* **O(g)** where `g` is the number of unique gap positions
* Worst case, all bricks end at different positions

This is the optimal solution since we minimize passes and only track required gap positions.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
wall1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(sol.leastBricks(wall1))  # Expected output: 2

# Test Case 2
wall2 = [[1],[1],[1]]
print(sol.leastBricks(wall2))  # Expected output: 3
```