# Car Fleet - Leetcode

## Problem Description

You are given a target distance and two arrays: `position` and `speed`. Each index `i` in these arrays represents a car: `position[i]` is its starting mile from the origin, and `speed[i]` is the car's speed in miles per hour.

The goal is to find out how many car fleets will arrive at the destination. A car fleet is a group of cars that travel together at the same speed because no car can overtake another. If a faster car catches up with a slower one before reaching the destination, they become part of the same fleet and move together at the slower car's speed.

### Example 1:
**Input**: `target = 12`, `position = [10,8,0,5,3]`, `speed = [2,4,1,1,3]`  
**Output**: `3`  
**Explanation**:
- Cars at positions 10 and 8 meet at the target forming a fleet.
- Car at position 0 does not catch up with any others.
- Cars at 5 and 3 meet before reaching target and become a fleet.

### Example 2:
**Input**: `target = 10`, `position = [3]`, `speed = [3]`  
**Output**: `1`

### Example 3:
**Input**: `target = 100`, `position = [0,2,4]`, `speed = [4,2,1]`  
**Output**: `1`

## Constraints
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- All `position[i]` values are unique
- `0 < speed[i] <= 10^6`

---

## Solution

We can solve this problem using a **greedy stack based** approach. Here's the Python code:

```python
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Pair up each car's position and speed
        pair = [(p, s) for p, s in zip(position, speed)]

        # Step 2: Sort the cars in descending order of their positions
        pair.sort(reverse=True)

        # Step 3: Initialize an empty stack to track fleet arrival times
        stack = []

        # Step 4: Iterate through the sorted pairs
        for p, s in pair:
            # Calculate time taken by current car to reach the target
            time = (target - p) / s
            stack.append(time)

            # If the current car catches up to the fleet ahead, pop it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Step 5: The number of elements in stack is the number of fleets
        return len(stack)
```

### Step by Step Explanation

1. **Pairing**: Create a list of tuples where each tuple has `(position, speed)`.
2. **Sorting**: Sort these pairs in descending order of `position` so we process the cars closest to the destination first.
3. **Stack**: Initialize a stack that keeps track of the time each fleet takes to reach the destination.
4. **Calculating Time**: For each car, calculate the time it would take to reach the destination.
5. **Fleet Formation**:
   - If a car takes less or equal time than the car in front, it will catch up and form a fleet.
   - Pop the faster car from the stack as it becomes part of the same fleet.
6. **Final Count**: The number of distinct times left in the stack gives the number of fleets.

### Time and Space Complexity

- **Time Complexity**: `O(n log n)`
  - Sorting the pairs takes `O(n log n)`.
  - Traversing the list and stack operations take `O(n)`.

- **Space Complexity**: `O(n)`
  - The stack holds at most `n` elements in the worst case.

### Optimality

This solution is the most optimal because:
- It leverages sorting to process cars in the correct order.
- It uses a stack to efficiently simulate fleet formation without nested loops.
- It completes in linearithmic time, which is ideal given the constraints (`n` up to `10^5`).

---

## Test Cases
```python
# Test Case 1
print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # Output: 3

# Test Case 2
print(Solution().carFleet(10, [3], [3])) # Output: 1

# Test Case 3
print(Solution().carFleet(100, [0,2,4], [4,2,1])) # Output: 1
```

This solution efficiently solves the car fleet problem while maintaining clarity and simplicity through the use of a greedy strategy and stack data structure.
