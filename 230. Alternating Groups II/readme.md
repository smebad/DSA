# Alternating Groups II - LeetCode

## Problem Description

The problem **"Alternating Groups II"** is about counting valid groups of tiles arranged in a circle. Each tile is either red (`0`) or blue (`1`).

You are given:

* An array `colors` representing the colors of tiles arranged in a **circular** manner
* An integer `k` representing the size of a group

An **alternating group** is defined as **any `k` contiguous tiles in the circle** where colors strictly alternate. This means every tile (except the first and last) must have a different color from both its left and right neighbors.

Because the tiles form a **circle**, the first and last tiles are considered adjacent.

Your task is to **count how many such alternating groups of size `k` exist**.

---

## Examples

### Example 1

```
Input: colors = [0,1,0,1,0], k = 3
Output: 3
```

There are three contiguous groups of size 3 where colors alternate.

### Example 2

```
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2
```

Only two circular windows of length 6 form valid alternating groups.

### Example 3

```
Input: colors = [1,1,0,1], k = 4
Output: 0
```

No group of size 4 alternates correctly.

---

## Sliding Window Solution

This problem can be solved efficiently using a **sliding window** approach while simulating circular behavior using modulo (`%`).

### Code With Comments

```python
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)        # Total number of tiles
        l = 0                 # Left pointer of the sliding window
        res = 0               # Stores number of valid alternating groups

        # Traverse up to N + k - 1 to simulate circular behavior
        for r in range(1, N + k - 1):
            # If two adjacent tiles have the same color,
            # the alternating pattern breaks
            if colors[r % N] == colors[(r - 1) % N]:
                l = r          # Reset the window

            # If window size exceeds k, shrink from the left
            if r - l + 1 > k:
                l += 1

            # If window size is exactly k, we found a valid group
            if r - l + 1 == k:
                res += 1
        
        return res
```

---

## Explanation of the Approach

### Key Ideas

1. Since the tiles form a **circle**, we simulate circular traversal using `index % N`.
2. We use a **sliding window** to keep track of consecutive alternating tiles.
3. If two adjacent tiles have the same color, the alternating sequence breaks and the window is reset.
4. Every time the window size becomes exactly `k`, we count it as one valid alternating group.

---

## Logic in Simple Words

* Move through the tiles as if the array continues in a loop.
* Keep expanding the window as long as the colors alternate.
* If two same colors appear next to each other, restart the window.
* Count every window of size `k` that maintains alternation.

---

## Time and Space Complexity

### Time Complexity: `O(n)`

* Each tile is visited once.
* Both pointers (`l` and `r`) only move forward.

### Space Complexity: `O(1)`

* No extra data structures are used.
* Only a few integer variables are maintained.

---

## Why This Solution Is Optimal

* A brute-force solution would check all circular subarrays of size `k`, resulting in `O(n * k)` time.
* This sliding window approach reduces it to **linear time**.
* It avoids copying arrays or duplicating data to handle circular behavior.
* This is the most efficient approach possible given the constraints.

---

## Test Cases

```python
solution = Solution()

# Test Case 1
colors1 = [0, 1, 0, 1, 0]
k1 = 3
print(solution.numberOfAlternatingGroups(colors1, k1))  # Expected output: 3

# Test Case 2
colors2 = [0, 1, 0, 0, 1, 0, 1]
k2 = 6
print(solution.numberOfAlternatingGroups(colors2, k2))  # Expected output: 2

# Test Case 3
colors3 = [1, 1, 0, 1]
k3 = 4
print(solution.numberOfAlternatingGroups(colors3, k3))  # Expected output: 0
```