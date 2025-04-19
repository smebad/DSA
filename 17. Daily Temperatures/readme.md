# Daily Temperatures - Leetcode

## Problem Statement
Given an array of integers `temperatures` that represent the daily temperatures, the task is to return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Example 1:
- **Input:** `temperatures = [73,74,75,71,69,72,76,73]`
- **Output:** `[1,1,4,2,1,1,0,0]`

### Example 2:
- **Input:** `temperatures = [30,40,50,60]`
- **Output:** `[1,1,1,0]`

### Example 3:
- **Input:** `temperatures = [30,60,90]`
- **Output:** `[1,1,0]`

### Constraints:
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## Brute Force Solution

### Code:
```python
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res
```

### Explanation:
- For each day, the algorithm checks every subsequent day to find a warmer temperature.
- If it finds a warmer temperature, it counts the number of days waited and stores it in the result.
- If it doesn’t find one, it stores 0.

### Time Complexity:
- **O(n^2)** where `n` is the length of the `temperatures` array because each element may require scanning all the subsequent elements.

### Space Complexity:
- **O(n)** for the result array.

This brute force approach works well for small inputs but is not suitable for large input sizes due to its quadratic time complexity.

---

## Optimal Stack-Based Solution

### Code:
```python
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
```

### Explanation:
- This solution uses a monotonic stack to keep track of temperature indices.
- For each temperature `t` at index `i`, it checks whether `t` is warmer than the temperature at the index on top of the stack.
- If it is, the difference in indices is calculated and stored.
- This ensures that each index is pushed and popped at most once.

### Time Complexity:
- **O(n)** where `n` is the length of the `temperatures` array, as each element is pushed and popped from the stack at most once.

### Space Complexity:
- **O(n)** for the stack and the result array.

This is the most efficient solution for the problem. The stack based method is optimal because it avoids unnecessary comparisons and reduces the number of operations to a linear scale.

---

## Summary
- The brute force solution checks each possible next day for a warmer temperature and has a time complexity of O(n^2).
- The optimal solution uses a stack to efficiently determine the next warmer day for each day and works in linear time.
- For large inputs, the stack-based solution is recommended due to its better performance.
