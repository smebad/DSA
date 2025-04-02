# Two Sum - Leetcode Blind 75

## Problem Statement
The **Two Sum** problem is a fundamental problem in data structures and algorithms. Given an array of integers `nums` and an integer `target`, the goal is to find two indices `i` and `j` such that:

```
nums[i] + nums[j] == target  (where i != j)
```

Every input is assumed to have exactly one pair of indices that satisfy the condition. The output should return these indices in ascending order.

### Example 1:
```python
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
```

### Example 2:
```python
Input: nums = [4,5,6], target = 10
Output: [0,2]
```

### Example 3:
```python
Input: nums = [5,5], target = 10
Output: [0,1]
```

### Constraints:
- `2 <= nums.length <= 1000`
- `-10,000,000 <= nums[i] <= 10,000,000`
- `-10,000,000 <= target <= 10,000,000`

---

## Solutions

### 1. Brute Force Approach
This approach checks all pairs of numbers in the list by using a nested loop to find a pair that sums up to the target.

#### Implementation:
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

#### Time and Space Complexity:
- **Time Complexity:** O(n^2) due to the nested loops.
- **Space Complexity:** O(1), as we are using only a few extra variables.

#### Test Cases:
```python
sol = Solution()
print(sol.twoSum([3, 4, 5, 6], 7))  # Output: [0, 1]
print(sol.twoSum([4, 5, 6], 10))    # Output: [0, 2]
```

---

### 2. Optimized Approach Using HashMap (One-Pass)
This approach uses a hash map to store the numbers seen so far and checks if the complement (target - current number) exists in the map. If it does, we return the indices.

#### Implementation:
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```

#### Time and Space Complexity:
- **Time Complexity:** O(n), as we traverse the list once.
- **Space Complexity:** O(n), as we store elements in the hash map.

#### Test Cases:
```python
sol = Solution()
print(sol.twoSum([3, 4, 5, 6], 7))  # Output: [0, 1]
print(sol.twoSum([4, 5, 6], 10))    # Output: [0, 2]
```

---

## Summary
| Approach  | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n^2)         | O(1)             |
| HashMap (Optimized) | O(n)  | O(n)             |

The **optimized approach using HashMap** is the recommended method for solving the Two Sum problem efficiently.

---

## Notes
- The brute force method is straightforward but inefficient for large inputs.
- The hash map solution significantly improves performance by reducing the lookup time to O(1).
- This problem is a part of the **LeetCode Blind 75** list, making it an essential problem for coding interviews.

