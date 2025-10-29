# Length of Longest Subarray With at Most K Frequency - LeetCode

## Problem Explanation

The problem **"Length of Longest Subarray With at Most K Frequency"** asks us to find the length of the longest contiguous subarray where no element appears more than **k times**.

In other words, you are given an integer array `nums` and an integer `k`. A subarray is called *good* if the frequency of each element in it is less than or equal to `k`. The task is to return the length of the longest such subarray.

### Example 1

**Input:** `nums = [1,2,3,1,2,3,1,2]`, `k = 2`
**Output:** `6`
**Explanation:** The longest good subarray is `[1,2,3,1,2,3]` because each number (1, 2, and 3) appears exactly twice.

### Example 2

**Input:** `nums = [1,2,1,2,1,2,1,2]`, `k = 1`
**Output:** `2`
**Explanation:** The longest good subarray is `[1,2]` or `[2,1]` because no number appears more than once.

### Example 3

**Input:** `nums = [5,5,5,5,5,5,5]`, `k = 4`
**Output:** `4`
**Explanation:** The longest good subarray is `[5,5,5,5]` because the number 5 appears four times.

---

## Code with Comments

```python
from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0                    # Stores the maximum length found so far
        count = defaultdict(int)   # Dictionary to store frequency of each element in the window
        l = 0                      # Left pointer of the sliding window

        # Iterate over each element using the right pointer
        for r in range(len(nums)):
            count[nums[r]] += 1     # Increase frequency of current element

            # If the current element's frequency exceeds k, move the left pointer
            while count[nums[r]] > k:
                count[nums[l]] -= 1  # Decrease frequency of element at left pointer
                l += 1               # Shrink the window from the left

            # Update result with the current valid window size
            res = max(res, r - l + 1)

        return res
```

---

## Approach and Logic Explained

### **Sliding Window Technique**

This problem is solved using the **sliding window** approach — a common pattern for subarray problems.

* We use two pointers `l` and `r` that define the current window.
* We expand the window by moving `r` to include more elements.
* If any element's frequency exceeds `k`, we shrink the window from the left (`l++`) until all elements satisfy the condition again.
* During this process, we track the **maximum window size** that meets the requirement.

### **Why Use a Dictionary (HashMap)?**

We use a `defaultdict(int)` to efficiently keep track of how many times each number appears within the current window.

### **Key Insight**

* Each number can appear at most `k` times in the subarray.
* The sliding window guarantees that we only check valid subarrays in **O(n)** time.

## Complexity Analysis

### **Time Complexity: O(n)**

* Each element is visited at most twice — once by the right pointer and once by the left pointer.
* Hence, the total work done is linear in relation to the array size.

### **Space Complexity: O(n)**

* In the worst case (all elements are unique), we store up to `n` keys in the frequency dictionary.

### **Optimality**

This **sliding window** solution is the most optimal approach because:

* It processes each element in constant time on average.
* It uses minimal extra space and avoids redundant checks that a brute-force method would perform.

---

## Test Cases

```python
sol = Solution()

# Test Case 1
print(sol.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))  # Expected output: 6

# Test Case 2
print(sol.maxSubarrayLength([1,2,1,2,1,2,1,2], 1))  # Expected output: 2

# Test Case 3
print(sol.maxSubarrayLength([5,5,5,5,5,5,5], 4))    # Expected output: 4
```