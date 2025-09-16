# Number of Students Unable to Eat Lunch - LeetCode

## Problem Explanation

The **Number of Students Unable to Eat Lunch** problem is about simulating a cafeteria scenario where students are in a queue, and sandwiches are in a stack. Each student has a preference for either a circular (0) or square (1) sandwich. The sandwiches are placed in a stack, with index 0 being the top. At each step:

* If the student at the front of the queue prefers the top sandwich, they take it and both leave.
* If not, the student goes to the end of the line.

This continues until no student in the queue wants the top sandwich. At this point, the process stops, and the remaining students cannot eat.

The goal is to return the number of students who are unable to eat.

### Example

**Input:**

```
students = [1,1,0,0], sandwiches = [0,1,0,1]
```

**Output:**

```
0
```

Explanation: All students eventually get their preferred sandwich.

**Input:**

```
students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
```

**Output:**

```
3
```

Explanation: Three students cannot get their preferred sandwiches.

---

## Code Explanation

We solve this problem efficiently using a **frequency count** approach instead of simulating the entire queue.

```python
from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)  # Start with all students
        cnt = Counter(students)  # Count preferences (0s and 1s)

        for s in sandwiches:
            if cnt[s] > 0:  # If there is a student who prefers this sandwich
                res -= 1    # One student gets their sandwich
                cnt[s] -= 1 # Decrease preference count
            else:
                break       # If no student wants this sandwich, stop

        return res
```

### Key Points in Code

* `Counter(students)` counts how many students want each sandwich type.
* For each sandwich in the stack:

  * If there is a student who wants it, serve it and reduce the count.
  * If no one wants it, stop immediately because the process ends.
* Return the number of students left (`res`).

---

## Approach and Logic

1. Instead of simulating the queue rotation, we observe that once a sandwich at the top cannot be taken, the process ends.
2. We count how many students prefer each type of sandwich.
3. Iterate through the sandwiches stack:

   * If a student preference exists for the current sandwich, serve it.
   * If no student preference exists, return the remaining students.

### Why This Works

The problem looks like it requires simulating a queue, but in reality, the **only important factor** is whether at least one student still wants the current sandwich. If not, the loop breaks.

---

## Complexity Analysis

* **Time Complexity:** `O(n)` where `n` is the number of sandwiches (or students). We only loop once through the sandwiches.
* **Space Complexity:** `O(1)`. The counter only stores preferences for `0` and `1`, which is constant space.

---

## Optimality

This frequency count method is the most optimal solution:

* It avoids simulating the queue, which could require many rotations.
* It directly counts and matches students with sandwiches in one pass.
* The logic ensures minimal time and constant space usage, making it suitable for large inputs.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(sol.countStudents(students, sandwiches))  # Output: 0

# Test Case 2
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(sol.countStudents(students, sandwiches))  # Output: 3
```