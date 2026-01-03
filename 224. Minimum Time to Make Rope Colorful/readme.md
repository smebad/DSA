# Minimum Time to Make Rope Colorful - LeetCode

## Problem Overview

In this problem, you are given a rope with `n` balloons arranged in a line. Each balloon has a color, represented by a string `colors`, and a removal time, represented by an integer array `neededTime`.

The rope is considered **colorful** if no two adjacent balloons have the same color. If there are consecutive balloons with the same color, Bob can remove balloons to fix the rope. Removing a balloon costs a certain amount of time, and the goal is to **minimize the total removal time** while ensuring the rope becomes colorful.

You must return the minimum total time required to remove balloons so that no two adjacent balloons have the same color.

---

## Key Observations

* Only **consecutive balloons of the same color** cause a problem.
* From a group of consecutive balloons with the same color, **only one should remain**.
* To minimize time, we should **keep the balloon with the highest removal time** and remove the others.

---

## Two-Pointer Solution With Comments

```python
from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # l points to the start (or strongest balloon) of the current color group
        l, res = 0, 0

        # r traverses the rope starting from the second balloon
        for r in range(1, len(colors)):
            # If current balloon has the same color as previous group
            if colors[l] == colors[r]:
                # Remove the balloon with smaller removal time
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r  # Keep the stronger balloon
                else:
                    res += neededTime[r]
            else:
                # New color group starts
                l = r
        
        return res
```

---

## Step-by-Step Explanation of the Approach

### 1. Two Pointers Technique

* Pointer `l` represents the **balloon we want to keep** in a group of same-colored balloons.
* Pointer `r` scans through the rope to compare adjacent balloons.

### 2. Handling Same Color Balloons

When two consecutive balloons have the same color:

* We must remove **one of them**.
* To minimize total time, we remove the balloon with **smaller `neededTime`**.
* We always keep track of the balloon with the **maximum removal time** in the current group.

### 3. Handling Different Colors

* When the color changes, we move `l` to `r` because a new group starts.

### 4. Accumulating the Result

* Each removal time is added to `res`.
* At the end, `res` contains the minimum total time required.

---

## Example Walkthrough

### Input

```
colors = "aabaa"
neededTime = [1, 2, 3, 4, 1]
```

### Process

* First group: `a a` → remove the one with time `1`
* Middle balloon `b` → no action needed
* Last group: `a a` → remove the one with time `1`

### Output

```
2
```

---

## Time and Space Complexity

### Time Complexity

* **O(n)** where `n` is the length of the string.
* Each balloon is processed exactly once.

### Space Complexity

* **O(1)** extra space.
* No additional data structures are used.

---

## Why This Solution Is Optimal

* Any valid solution must inspect each balloon at least once, so **O(n)** is the best possible time complexity.
* This approach avoids sorting, extra arrays, or nested loops.
* It directly solves the problem in one pass using constant memory.

---

## Test Cases
```python
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    colors = "abaac"
    neededTime = [1,2,3,4,5]
    print(solution.minCost(colors, neededTime))  # Expected output: 3

    # Test Case 2
    colors = "abc"
    neededTime = [1,2,3]
    print(solution.minCost(colors, neededTime))  # Expected output: 0

    # Test Case 3
    colors = "aabaa"
    neededTime = [1,2,3,4,1]
    print(solution.minCost(colors, neededTime))  # Expected output: 2
    ```
