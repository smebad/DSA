# Sum Numbers Recursive

## Problem Description
The problem is to write a function, `sum_numbers_recursive`, that takes in an array of numbers and returns the sum of all the numbers in the array. The solution must be implemented **recursively**. All elements in the input array are guaranteed to be integers.

---

## Understanding Recursion
Recursion is a problem-solving technique where a function calls itself in order to break the problem down into smaller subproblems. Each recursive function must have:
1. **Base Case**: This stops the recursion when the problem is small enough to solve directly.
2. **Recursive Case**: This reduces the problem into smaller instances and calls itself on these instances.

In this problem:
- The base case occurs when the input array is empty (`len(numbers) == 0`). At this point, the sum is `0`.
- The recursive case reduces the problem by summing the first element (`numbers[0]`) and recursively calling the function on the rest of the array (`numbers[1:]`).

---

## Recursive Approach
The function can be implemented as follows:

```python
def sum_numbers_recursive(numbers):
  if len(numbers) == 0:  # Base case
    return 0
  return numbers[0] + sum_numbers_recursive(numbers[1:])  # Recursive case
```
---

### Explanation of the Solution:

1. **Base Case**:  
   If the input array is empty, return `0`.

2. **Recursive Case**:  
   Otherwise, take the first element (`numbers[0]`) and add it to the result of recursively summing the rest of the array (`numbers[1:]`).

3. **Process**:  
   This process continues until the base case is reached.

---

### Example Test Cases
Here are a few test cases to demonstrate the functionality of the function:

``` python
# Test Case 1
print(sum_numbers_recursive([5, 2, 9, 10]))  # Output: 26

# Test Case 2
print(sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]))  # Output: 1

# Test Case 3
print(sum_numbers_recursive([]))  # Output: 0

# Test Case 4
print(sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]))  # Output: 1001

# Test Case 5
print(sum_numbers_recursive([700, 70, 7]))  # Output: 777

# Test Case 6
print(sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))  # Output: -55

# Test Case 7
print(sum_numbers_recursive([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Output: 0

# Test Case 8
print(sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]))  # Output: 137174205
```
---

### Time Complexity

#### Recursive Time Complexity:
- The time complexity is determined by the size of the array and how the recursive function operates:
  1. Each recursive call processes the first element and creates a new list using `numbers[1:]`, which involves copying the rest of the array.
  2. Copying `numbers[1:]` is an **O(n)** operation.
  3. Therefore, with `n` recursive calls, the total time complexity is **O(n^2)**.

#### Space Complexity:
- Each recursive call adds a new frame to the call stack, and the maximum depth of the recursion is `n`.
- Additionally, each `numbers[1:]` creates a new list, taking **O(n)** space.  
- Hence, the space complexity is **O(n^2)**.

---

### Summary

This recursive solution breaks down the problem of summing an array into smaller subproblems. While elegant and functional, it has high time and space complexity due to the repeated creation of subarrays.  

For large arrays, an iterative approach might be more efficient. However, this recursive solution is an excellent example of how recursion can simplify problem-solving for smaller input sizes.
