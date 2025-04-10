# Two Sum II - Input Array Is Sorted

## Problem Description
The **Two Sum II** problem is a classic algorithmic challenge in data structures and algorithms (DSA), often included in the LeetCode Blind 75 list. The task involves finding two numbers in a sorted array that sum up to a specific target value.

Given a **1-indexed** array of integers `numbers`, already sorted in non-decreasing order, you must find two numbers such that they add up to a target value. Return the indices of the two numbers as a list `[index1, index2]`, where `1 <= index1 < index2 <= numbers.length`. Only one valid solution exists, and each input must be used at most once.

## Example
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9.

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]
```

## Constraints
- 2 <= numbers.length <= 30,000
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists

---

## Solutions

### 1. Brute Force Solution
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
```
**Explanation:**
- Iterate through every pair of elements in the list.
- Check if any two numbers add up to the target.
- Return their indices (1-based) when found.

**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1)`

---

### 2. Hash Map Solution
```python
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []
```
**Explanation:**
- Use a hash map to store previously seen numbers and their indices.
- For each number, check if the complement (target - current number) exists in the map.
- If it does, return the stored index and current index.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

### 3. Two Pointers Solution (Optimal)
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
```
**Explanation:**
- Utilize the sorted nature of the array.
- Start with two pointers: one at the beginning (`l`) and one at the end (`r`).
- Move pointers inward based on whether the current sum is greater or smaller than the target.
- Stop and return indices when the correct pair is found.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## Most Optimal Solution
The **Two Pointers** solution is the most optimal because:
- It achieves linear time complexity `O(n)`.
- It uses constant extra space `O(1)`.
- It takes advantage of the input constraint that the array is already sorted.

This method is both efficient and clean, making it ideal for this problem.

---

## Conclusion
The Two Sum II problem teaches efficient searching techniques in sorted arrays. Starting with brute-force methods and evolving to optimized solutions like two-pointers is a good example of how to improve performance using DSA principles.