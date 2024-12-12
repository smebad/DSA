# Five Sort Problem

## Problem Description
The **Five Sort** problem involves writing a function, `five_sort`, that takes a list of numbers as input and rearranges its elements such that all occurrences of the number `5` appear at the end of the list. The function should modify the list in-place, without creating a new list, and return the modified list.

Elements in the list that are not `5` can appear in any order in the output as long as the `5`s are all moved to the end.

## Solution Overview
To solve this problem, we employ the **two-pointers technique**:

1. **Pointers Initialization**: We initialize two pointers:
   - `i`: Points to the start of the list.
   - `j`: Points to the end of the list.
2. **Pointer Movement**:
   - If the element at `j` is `5`, we simply decrement `j` to skip it.
   - If the element at `i` is `5`, we swap the values at `i` and `j`, then increment `i` and decrement `j`.
   - If neither condition is met, we increment `i` to check the next element.
3. **Loop Termination**: The loop terminates when `i` meets or exceeds `j`.

This approach ensures that all `5`s are moved to the end efficiently without using extra space.

## Code Implementation
```python
# Solution - Using Two Pointers

def five_sort(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:
            i += 1
    return nums
```

## Example Test Cases
```python
# Test Case 1
print(five_sort([12, 5, 1, 5, 12, 7]))  # Output: [12, 7, 1, 12, 5, 5]

# Test Case 2
print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))  # Output: [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]

# Test Case 3
print(five_sort([5, 5, 6, 5, 5, 5, 5]))  # Output: [6, 5, 5, 5, 5, 5, 5]

# Test Case 4
print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]))  # Output: [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]

# Test Case 5
fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
print(five_sort(nums))
# Output: twenty-thousand 4s followed by twenty-thousand 5s
```

## Complexity Analysis
### Time Complexity
The solution has a time complexity of **O(n)**, where `n` is the size of the input list. This is because each pointer (`i` and `j`) traverses the list at most once.

### Space Complexity
The solution has a space complexity of **O(1)** since it operates directly on the input list and does not use additional data structures.

## Conclusion
The `five_sort` function is an efficient and in-place solution to the problem, leveraging the two-pointers technique to achieve optimal time and space complexity. The approach ensures correctness while maintaining simplicity and readability.