# Find the Duplicate Number - LeetCode

## Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is only one repeated number. Return this repeated number.

### Constraints

* You must solve the problem **without modifying** the array `nums`.
* You must use only **constant extra space**.

### Example

```
Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3

Input: nums = [3,3,3,3,3]
Output: 3
```

---

## Solutions

### 1. Hash Set Solution

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()  # Create a set to track seen numbers
        for num in nums:
            if num in seen:  # If num is already seen, it's the duplicate
                return num
            seen.add(num)  # Add num to seen set
        return -1  # Should never reach here given problem constraints
```

**Time Complexity:** `O(n)` – We iterate through the array once.
**Space Complexity:** `O(n)` – In the worst case, we store all unique values in the set.

**Note:** This solution is not optimal due to its space usage, which violates the constant space requirement.

---

### 2. Array Marking Solution

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)  # Create an auxiliary array to mark seen numbers
        for num in nums:
            if seen[num - 1]:  # If already marked, it's the duplicate
                return num
            seen[num - 1] = 1  # Mark the number as seen
        return -1  # Should never reach here
```

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)` – Uses an extra array of the same size as input.

**Note:** Also violates the constant space requirement.

---

### 3. Fast and Slow Pointer (Floyd's Cycle Detection) – Optimal Solution

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # Phase 1: Find the intersection point of the two runners
        while True:
            slow = nums[slow]         # Move slow by 1 step
            fast = nums[nums[fast]]   # Move fast by 2 steps
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow2 = 0
        while True:
            slow = nums[slow]        # Move both pointers at the same speed
            slow2 = nums[slow2]
            if slow == slow2:
                return slow          # Duplicate number found
```

### Why This Works

This approach treats the array as a linked list where the value at each index points to the next index. Since there's a duplicate, a cycle must exist. Floyd's Tortoise and Hare algorithm is used to detect the cycle and identify the start of the loop — the duplicate.

**Time Complexity:** `O(n)` – Both phases of the algorithm traverse the array linearly.

**Space Complexity:** `O(1)` – Only a few pointers are used, satisfying the constant space constraint.

### Conclusion

The **Floyd's Tortoise and Hare** (fast and slow pointer) method is the optimal solution to the problem because:

* It does **not modify** the input array.
* It uses **constant extra space**.
* It has a linear time complexity, `O(n)`.

Other solutions like hash set or extra array are intuitive but do not meet the problem's constraints regarding space efficiency.
