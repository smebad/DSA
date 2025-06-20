# Baseball Game - LeetCode

## Problem Description

The **Baseball Game** problem requires maintaining a record of scores according to a specific set of operations. Each operation modifies the record in a particular way. After processing all operations, return the total sum of the scores on the record.

Given a list of operations (as strings), perform the following:

* An integer x: Add x to the record.
* "+": Add a score that is the sum of the previous two scores.
* "D": Add a score that is double the previous score.
* "C": Remove the previous score from the record.

All operations are guaranteed to be valid.

### Example 1:

* Input: `ops = ["5", "2", "C", "D", "+"]`
* Output: `30`
* Explanation:

  * Add 5: \[5]
  * Add 2: \[5, 2]
  * Cancel previous (2): \[5]
  * Double last (5\*2): \[5, 10]
  * Sum last two (5+10): \[5, 10, 15] => Total = 30

### Example 2:

* Input: `ops = ["5","-2","4","C","D","9","+","+"]`
* Output: `27`

### Example 3:

* Input: `ops = ["1", "C"]`
* Output: `0`

### Constraints:

* `1 <= operations.length <= 1000`
* `operations[i]` is "C", "D", "+", or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`
* Each operation is valid and adheres to the rules.

---

## Stack-Based Solution

```python
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []  # Used to keep track of valid scores

        for op in operations:
            if op == "+":
                # Add the sum of the last two scores
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Add double the last score
                stack.append(2 * stack[-1])
            elif op == "C":
                # Remove the last score
                stack.pop()
            else:
                # Convert string to int and append
                stack.append(int(op))

        return sum(stack)  # Return the sum of all valid scores
```

---

## Code Explanation with Comments

* `stack = []`: Initializes an empty list to store scores.
* `for op in operations:`: Loops through each operation.

  * `if op == "+"`: Adds the last two valid scores and pushes the result.
  * `elif op == "D"`: Doubles the last valid score and adds it.
  * `elif op == "C"`: Pops/removes the last score from the stack.
  * `else`: Converts the string to an integer and appends it to the stack.
* `return sum(stack)`: Returns the sum of all valid scores after processing all operations.

---

## Approach and Logic

The solution uses a **stack** (a list in Python) to store valid scores. This is ideal because:

* We often need to access or remove the **most recent** score, which is efficiently done using a stack (LIFO - Last In First Out).
* It allows us to backtrack (with 'C'), double previous ('D'), or combine scores ('+') without losing access to the order of operations.

### Summary of Operations:

* **Push Integer**: Add to the stack.
* **C**: Pop last score.
* **D**: Push double the last score.
* **+**: Push sum of last two scores.

---

## Time and Space Complexities

* **Time Complexity:** `O(n)`

  * We process each operation exactly once.
* **Space Complexity:** `O(n)`

  * In the worst case, we store all scores in the stack.

### Why This is Optimal

* All operations are processed in linear time.
* Stack ensures easy access to recent scores, allowing efficient implementation.
* No unnecessary passes over the data.

---

## Test Cases

```python
# Test Case 1
ops = ["5", "2", "C", "D", "+"]
print(Solution().calPoints(ops))  # Expected Output: 30

# Test Case 2
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(Solution().calPoints(ops))  # Expected Output: 27

# Test Case 3
ops = ["1", "C"]
print(Solution().calPoints(ops))  # Expected Output: 0
```
