# Can Place Flowers - LeetCode

## Problem Explanation

The **Can Place Flowers** problem involves determining whether a given number of new flowers (`n`) can be planted in a `flowerbed` without violating the rule that no two flowers can be adjacent.

* The `flowerbed` is represented by a list of integers:

  * `0` means the plot is empty.
  * `1` means the plot already has a flower.
* The task is to check if we can plant `n` new flowers such that no two flowers are next to each other.

**Example:**

* Input: `flowerbed = [1,0,0,0,1]`, `n = 1` → Output: `True`
* Input: `flowerbed = [1,0,0,0,1]`, `n = 2` → Output: `False`

## Code with Comments

```python
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add a 0 at the beginning and end to handle edge cases
        f = [0] + flowerbed + [0]

        # Iterate through the flowerbed
        for i in range(1, len(f) - 1):
            # Check if the current plot and its neighbors are empty
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1  # Plant a flower here
                n -= 1    # Reduce the required number of flowers

        # If n is less than or equal to 0, we successfully planted all flowers
        return n <= 0
```

## Approach and Logic

1. **Edge Handling:**

   * By adding a `0` at the start and end of the flowerbed, we avoid writing separate logic for the first and last plots.
2. **Iteration:**

   * We scan the flowerbed from left to right.
   * For each position, if the previous, current, and next plots are all empty (`0`), we can plant a flower.
3. **Decrement `n`:**

   * Every time we plant a flower, we reduce the required count by one.
4. **Result:**

   * If `n <= 0` after planting, we return `True`; otherwise, `False`.

**Why This Works:**

* The problem only restricts adjacent flowers.
* By checking three consecutive plots at a time, we ensure we never plant next to another flower.

## Time and Space Complexity

* **Time Complexity:** `O(n)`

  * We loop through the flowerbed once, where `n` is the length of the flowerbed.
* **Space Complexity:** `O(n)`

  * We create a new list `f` that is a copy of the original flowerbed with two additional elements.

## Optimality

* The algorithm is **optimal for clarity and simplicity**, but space can be improved to `O(1)` by modifying the original list directly without adding padding.
* In an `O(1)` space approach, we would handle edge cases explicitly instead of padding.

## Test Cases

```python
solution = Solution()

# Test Case 1
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(solution.canPlaceFlowers(flowerbed1, n1))  # Expected: True

# Test Case 2
flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(solution.canPlaceFlowers(flowerbed2, n2))  # Expected: False
```