# Concatenation of Array - LeetCode

## Problem Statement

Given an integer array `nums` of length `n`, the goal is to create an array `ans` of length `2n` such that:

* `ans[i] == nums[i]` and
* `ans[i + n] == nums[i]`

for `0 <= i < n`. In simpler terms, you need to concatenate the `nums` array with itself.

### Example 1

**Input:** `nums = [1,2,1]`
**Output:** `[1,2,1,1,2,1]`
**Explanation:** The array `ans` is formed by repeating the `nums` array twice.

### Example 2

**Input:** `nums = [1,3,2,1]`
**Output:** `[1,3,2,1,1,3,2,1]`
**Explanation:** Again, the array is just `nums` followed by `nums`.

### Constraints

* `n == nums.length`
* `1 <= n <= 1000`
* `1 <= nums[i] <= 1000`

---

## Code Explanation

```python
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []  # Initialize an empty list to store the result
        for i in range(2):  # Repeat the process twice to concatenate nums with itself
            for num in nums:  # Loop through each element in nums
                ans.append(num)  # Append the element to the result list
        return ans  # Return the final concatenated list
```

---

## Approach and Logic

This problem is quite straightforward and can be approached using a simple loop.

### Solution: Iteration

* We use a for-loop that runs twice (since we want to concatenate the array with itself).
* For each iteration, we loop through the `nums` array and add each element to the result list `ans`.
* This way, we append all elements of `nums` two times, resulting in the desired output.

## Time and Space Complexity

### Time Complexity: `O(n)`

* We iterate over the `nums` list twice.
* Since each element is visited exactly twice, the time complexity remains linear, i.e., `O(n)`.

### Space Complexity: `O(n)`

* We create a new list `ans` that contains `2n` elements, which takes linear space.

### Another (not recommended) Solution

The another one line (not recommended) solution in terms of both readability and performance which I will not be adding in the python file is:

```python
return nums * 2
```

* **This one line solution**

  * It leverages built-in operations optimized in Python.
  * Fewer lines of code make it easier to maintain and understand.
  * Still maintains `O(n)` time and space complexity.

---

## Test Cases

```python
# Test Case 1:
nums = [1, 2, 1]
sol = Solution()
print(sol.getConcatenation(nums))  # Output: [1, 2, 1, 1, 2, 1]

# Test Case 2:
nums = [1, 3, 2, 1]
print(sol.getConcatenation(nums))  # Output: [1, 3, 2, 1, 1, 3, 2, 1]
```

---

## Summary

* This problem helps practice array manipulation.
* The key idea is to understand how to construct a new array by repeating an existing one.
* The iterative solution is easy to implement, and Python's syntactic sugar offers an even simpler one-liner solution.
