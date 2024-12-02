# Pair Sum Problem

## Introduction
The Pair Sum problem involves finding two distinct indices in a list where the corresponding elements sum up to a given target value. The function should return a tuple containing these indices. The indices must be unique, and there is guaranteed to be exactly one pair that satisfies the condition.

This README explains the problem, two different approaches to solve it, and their respective time complexities.

---

## Problem Description
**Function Definition**:  
`pair_sum(numbers: List[int], target_sum: int) -> Tuple[int, int]`

### Input
- `numbers`: A list of integers.
- `target_sum`: The target integer value that the sum of two elements in the list should be equal.

### Output
- A tuple of two integers, representing the indices of the pair of numbers whose sum equals `target_sum`.

### Example
```python
pair_sum([3, 2, 5, 4, 1], 8)  # Output: (0, 2)
```
## Solutions
### 1. Brute Force Solution:
This approach uses two nested loops to iterate over all possible pairs of elements in the list. For each pair, it checks whether their sum equals the target. If a pair is found, it returns their indices.

```python
def pair_sum(numbers, target_sum):
    # Iterate through each element as the first number
    for i in range(0, len(numbers)):
        # Iterate through each subsequent element as the second number
        for j in range(i + 1, len(numbers)):
            # Check if the sum matches the target
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)
```
### Steps:
1. Use two nested loops to iterate over all unique pairs of elements.
2. For each pair (i, j), check if numbers[i] + numbers[j] == target_sum.
3. If a match is found, return the indices (i, j).

### Time Complexity:
* Time: O(n^2)
  * The algorithm compares every pair of elements, leading to a quadratic time complexity.
* Space: O(1)
  * No extra space is used beyond the input.

### 2. Optimized Solution (Using a Hash Map):
This approach uses a hash map (dictionary) to store numbers and their indices while iterating through the list. For each number, it checks if the complement (difference between the target and the current number) exists in the hash map.

```python
def pair_sum(numbers, target_sum):
    # Dictionary to store numbers and their indices
    previous_numbers = {}
    
    # Iterate through the list
    for index, num in enumerate(numbers):
        # Calculate the complement
        complement = target_sum - num
        
        # Check if the complement exists in the dictionary
        if complement in previous_numbers:
            return (index, previous_numbers[complement])
        
        # Store the current number with its index in the dictionary
        previous_numbers[num] = index
```
### Steps:
1. Create an empty dictionary to store numbers and their indices.
2. For each number in the list, calculate its complement (target_sum - num).
3. Check if the complement exists in the dictionary:
      * If it does, return the current index and the index of the complement.
      * Otherwise, store the current number and its index in the dictionary.

### Time Complexity:
* Time: O(n)
  * Each element is processed once, and dictionary operations (insert and lookup) are O(1).
* Space: O(n)
  * The dictionary stores up to n elements.

## Comparison of Solutions

| **Aspect**          | **Brute Force Solution**         | **Optimized Solution**         |
|----------------------|-----------------------------------|---------------------------------|
| **Time Complexity**  | \(O(n^2)\)                      | \(O(n)\)                       |
| **Space Complexity** | \(O(1)\)                        | \(O(n)\)                       |
| **Approach**         | Exhaustive search using nested loops. | Hash map for efficient lookups. |
| **Efficiency**       | Slow for large lists.            | Scales well for large lists.    |

## Test Cases
```python
# Test Case 0
print(pair_sum([3, 2, 5, 4, 1], 8))  # -> (0, 2)

# Test Case 1
print(pair_sum([4, 7, 9, 2, 5, 1], 5))  # -> (0, 5)

# Test Case 2
print(pair_sum([4, 7, 9, 2, 5, 1], 3))  # -> (3, 5)

# Test Case 3
print(pair_sum([1, 6, 7, 2], 13))  # -> (1, 2)

# Test Case 4
print(pair_sum([9, 9], 18))  # -> (0, 1)

# Test Case 5
print(pair_sum([6, 4, 2, 8], 12))  # -> (1, 3)

# Test Case 6
numbers = [i for i in range(1, 6001)]
print(pair_sum(numbers, 11999))  # -> (5998, 5999)
```

## Conclusion
The optimized solution is significantly more efficient than the brute force solution due to its O(n) time complexity, making it ideal for larger input sizes. Use the brute force method for understanding the problem or small datasets, and prefer the optimized approach for practical applications.
