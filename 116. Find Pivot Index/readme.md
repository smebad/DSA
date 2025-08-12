# Find Pivot Index - LeetCode

## Problem Description

Given an array of integers `nums`, the task is to find the **pivot index**.

The **pivot index** is defined as the index where the sum of all the numbers **strictly to the left** of the index is equal to the sum of all the numbers **strictly to the right**.

* If the index is on the left edge of the array, the left sum is considered `0`.
* If the index is on the right edge, the right sum is considered `0`.
* If multiple pivot indices exist, return the **leftmost** one.
* If no pivot index exists, return `-1`.

### Example 1:

**Input:**

```python
nums = [1, 7, 3, 6, 5, 6]
```

**Output:**

```
3
```

**Explanation:**

* Left sum = 1 + 7 + 3 = 11
* Right sum = 5 + 6 = 11

### Example 2:

**Input:**

```python
nums = [1, 2, 3]
```

**Output:**

```
-1
```

**Explanation:** No index satisfies the condition.

### Example 3:

**Input:**

```python
nums = [2, 1, -1]
```

**Output:**

```
0
```

**Explanation:**

* Left sum = 0 (no elements to the left)
* Right sum = 1 + (-1) = 0

**Constraints:**

```
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
```

---

## Brute Force Solution

```python
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            leftSum = rightSum = 0
            
            # Calculate sum of elements to the left of i
            for l in range(i):
                leftSum += nums[l]
            
            # Calculate sum of elements to the right of i
            for r in range(i + 1, n):
                rightSum += nums[r]
            
            # Check if both sums are equal
            if leftSum == rightSum:
                return i
        return -1
```

### How it works:

1. Loop over each index `i` in `nums`.
2. For each index, compute:

   * `leftSum`: sum of all elements before `i`.
   * `rightSum`: sum of all elements after `i`.
3. If they are equal, return the index.
4. If no index satisfies the condition, return `-1`.

**Time Complexity:** `O(n^2)` — For each index, we sum the elements on both sides.

**Space Complexity:** `O(1)` — No extra storage except variables.

---

## Prefix-Sum Solution (Efficient)

```python
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)  # Total sum of the array
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum  # Calculate right sum without extra loop
            if leftSum == rightSum:
                return i
            leftSum += nums[i]  # Move left sum forward
        
        return -1
```

### How it works:

1. Compute the **total sum** of the array.
2. Keep a running `leftSum` starting at `0`.
3. For each index `i`:

   * Calculate `rightSum` as `total - nums[i] - leftSum`.
   * If `leftSum == rightSum`, return `i`.
   * Add `nums[i]` to `leftSum` before moving to the next index.
4. If no pivot index is found, return `-1`.

**Time Complexity:** `O(n)` — We compute the total sum once, then iterate through the array once.

**Space Complexity:** `O(1)` — Only a few variables are used.

This is the **most optimal solution** because it avoids nested loops and calculates sums on the fly.

---

## Differences Between Solutions

| Aspect                | Brute Force Solution       | Prefix-Sum Solution   |
| --------------------- | -------------------------- | --------------------- |
| Time Complexity       | `O(n^2)` (slower)          | `O(n)` (faster)       |
| Space Complexity      | `O(1)`                     | `O(1)`                |
| Ease of Understanding | Easy                       | Medium                |
| Practical Use         | Only for very small inputs | Best for large inputs |

**Why Prefix-Sum is Optimal:**

* It calculates the right sum **without looping**, reducing time complexity to linear.
* It processes the array in a single pass after computing the total sum.

---

## Key Takeaways

* The pivot index is where left and right sums match.
* Brute force checks every index and recalculates sums each time, which is slow.
* The prefix-sum method reuses already calculated information to achieve `O(n)` time complexity.
* For large arrays, always prefer the prefix-sum approach.