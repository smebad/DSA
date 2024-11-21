# Max Value Problem

## Problem Description
Write a function, `max_value`, that takes in a list of numbers as an argument and returns the largest number in the list. The solution should be implemented **without using any built-in list methods** like `max()`.

---

## Solution

The function iterates through the list, keeping track of the largest number encountered so far. It handles edge cases such as empty lists by initializing the maximum value to negative infinity (`float('-inf')`).

### Code Implementation
```python
def max_value(nums):
    max_num = float('-inf')  # Start with negative infinity
    for num in nums:
        if num > max_num:  # Update if a larger number is found
            max_num = num
    return max_num
```
# Test cases
```python
if __name__ == "__main__":
    print(max_value([3, 1, 4, 1, 5, 9]))  # Output: 9
    print(max_value([-10, -20, -30, -5]))  # Output: -5
    print(max_value([7]))  # Output: 7
    print(max_value([]))  # Output: float('-inf')
```
