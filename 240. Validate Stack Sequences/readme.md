# Validate Stack Sequences - LeetCode

## 1. Problem Explanation

**Validate Stack Sequences** is a stack simulation problem where you are given two integer arrays:

* `pushed`: the order in which elements are pushed onto a stack
* `popped`: the order in which elements are popped from the stack

All values are distinct, and both arrays contain the same elements.

### Goal

Determine whether the `popped` sequence **can be produced** by performing valid stack push and pop operations on an initially empty stack while pushing elements in the order given by `pushed`.

### Key Rules of a Stack

* Elements can only be popped from the **top** of the stack
* You must push elements in the given `pushed` order
* You can pop at any time, as long as the stack is not empty

### Output

* Return `true` if the `popped` sequence is valid
* Return `false` otherwise

---

## 2. Stack-Based With Comments

```python
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0              # Pointer for the popped array
        stack = []         # Stack to simulate push and pop operations

        # Iterate through each number in pushed
        for n in pushed:
            stack.append(n)   # Push current element onto stack

            # Try popping while the top of the stack matches popped[i]
            while i < len(popped) and stack and stack[-1] == popped[i]:
                stack.pop()   # Pop from stack
                i += 1        # Move to next popped element

        # If stack is empty, all pops were valid
        return not stack
```

### How to Remember This

* Push everything from `pushed`
* Pop whenever the stack top matches the next required pop
* If the stack ends empty, the sequence is valid

---

## 3. Two-Pointer Solution

This solution reuses the `pushed` array itself to simulate a stack, saving extra space.

```python
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = r = 0   # l = stack size, r = index in popped

        for num in pushed:
            pushed[l] = num   # Simulate pushing onto stack
            l += 1

            # Pop while top of simulated stack matches popped[r]
            while l > 0 and pushed[l - 1] == popped[r]:
                l -= 1        # Remove top element
                r += 1        # Move to next popped element

        # If simulated stack is empty, sequence is valid
        return l == 0
```

---

## 4. Solution Approach and Logic

### Core Idea

Both solutions simulate how a real stack behaves.

* You push elements in order
* You pop only when the top of the stack matches the next expected element in `popped`

If at the end everything has been popped correctly, the sequence is valid.

---

## 5. Differences Between the Two Solutions

| Aspect             | Stack Solution           | Two-Pointer Solution          |
| ------------------ | ------------------------ | ----------------------------- |
| Extra Space        | Uses a separate stack    | Uses `pushed` array itself    |
| Readability        | Very clear and intuitive | Slightly harder to understand |
| Space Complexity   | O(n)                     | O(1)                          |
| Interview Friendly | Excellent                | Advanced optimization         |

### Which One Should Beginners Use?

* Start with the **stack solution** to understand the logic
* Learn the **two-pointer solution** as an optimization technique

---

## 6. Time and Space Complexity

### Stack Solution

* **Time Complexity:** O(n)

  * Each element is pushed and popped at most once

* **Space Complexity:** O(n)

  * Stack can hold all elements in the worst case

---

### Two-Pointer Solution (Most Optimal)

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

### Why Is It Optimal?

* Avoids allocating extra memory for a stack
* Reuses the input array safely
* Maintains linear time efficiency

---

## 7. Test Cases

```python
# Test Case 1
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(Solution().validateStackSequences(pushed, popped))  # True

# Test Case 2
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(Solution().validateStackSequences(pushed, popped))  # False

# Test Case 3
pushed = [2, 1, 0]
popped = [1, 2, 0]
print(Solution().validateStackSequences(pushed, popped))  # True
```