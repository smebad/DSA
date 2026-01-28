# Number of Visible People in a Queue - LeetCode

## 1. Problem Explanation

In this problem, there are `n` people standing in a queue from left to right. Each person has a unique height, given in the array `heights`, where `heights[i]` represents the height of the `i`th person.

A person at index `i` can see another person at index `j` (`i < j`) if **every person between them is shorter than both of them**. In other words:

```
min(heights[i], heights[j]) > max(heights[i+1], ..., heights[j-1])
```

Your task is to compute an array `answer` where `answer[i]` is the number of people the `i`th person can see to their right.

If a person has no one to their right, the answer is `0`.

---

## 2. Code with Comments

```python
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n          # Result array to store visible count for each person
        stack = []             # Monotonic decreasing stack storing heights

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop all shorter people because current person can see them
            while stack and stack[-1] < heights[i]:
                stack.pop()
                res[i] += 1

            # If someone taller is still in the stack, current person can see them too
            if stack:
                res[i] += 1

            # Push current person's height onto the stack
            stack.append(heights[i])

        return res
```

---

## 3. Solution Approach and Logic

### Key Idea

The main challenge is efficiently determining who is visible without checking every possible pair. A **monotonic decreasing stack** helps solve this in linear time.

### Step-by-Step Logic

1. Traverse the queue from **right to left**.
2. Use a stack to keep track of people to the right of the current person.
3. While the stack top is shorter than the current person:

   * The current person can see them.
   * Pop them from the stack.
4. After popping shorter people:

   * If the stack is not empty, the current person can see exactly one taller person.
5. Push the current person onto the stack.

### Why This Works

* Shorter people are removed because they cannot block the view anymore.
* The first taller person remaining blocks further visibility.
* Each person is pushed and popped **at most once**, making the solution efficient.

---

## 4. Time and Space Complexity

### Time Complexity

* **O(n)**
* Each person is pushed onto the stack once and popped once.

### Space Complexity

* **O(n)** in the worst case when the stack stores all people.

### Most Optimal Solution

The monotonic stack solution is the most optimal approach because:

* It processes each element a constant number of times.
* It avoids nested loops.
* It works efficiently even for the maximum constraint of `10^5` people.

This makes it both time-efficient and practical for large inputs.

---

## 5. Example Walkthrough

**Input:**

```
heights = [10, 6, 8, 5, 11, 9]
```

**Output:**

```
[3, 1, 2, 1, 1, 0]
```

Each person counts how many people they can see to their right following the rules, using the stack logic described above.

---

## 6. Summary

* This problem is about visibility based on height.
* A monotonic decreasing stack is the key data structure.
* The solution runs in linear time and is optimal.
* Understanding stack behavior makes many similar problems easier to solve.