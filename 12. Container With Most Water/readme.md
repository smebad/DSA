# Container With Most Water - LeetCode Problem

## Problem Description

The "Container With Most Water" is a popular data structures and algorithms (DSA) problem on LeetCode.

You are given an integer array `height` of length `n`. Each index in the array represents a vertical line with height `height[i]`, and all lines are placed at equal distance from each other. Your task is to find the two lines that, together with the x-axis, form a container such that it holds the most water.

### Constraints:
- 2 <= height.length <= 10^5
- 0 <= height[i] <= 10^4

### Example 1:
**Input:** height = [1,8,6,2,5,4,8,3,7]  
**Output:** 49  
**Explanation:** The maximum area is formed between the lines at indices 1 and 8. The shorter line has height 7, and the width between them is 7. So, the area is 7 * 7 = 49.

### Example 2:
**Input:** height = [1,1]  
**Output:** 1

---

## Brute Force Solution

```python
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
```

### Step-by-Step Explanation:
1. Initialize `res` to 0.
2. Iterate over all pairs `(i, j)` where `i < j`.
3. Calculate the area by taking the minimum of the two heights and multiplying by the distance `(j - i)`.
4. Keep track of the maximum area encountered.

### Time and Space Complexity:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)

This solution works but is not efficient for large input sizes.

---

## Optimal Solution: Two Pointers Approach

```python
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
```

### Step-by-Step Explanation:
1. Initialize two pointers: `l` at the beginning and `r` at the end of the array.
2. Calculate the area using the heights at `l` and `r`.
3. Update `res` if this area is larger.
4. Move the pointer pointing to the shorter line inward to potentially find a taller line.
5. Repeat until `l` meets `r`.

### Time and Space Complexity:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This solution is optimal and significantly faster than the brute force approach, making it ideal for large input sizes.

---

## Conclusion
The "Container With Most Water" problem challenges your ability to find an optimal solution using pointer-based techniques. The brute force approach is easy to understand but inefficient, while the two-pointer method offers a smart and optimal way to solve the problem in linear time.

---

## Test Cases
```python
# Test Case 1:
heights = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(heights))  # Expected Output: 49

# Test Case 2:
heights = [1,1]
print(Solution().maxArea(heights))  # Expected Output: 1

# Test Case 3:
heights = [4,3,2,1,4]
print(Solution().maxArea(heights))  # Expected Output: 16
```