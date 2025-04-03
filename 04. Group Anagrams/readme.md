# Contains Duplicate - LeetCode Blind 75

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Examples

#### Example 1:
**Input:**
```python
nums = [1,2,3,1]
```
**Output:**
```python
True
```
**Explanation:** The element `1` occurs at the indices `0` and `3`.

#### Example 2:
**Input:**
```python
nums = [1,2,3,4]
```
**Output:**
```python
False
```
**Explanation:** All elements are distinct.

#### Example 3:
**Input:**
```python
nums = [1,1,1,3,3,4,3,2,4,2]
```
**Output:**
```python
True
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Solution Explanation
To solve this problem efficiently, we use a **HashSet** data structure to keep track of the numbers we have seen so far.

### Approach:
1. Initialize an empty set called `hashset`.
2. Iterate through each element `n` in `nums`:
   - If `n` is already present in `hashset`, return `True` (since it is a duplicate).
   - Otherwise, add `n` to `hashset`.
3. If the loop completes without finding duplicates, return `False`.

### Code Implementation:
```python
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```

### Complexity Analysis
- **Time Complexity:** `O(n)`, where `n` is the length of the `nums` array. Each lookup and insertion operation in a hash set runs in **O(1)** on average, making the total complexity **O(n)**.
- **Space Complexity:** `O(n)`, as we store at most `n` elements in the hash set.

### Test Cases
```python
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
```

### Alternative Approaches
1. **Sorting Approach:** Sort the array and check if adjacent elements are the same.
   - **Time Complexity:** `O(n log n)` (due to sorting)
   - **Space Complexity:** `O(1)` (if sorting in-place) or `O(n)` (if using extra space)

2. **Brute Force Approach:** Use two nested loops to compare each element with every other element.
   - **Time Complexity:** `O(n^2)` (inefficient for large inputs)
   - **Space Complexity:** `O(1)` (no extra data structures used)

---

### Summary
✅ **Efficient HashSet-based solution with O(n) time complexity.**  
✅ **Handles large inputs efficiently.**  
✅ **Tested with multiple edge cases.**
