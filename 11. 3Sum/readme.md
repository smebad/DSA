# 3Sum - LeetCode DSA Problem

## Problem Description
The **3Sum** problem is a classic algorithmic challenge that involves finding triplets in an array that add up to zero. Given an integer array `nums`, your task is to return all unique triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

**Note:** The solution set must not contain duplicate triplets.

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Example
**Input:** `nums = [-1, 0, 1, 2, -1, -4]`

**Output:** `[[-1, -1, 2], [-1, 0, 1]]`

**Explanation:**
- `-1 + 0 + 1 = 0`
- `-1 + -1 + 2 = 0`
- The solution set only includes unique triplets.

---

## Solutions

### 1. Brute Force Solution
This solution checks all possible triplets using three nested loops.

```python
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
```

#### Time Complexity: `O(n^3)`
- Iterates through all possible combinations of triplets.

#### Space Complexity: `O(m)`
- Where `m` is the number of unique triplets.

#### Explanation:
- Sorts the input array.
- Uses three nested loops to try all combinations.
- Stores results in a set to avoid duplicates.
- Converts the set of tuples back to list format for the output.

### 2. Two Pointers Solution (Optimal)
This is a more efficient solution using sorting and the two-pointer technique.

```python
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break  # No need to continue if the first number is > 0

            if i > 0 and a == nums[i - 1]:
                continue  # Skip duplicate elements

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
```

#### Time Complexity: `O(n^2)`
- Outer loop runs `n` times.
- Inner two-pointer loop runs in `O(n)` for each outer loop iteration.

#### Space Complexity: `O(1)` (excluding output)
- No extra space used besides the output list.

#### Explanation:
- Sorts the input array.
- Uses an outer loop to fix one number `a`.
- Then uses two pointers to find the other two numbers such that the sum is 0.
- Skips duplicates to ensure unique triplets.

---

## Optimal Solution
The **Two Pointers** approach is the most optimal among the two. It brings down the time complexity from `O(n^3)` to `O(n^2)` by leveraging the sorted nature of the array. This method also uses constant extra space, making it efficient in both time and memory.

This problem is a great exercise in understanding the power of sorting combined with pointer techniques to optimize brute force solutions.