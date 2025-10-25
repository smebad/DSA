# Frequency of the Most Frequent Element - LeetCode

## Problem Explanation

The problem **"Frequency of the Most Frequent Element"** asks us to determine the highest possible frequency of any element in an array after performing at most `k` increment operations. Each operation allows you to choose an element in the array and increase its value by 1.

### Problem Statement

Given:

* An integer array `nums`.
* An integer `k`, representing the maximum number of increments allowed.

You need to **return the maximum possible frequency** of any element after performing at most `k` increments.

### Example

**Input:**

```
nums = [1,2,4], k = 5
```

**Output:**

```
3
```

**Explanation:** We can increment the first element three times and the second element two times to make all elements equal to 4 → `[4,4,4]`. The frequency of 4 is 3.

---

## Code Implementation

```python
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array to make it easier to work with increasing sequences
        total = res = 0
        l = 0  # Left pointer for the sliding window

        for r in range(len(nums)):
            total += nums[r]  # Add the current element to the running total

            # Check if we can make all elements in the current window equal to nums[r]
            # The condition ensures the total increments needed don't exceed k
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]  # Remove the leftmost element from the window
                l += 1  # Move the left pointer forward

            # Update the maximum frequency found so far
            res = max(res, r - l + 1)

        return res
```

### Code Explanation

* The array is first **sorted** to ensure all increments move elements toward a higher target value without decreasing any.
* A **sliding window** is used to represent a range of elements that can be made equal to the current rightmost element (`nums[r]`).
* The formula `nums[r] * (r - l + 1)` calculates the total value if all elements in the window were equal to `nums[r]`.
* `total + k` is the total value we can reach after spending at most `k` increments.
* If `nums[r] * (r - l + 1)` exceeds `total + k`, it means we cannot make all elements in the current window equal, so we **shrink the window** from the left by moving `l` forward.
* The result `res` keeps track of the **maximum window size**, representing the highest frequency achievable.

---

## Approach and Logic

### Sliding Window Approach (Efficient)

* Sort the array to align all elements in ascending order.
* Use a **sliding window** to efficiently track how many elements can be made equal to the current rightmost element using up to `k` increments.
* By expanding and shrinking the window dynamically, we find the largest window size that meets the condition.

This approach ensures we only traverse the array once after sorting, making it very efficient.

---

## Complexity Analysis

### Time Complexity: **O(n log n)**

* The array is sorted once → **O(n log n)**.
* The sliding window traverses the array once → **O(n)**.
* Overall: **O(n log n)**.

### Space Complexity: **O(1)**

* We use only a few integer variables (`l`, `total`, `res`), regardless of input size.
* Sorting can be done in-place, so no extra space is needed.

---

## Why This Solution Is Optimal

* Sorting gives a clear direction to move toward increasing all elements to match a higher target.
* The sliding window ensures each element is processed only once.
* By maintaining the total sum dynamically, we avoid recalculating sums repeatedly.

Thus, the combination of sorting and the sliding window technique provides the **most efficient** solution for this problem.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
nums1 = [1,2,4]
k1 = 5
print(sol.maxFrequency(nums1, k1))  # Expected Output: 3

# Test Case 2
nums2 = [1,4,8,13]
k2 = 5
print(sol.maxFrequency(nums2, k2))  # Expected Output: 2

# Test Case 3
nums3 = [3,9,6]
k3 = 2
print(sol.maxFrequency(nums3, k3))  # Expected Output: 1
```