# Path Crossing - LeetCode

## Problem Explanation

A **Path Crossing** problem is about determining whether a path on a 2D plane crosses itself.

You are given a string `path`, where:

* Each character represents a movement in one of four directions:

  * `'N'` → move **north** (up) by 1 unit.
  * `'S'` → move **south** (down) by 1 unit.
  * `'E'` → move **east** (right) by 1 unit.
  * `'W'` → move **west** (left) by 1 unit.

You start at the **origin (0,0)** and follow the path. The task is to check whether you ever visit the same coordinate more than once.

* If the path crosses itself, return `True`.
* If it does not cross, return `False`.

### Example 1:

**Input:** `path = "NES"`
**Output:** `False`
**Explanation:** The path goes north, east, then south. No point is visited twice.

### Example 2:

**Input:** `path = "NESWW"`
**Output:** `True`
**Explanation:** The path returns to the origin `(0,0)`, so it crosses itself.

---

## Solution (Hash Set)

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Dictionary to represent movement directions
        dir = {
            'N': [0, 1],   # Move up (y + 1)
            'S': [0, -1],  # Move down (y - 1)
            'E': [1, 0],   # Move right (x + 1)
            'W': [-1, 0]   # Move left (x - 1)
        }

        visit = set()       # Store all visited coordinates
        x, y = 0, 0         # Start at the origin (0,0)

        for c in path:
            visit.add((x, y))       # Mark the current position as visited
            dx, dy = dir[c]         # Get movement direction for the step
            x, y = x + dx, y + dy   # Update position

            # If the new position was already visited, path crosses itself
            if (x, y) in visit:
                return True

        return False  # No crossing found
```

---

## Approach and Logic

1. **Representation of movement**:

   * A dictionary `dir` maps each direction to a coordinate change `(dx, dy)`.
   * For example, `'N'` → `(0,1)` means move one step upward.

2. **Tracking visited positions**:

   * We use a **hash set** `visit` to store visited coordinates.
   * At every step, we add the current position to `visit` before moving.

3. **Checking crossing**:

   * After moving, if the new position is already in `visit`, it means we visited it earlier → return `True`.

4. **No crossing**:

   * If the loop ends without detecting a repeated position, return `False`.

---

## Explanation in Simple Words

Imagine you are walking on graph paper:

* Every step you mark the square you stand on.
* If at any time you step on a square that already has a mark, you crossed your path.
* If not, you keep moving without crossing.

This solution works by recording every square you visit and checking if you land on a marked one again.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * We process each character in the path once.
  * Lookup and insertion in a set take constant time on average.

* **Space Complexity:** `O(n)`

  * In the worst case, we visit all positions uniquely, so we store up to `n` positions.

---

## Optimality

This **hash set solution** is optimal because:

* You must check every step to know if the path crosses.
* Using a set ensures **constant-time checking** of whether a coordinate has already been visited.
* The problem cannot be solved in less than `O(n)` time since every step needs to be examined.

Thus, this approach is both **time-optimal and space-optimal** within the problem constraints.

---

## Test Cases

```python
solution = Solution()

# Test Case 1
print(solution.isPathCrossing("NES"))   # False

# Test Case 2
print(solution.isPathCrossing("NESWW")) # True

# Test Case 3
print(solution.isPathCrossing("N"))     # False (only one move, no crossing)

# Test Case 4
print(solution.isPathCrossing("NS"))    # True (returns to origin)
```