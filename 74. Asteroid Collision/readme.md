# Asteroid Collision - LeetCode

## Problem Description

The **Asteroid Collision** problem asks us to simulate collisions between asteroids represented by integers in a list. Each integer's absolute value is the size of the asteroid, and the sign represents its direction:

* Positive integers move to the **right**.
* Negative integers move to the **left**.

Asteroids move at the same speed. If two asteroids meet:

* The smaller one explodes.
* If they are the same size, both explode.
* Asteroids moving in the same direction never collide.

The task is to return the state of the asteroids after all possible collisions.

### Example 1:

* Input: `asteroids = [5, 10, -5]`
* Output: `[5, 10]`
* Explanation: `10` and `-5` collide. `10` survives.

### Example 2:

* Input: `asteroids = [8, -8]`
* Output: `[]`
* Explanation: `8` and `-8` collide and both explode.

### Example 3:

* Input: `asteroids = [10, 2, -5]`
* Output: `[10]`
* Explanation: `2` and `-5` collide. Then `10` and `-5` collide. `10` survives.

### Constraints:

* `2 <= asteroids.length <= 10^4`
* `-1000 <= asteroids[i] <= 1000`
* `asteroids[i] != 0`

---

## Stack-Based Solution

```python
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Used to track surviving asteroids

        for a in asteroids:
            # Handle collision while there is a right-moving asteroid and a left-moving asteroid
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]  # Compute net effect of collision
                if diff < 0:
                    # New asteroid is bigger, pop the one from stack and continue
                    stack.pop()
                elif diff > 0:
                    # Stack asteroid is bigger, new one is destroyed
                    a = 0
                else:
                    # Both are equal, destroy both
                    a = 0
                    stack.pop()

            # If current asteroid survived all possible collisions, add it to stack
            if a:
                stack.append(a)

        return stack  # Remaining asteroids after all collisions
```

---

## Explanation of Code

* A **stack** is used to simulate the list of asteroids moving in space.
* When a new asteroid appears:

  * If it moves **left** (`< 0`) and the top of the stack is moving **right** (`> 0`), a collision occurs.
  * We resolve the collision by comparing sizes.
  * The bigger asteroid survives; if both are equal, both are removed.
* If the asteroid does not collide or survives the collision, it is added to the stack.

This approach allows us to simulate collisions in order with minimal operations.

---

## Time and Space Complexities

* **Time Complexity:** `O(n)` where `n` is the number of asteroids. Each asteroid is pushed and popped at most once.
* **Space Complexity:** `O(n)` in the worst case where no collisions happen, and all asteroids are stored in the stack.

### Why is it optimal?

* This is optimal because it ensures each asteroid is processed only once and uses a single stack for storage, making it both time and space efficient.

---

## Test Cases

```python
# Test Case 1:
asteroids1 = [5, 10, -5]
print(Solution().asteroidCollision(asteroids1))  # Output: [5, 10]

# Test Case 2:
asteroids2 = [8, -8]
print(Solution().asteroidCollision(asteroids2))  # Output: []

# Test Case 3:
asteroids3 = [10, 2, -5]
print(Solution().asteroidCollision(asteroids3))  # Output: [10]
```