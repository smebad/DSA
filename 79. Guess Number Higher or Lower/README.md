# Guess Number Higher or Lower - LeetCode

## Problem Description

"Guess Number Higher or Lower" is a classic search problem where you have to guess a number that has been pre-selected from the range `1` to `n`. You are given a feedback mechanism through a predefined API called `guess(int num)`, which tells you if your guess is:

* `-1`: Your guess is **higher** than the target.
* `1`: Your guess is **lower** than the target.
* `0`: Your guess is **correct**.

The task is to implement an algorithm that returns the correct number using the fewest possible guesses.

---

## Binary Search Solution

```python
# The guess API is simulated for local testing
# Returns -1, 1, or 0 based on comparison with the correct number

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            m = (l + r) // 2  # Find the midpoint
            res = guess(m)    # Get result from guess API
            if res > 0:
                l = m + 1     # Target is higher
            elif res < 0:
                r = m - 1     # Target is lower
            else:
                return m      # Target found
```

### Explanation with Comments

* Use binary search to minimize the number of guesses.
* Maintain two pointers `l` and `r` to represent the current search space.
* Calculate the midpoint `m` and use `guess(m)` to adjust the search range.
* Repeat until the correct number is found.

---

## Linear Search Solution

```python
# The guess API is simulated for local testing

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        for num in range(1, n + 1):
            if guess(num) == 0:
                return num
```

### Explanation with Comments

* Use a simple `for` loop to check each number from `1` to `n`.
* Return the number once `guess(num)` returns 0.
* This is a brute-force solution suitable for small `n`.

---

## Approach and Logic

### Binary Search Approach

* The binary search approach is optimal.
* Reduces the search space by half at each step.
* Uses feedback from the `guess()` function to decide which direction to continue searching.

### Linear Search Approach

* Simple to understand and implement.
* Iterates from the lowest possible value up to `n` until the correct number is found.
* Inefficient for large ranges.

---

## Time and Space Complexities

### Binary Search

* **Time Complexity**: O(log n)

  * Divides the range in half at each step.
* **Space Complexity**: O(1)

  * Uses constant extra memory.

### Linear Search

* **Time Complexity**: O(n)

  * Checks every number from 1 to n.
* **Space Complexity**: O(1)

  * Uses constant extra memory.

---

## Why Binary Search is Optimal

* Binary search guarantees the minimal number of API calls.
* Efficient for large input sizes.
* Directly leverages the sorted nature of the range.

---

## Test Cases

```python
# Test Case 1
pick = 6
print("Test Case 1:", Solution().guessNumber(10))  # Output: 6

# Test Case 2
pick = 1
print("Test Case 2:", Solution().guessNumber(1))   # Output: 1

# Test Case 3
pick = 1
print("Test Case 3:", Solution().guessNumber(2))   # Output: 1
```
